#include <bits/stdc++.h>

using namespace std;

string C,J;
vector<int> mc, mj;
vector<int> cValues, jValues;
int cAns, jAns;

const int oo = 100000;

inline digits(int num){
    if(num <= 9) return 1;
    int ctr = 0;
    while(num){
       num /= 10;
       ++ctr;
    }

    return ctr;
}

void bt( int i, int j ){
    if( i >= mc.size() && j >= mj.size() ){

        int x = 0, y = 0;
        int a = 0, b = 0;
        for(int k=0; k<C.size(); k++){
            a *= 10;
            if( C[k] == '?' )
                a += cValues[x++];
            else
                a += C[k] - '0';
        }

        for(int k=0; k<J.size(); k++){
            b *= 10;
            if( J[k] == '?' )
                b += jValues[y++];
            else
                b += J[k] - '0';
        }

//        for(auto &lel : cValues) cout << lel << " "; cout << endl;
//        for(auto &lel : jValues) cout << lel << " "; cout << endl;
//        cout << a << " " << b << endl;


        int xd = abs(a-b);
        int aux = abs(cAns-jAns);

        if( aux > xd ){
          cAns = a;
          jAns = b;
        } else if( aux == xd ){
            if( cAns > a ){
                cAns = a;
                jAns = b;
            }else if( cAns == a && jAns > b ){
                cAns = a;
                jAns = b;
            }
        }
//        cout << cAns << " " << jAns << endl;
        return;
    }

    for(int n=0; n<10; n++){
        if( i < mc.size() ){
            cValues[i] = n;
            bt(i+1,j);
        }

        if( j < mj.size() ){
            jValues[j] = n;
            bt(i,j+1);
        }
    }
}


int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("BSmall.out","w",stdout);
    int T;
    cin >> T;

    for(int cases=1; cases<=T; cases++){
        cin >> C >> J;


        mc = vector<int>();
        mj = vector<int>();
        for(int i=0; i<C.size(); i++)
            if( C[i] == '?' )
                mc.push_back(i);


        for(int i=0; i<J.size(); i++)
            if( J[i] == '?' )
                mj.push_back(i);

        cValues.assign(mc.size(),-1);
        jValues.assign(mj.size(),-1);

        cAns = oo;
        jAns = oo*2;
        bt(0,0);

        int dc = C.size() - digits(cAns), dj = J.size() - digits(jAns);

        cout << "Case #" <<cases << ": ";

        for(int i=0; i<dc; i++) cout << 0;
        cout << cAns << " ";

        for(int i=0; i<dj; i++) cout << 0;
        cout << jAns << " ";
        cout << endl;

    }

}
