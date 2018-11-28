#include <algorithm>
#include <vector>
#include <iostream>
#include <fstream>

#define TEST

using namespace std;

enum QBasis{
    UD, // undefined
    PI,
    PJ,
    PK,
    MI,
    MJ,
    MK,
    P1,
    M1,
};

QBasis Q(char c)
{
    if(c=='i') return QBasis::PI;
    if(c=='j') return QBasis::PJ;
    if(c=='k') return QBasis::PK;
    else return QBasis::UD;
}

QBasis operator-(const QBasis& b)
{
    QBasis nb;
    if(b==QBasis::PI) nb = QBasis::MI;
    if(b==QBasis::PJ) nb = QBasis::MJ;
    if(b==QBasis::PK) nb = QBasis::MK;
    if(b==QBasis::MI) nb = QBasis::PI;
    if(b==QBasis::MJ) nb = QBasis::PJ;
    if(b==QBasis::MK) nb = QBasis::PK;
    if(b==QBasis::P1) nb = QBasis::M1;
    if(b==QBasis::M1) nb = QBasis::P1;
    return nb;
}

QBasis operator*(const QBasis& b0, const QBasis& b1)
{
    if(b0==QBasis::M1) return -b1;
    else if(b1==M1) return -b0;
    else if(b0==P1) return b1;
    else if(b1==P1) return b0;
    else if(b0==PI && b1==PJ) return QBasis::PK;
    else if(b0==PJ && b1==PK) return QBasis::PI;
    else if(b0==PK && b1==PI) return QBasis::PJ;
    else if(b0==PJ && b1==PI) return QBasis::MK;
    else if(b0==PK && b1==PJ) return QBasis::MI;
    else if(b0==PI && b1==PK) return QBasis::MJ;
    else if(b0==b1) return M1;
    else if(b1==PI || b1==PJ || b1==PK)
        return(-((-b0)*b1));
    else if(b0==PI || b0==PJ || b0==PK)
        return(-(b0*(-b1)));
    else
        return(-((-b0)*(-b1)));
}

ostream& operator<<(ostream& c, const QBasis& b)
{
    switch(b)
    {
    case QBasis::PI: c << "i";  break;
    case QBasis::PJ: c << "j";  break;
    case QBasis::PK: c << "k";  break;
    case QBasis::MI: c << "-i"; break;
    case QBasis::MJ: c << "-j"; break;
    case QBasis::MK: c << "-k"; break;
    case QBasis::P1: c << "1";  break;
    case QBasis::M1: c << "-1"; break;
    default: c << "QBasis undefined :(";
    }
    return c;
}

QBasis reduce(vector<QBasis> qs)
{
    if(qs.empty()) return QBasis::UD;
//    if(qs.size() > 4)
//    {
//        vector<QBasis> qs1 = vector<QBasis>(qs.begin(), qs.begin()+qs.size()/2);
//        vector<QBasis> qs2 = vector<QBasis>(qs.begin()+qs.size()/2, qs.end());
//        return reduce(qs1)*reduce(qs2);
//    }
//    else
    {
        auto q = qs.front();
        for(uint i=1; i<qs.size(); ++i)
            q = q*qs[i];
        return q;
    }
}

QBasis reduce(string str)
{
    if(str.empty()) return QBasis::UD;
//    if(str.size() > 4)
//    {
//        string str1 = string(str.begin(), str.begin()+str.size()/2);
//        string str2 = string(str.begin()+str.size()/2, str.end());
//        return reduce(str1)*reduce(str2);
//    }
//    else
    {
        auto q = Q(str.front());
        for(uint i=1; i<str.size(); ++i)
            q = q*Q(str[i]);
        return q;
    }
}

QBasis pow(QBasis _q, int N)
{
    N %= 4;
    QBasis q = _q;
    for(int j=1; j<N; ++j)
        q = q*_q;
    return q;
}

// find the first k
int find(string& str, const QBasis& _q, const QBasis& _start=QBasis::P1)
{
    int i = 0;
    QBasis q = _start;
    bool found = false;
    do{
        q = q*Q(str[i++]);
        if(q==_q)
            found = true;
    } while (!found && i<str.size());
    if(found)
    {
        str.erase(str.begin(), str.begin() + i);
        return i;
    }
    else return 0;
}

vector<QBasis> Qs(string str)
{
    vector<QBasis> qs;
    qs.reserve(str.size());
    for(auto c : str) qs.push_back(Q(c));
    return qs;
}

int find(vector<QBasis>& qs, const QBasis& _q, const QBasis& _start=QBasis::P1)
{
    int i = 0;
    QBasis q = _start;
    bool found = false;
    if(qs.empty()) return 0;
    do{
        q = q*qs[i++];
        if(q==_q)
            found = true;
    } while (!found && i<qs.size());
    if(found)
    {
#ifdef TEST
        {
            cout << "size of qs before removal: " << qs.size() << endl;
            cout << "i = " << i << endl;
            cout << "characters to be removed: ";
            vector<QBasis> to_remove;
            for(int j=0; j<i; j++) to_remove.push_back(qs[j]);
            for(int j=0; j<i; j++) cout << qs[j];
            cout << endl;
            cout << "they reduce to: " << reduce(to_remove) << endl;
        }
#endif
        qs.erase(qs.begin(), qs.begin() + i);

#ifdef TEST
            cout << "size of qs after removal: " << qs.size() << endl;
#endif
        return i;
    }
    else return 0;
}

int main()
{
    ifstream fin("in.txt");
    ofstream fout("out.txt");
    int N;
    fin >> N;
#ifdef TEST
    {
//        N = 0;
    }
#endif
    cout << "N: " << N << endl;
    for(int i=0; i<N; ++i)
    {
        int L, X;
        fin >> L;
        fin >> X;
//        cout << "L: " << L << ", X: " << X << endl;
        string str;
        fin >> str;

        // test
//        {
//            str.clear();
//            for(int i=0; i<6+80000; ++i)
//                str += "ji";
//        }
//        X = 1;

        bool GOOD = false;

        vector<QBasis> qs;

//        if(X>20)
        if(0)
        {
            QBasis reduced = reduce(str);
            QBasis middle = pow(reduced, X - 20);
//            cout << "middle: " << middle << endl;
            string front, back;
            for(int i=0; i<10; ++i)
            {
                front += str;
                back += str;
            }
            vector<QBasis> qs_front = Qs(front);
            vector<QBasis> qs_back = Qs(back);
            qs.insert(qs.end(), qs_front.begin(), qs_front.end());
            qs.push_back(middle);
            qs.insert(qs.end(), qs_back.begin(), qs_back.end());
        }
        else
        {
            string full;
            for(int i=0; i<X; ++i)
                full += str;
            vector<QBasis> qs_full = Qs(full);
            qs.insert(qs.end(), qs_full.begin(), qs_full.end());
        }


        bool SumGood = (reduce(qs)==reduce("ijk"));

        if(find(qs, QBasis::PI))
        {
//            cout << "size of qs after i is found: " << qs.size() << endl;
//            for(auto q : qs) cout << q;
            if(find(qs, QBasis::PJ))
            {
//                for(auto q : qs) cout << q;
//                cout << "size of qs after j is found: " << qs.size() << endl;
//                cout << endl;
                auto final = reduce(qs);
                cout << "final: " << final << endl;
//                if((reduce(qs)) == QBasis::PK)
                if(final == QBasis::PK)
                    GOOD = true;
            }
        }

        fout << "Case " << "#" << i+1 << ": " << (GOOD ? "Yes" : "No") << endl;

        if(SumGood != GOOD)
        {
            cout << endl << "WARNING!!!!!!!!!!!!!!!!!!!!!!!!!" << endl;
            if(GOOD)
                cout << "Fatal!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" << endl << endl;
            cout << "ijk = " << reduce("ijk") << endl;
        }

        cout << "Case " << "#" << i+1 << ": " << (GOOD ? "Yes" : "No") << endl;
        cout << "Case " << "#" << i+1 << " Reduced Sum Equal: " << (SumGood ? "Yes" : "No") << endl << endl;
    }
    fin.close();
    fout.close();

    vector<QBasis> qs{QBasis::P1, QBasis::PI, QBasis::PJ, QBasis::PK};

#ifdef TEST
    for(auto q : qs)
    {
        for(auto p : qs)
            cout << q*p << " ";
        cout << endl;
    }

    cout << "k*-k: " << QBasis::PK*QBasis::MK << endl;
    cout << "i*j*k: " << QBasis::PI*QBasis::PJ*QBasis::PK << endl;
    cout << "i*j*-k: " << QBasis::PI*QBasis::PJ*QBasis::MK << endl;
#endif

}










