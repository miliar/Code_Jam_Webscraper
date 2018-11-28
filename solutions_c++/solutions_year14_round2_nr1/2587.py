


#include<algorithm>
#include<cassert>
#include<complex>
#include<map>
#include<iomanip>
#include<sstream>
#include<queue>
#include<set>
#include<string>
#include<cstdio>
#include<vector>
#include<iostream>
#include<cstring>
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define fup FOR
#define fdo FORD
#define REP(i, n) for(int i = 0;i <(n); ++i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define siz SZ
#define CLR(x) memset((x), 0, sizeof(x))
#define PB push_back
#define MP make_pair
//#define X first
#define Y second 
#define FI X
#define SE Y
#define SQR(a) ((a)*(a))
#define DEBUG 1
#define debug(x) {if (DEBUG)cerr <<#x <<" = " <<x <<endl; }
#define debugv(x) {if (DEBUG) {cerr <<#x <<" = "; FORE(it, (x)) cerr <<*it <<", "; cout <<endl; }}
#define SETALL(x,l,v) for(int i=0;i<l;++i){x[i]=v;}
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int, int>P;
typedef vector<int>VI;
const int INF=1E9+7;
int T;
int C;
int D;
int N;
string words[1001];
char chars[101];
int charcount[1001][101];
int howchars;



bool elgawon;
int res;


void addtores(int x) {
    //adds best option
    int mysum = 0;
    FOR(IN,1,N) {
        mysum+= charcount[IN][x];
    }
    double lol = (double) mysum/N;
    //debug(lol);
    lol +=0.5;
    int meh = lol;

    FOR(IN,1,N) {
        res+=abs(meh-charcount[IN][x]);
    }

}

int main() {
    ios::sync_with_stdio(0);
    cout << setprecision(15) << fixed;
    cin>>T;
    FOR(IT,1,T) {
        cin>>N;
        res=0;
        howchars=0;
        elgawon=false;
        FOR(IN,0,100) {
            //        charcount[IN]=0;
            chars[IN] = '.';
        FOR(INN,0,1000) {
charcount[INN][IN] = 0;
        }
        }


        FOR(IN,1,N) {
            cin>>words[IN];
        }
        int wsize = words[1].length()-1;

        FOR(IK,0,wsize) {
            if(chars[howchars] != words[1][IK]) {
                if(chars[howchars] == '.') {
                    chars[howchars]=words[1][IK];
                    charcount[1][howchars]=1;

                }
                else {
                    //inny znak
                    howchars++;
                    chars[howchars] = words[1][IK];
                    charcount[1][howchars]=1;
                }
            }
            else {
                charcount[1][howchars]++;

            }

        }

        FOR(IN,2,N) {
            int wsize = words[IN].length()-1;
            int myhowchars=0;
            FOR(IK,0,wsize) {
                if(chars[myhowchars] != words[IN][IK]) {
                    if(chars[myhowchars] == '.') {
                        
                        //  chars[howchars]=words[1][IK];
                        //  charcount[1][howchars]=1;
                        elgawon=true;
                        goto costam;
                    }
                    else {
                        //inny znak
                        if(charcount[IN][myhowchars] == 0) {
                       // debug(chars[myhowchars]);
                       // debug(words[IN][IK]);
                            elgawon = true;
                        goto costam;
                        }
                        myhowchars++;
                        if(chars[myhowchars] != words[IN][IK]) {
                            elgawon=true;
                            goto costam;
                        }
                        charcount[IN][myhowchars]=1;
                    }
                }
                else {
                    charcount[IN][myhowchars]++;

                }

            }
            if(myhowchars!=howchars) {
            elgawon=true;
            goto costam;
            }

        }
/*
        FOR(IC,0,howchars) {
cout<<chars[IC]<<endl;
FOR(IN,1,N) {
cout<<charcount[IN][IC]<<" ";
}
cout<<endl;
}
*/
        FOR(IC,0,howchars) {

            addtores(IC);
        }


costam:
        if(elgawon) {
            cout<<"Case #"<<IT<<": Fegla Won"<<endl;

        }
        else {
            cout<<"Case #"<<IT<<": "<<res<<endl;
        }
    }
    return 0;
}


