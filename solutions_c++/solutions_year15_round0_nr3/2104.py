#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

struct quat{
    unsigned q;
    int sign;

    quat(const quat& q2){
        this->q = q2.q;
        this->sign = q2.sign;
    }

    quat(const string& qu){
        this->q = 0;
        assert(qu.length() >= 1 && qu.length() <= 2);
        if(qu[0] == '-')
            this->sign = -1;
        else
            this->sign = 1;
        char v;
        if(qu[0] == '-' || qu[0] == '+'){
            assert(qu.length() == 2);
            v = qu[1];
        }
        else
            v = qu[0];
        switch(v){
            case '1':
                this->q = 1;
                break;
            case 'i':
                this->q = 2;
                break;
            case 'j':
                this->q = 3;
                break;
            case 'k':
                this->q = 4;
                break;
            default:
                assert(false);
        }
    }

    quat& operator*=(const quat& q2){
        int lut[4][4] = {{1, 2, 3, 4},
        {2, -1, 4, -3},
        {3, -4, -1, 2},
        {4, 3, -2, -1}};
        int r = lut[this->q-1][q2.q-1]*this->sign*q2.sign;
        this->sign = 1;
        if(r<0)
            this->sign = -1;
        this->q = r*this->sign;
        return *this;
    }
};

quat operator*(const quat& q1, const quat& q2){
    quat res=q1;
    res*=q2;
    return res;
}

bool operator==(const quat& q1, const quat& q2){
    return q1.q == q2.q && q1.sign == q2.sign;
}

bool operator!=(const quat& q1, const quat& q2){
    return !(q1==q2);
}

void printquattest(){
    quat q1 = quat("1");
    quat q2 = quat("i");
    quat q3 = quat("j");
    cout << "1=" << q1.q << "*" << q1.sign << ", i=" << q2.q << "*" << q2.sign << ", j=" << q3.q << "*" << q3.sign << endl;
    quat q4 = q1*q2;
    cout << "1*i=" << q4.q << "*" << q4.sign << endl;
    q4 *= q3;
    cout << "1*i*j=" << q4.q << "*" << q4.sign << endl;
    cout << "i*i==i*j*i*j:" << ((q2*q2)==(q4*q4)) << endl;
}

int main(){
    //printquattest();
    const quat iquat = quat("i");
    const quat jquat = quat("j");
    const quat kquat = quat("k");
    unsigned t;
    cin >> t;
    for(unsigned tc = 1; tc <= t; ++tc){
        unsigned long long l, x;
        cin >> l >> x;
        string s;
        cin >> s;
        vector<quat> qs;
        for(unsigned i = 0; i < s.length(); ++i)
            qs.push_back(quat(s.substr(i,1)));
        unsigned j = 0;
        unsigned i = 0;
        quat c("1");
        for(j = 0; j < x; ++j){
            for(i = 0; i < l; ++i){
                c *= qs[i];
                //cout << c.q << "*" << c.sign << " ";
                if(c == iquat){
                    //cout << "Found minimal i part: r0c0 to r" << j << "c" << i << endl;
                    break;
                }
            }
            if(c == iquat)
                break;
        }
        if(c != iquat){
            cout << "Case #" << tc << ": NO" << endl;
            continue;
        }
        //unsigned long long iend = j*l+i;
        c = quat("1");
        ++i;
        for(; j < x; ++j){
            for(; i < l; ++i){
                c *= qs[i];
                //cout << c.q << "*" << c.sign << " ";
                if(c == jquat){
                    //cout << "Found minimal j part: to r" << j << "c" << i << endl;
                    break;
                }
            }
            if(c == jquat)
                break;
            i = 0;
        }
        if(c != jquat){
            cout << "Case #" << tc << ": NO" << endl;
            continue;
        }
        //unsigned long long jend = j*l+i;
        c = quat("1");
        ++i;
        for(; j < x; ++j){
            for(; i < l; ++i){
                c *= qs[i];
                //cout << c.q << "*" << c.sign << " ";
            }
            i = 0;
        }
        if(c != kquat){
            cout << "Case #" << tc << ": NO" << endl;
            continue;
        }
        cout << "Case #" << tc << ": YES" << endl;
    }
    return 0;
}
