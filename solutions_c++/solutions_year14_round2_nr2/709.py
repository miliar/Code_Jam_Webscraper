/*
Bismillahir Rahmanir Rahim
Coder: Ahmad Faiyaz
*/

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#include <fstream>
#include <ctime>


# define FOR(i, a, b) for (int i=a; i<b; i++)
# define REP(i, a) FOR(i,0,a)

#define EPS 1e-11
#define inf 1234567891
#define LL long long

#define abs(x) (((x)< 0) ? (-(x)) : (x))
#define all(x) (x).begin(), (x).end()
#define ms(x, a) memset((x), (a), sizeof(x))

#define pb push_back
#define FORIT(i,m) for(__typeof((m).begin()) i=(m).begin();i!=(m).end();i++)
#define pii pair<int,int>
#define UNIQUE(c) (c).resize( unique( all(c) ) - (c).begin() )

#define READ(f) {ifstream infile(f) ;if(infile.good()) freopen(f, "r", stdin);}
#define WRITE(f) freopen(f, "w", stdout)
#define CIN ios_base::sync_with_stdio(0);
///int rrr[]={1,0,-1,0};int ccc[]={0,1,0,-1}; //4 Direction
///int rrr[]={1,1,0,-1,-1,-1,0,1};int ccc[]={0,1,1,1,0,-1,-1,-1};//8 direction
///int rrr[]={2,1,-1,-2,-2,-1,1,2};int ccc[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
///int rrr[]={2,1,-1,-2,-1,1};int ccc[]={0,1,1,0,-1,-1}; //Hexagonal Direction
///int month[]={31,28,31,30,31,30,31,31,30,31,30,31}; //month

using namespace std;

string a, b;
string k;
string toBase( int number, int base ) {
    if(number== 0) return  "0";
    string ret = "";
    while( number )
    ret += ( number % base ) + '0',
    number /= base;
    reverse( ret.begin(), ret.end() );
    return ret;
}


LL mem [60][4][4][4][4];
LL dp(int idx, int sma, int smb, int smk, int ok){
    //cout<<idx<<" "<<sma<<" "<<smb<<" "<<smk<<" "<<ok<<endl;
    if(idx >= a.size()){
        return ok;
    }

    if(mem[idx][sma][smb][smk][ok] > -1 ) return mem[idx][sma][smb][smk][ok];
    LL ret = 0;

    int sta = 0, nda = 1;
    if(!sma){
        nda = a[idx]-'0';
    }
    int stb = 0, ndb = 1;
    if(!smb){
        ndb = b[idx]-'0';
    }

    for(int i=sta;i<=nda;i++){
        for(int j=stb;j<=ndb;j++){
            //cout<<"he "<<idx<<" "<<i<<" "<<j<<endl;
            int tma = 1;
            int tmb = 1;
            int bit = i & j;
            int tmk = 1;
            int ps = a.size() - idx - 1;
            int kk = (k[idx] - '0');
            int big = 0;
            if(bit){
                if(!smk){
                    if(kk < bit){
                        big = 1;
                        tmk = 0;
                    }else if(kk == bit){
                        tmk  = 0;
                    }
                }
            }else{
                if(kk == bit) tmk = 0;
            }
            if(i == nda) tma = 0;
            if(j == ndb) tmb = 0;

            ret = (ret + dp(idx+1, sma | tma , smb | tmb, smk | tmk, big|ok));
        }
    }
    return mem[idx][sma][smb][smk][ok]=ret;
}

int main(){
    #if defined( faiyaz_pc )
        READ("B-large.in");
        WRITE("large.txt");
    #endif

    int t, chk = 1;
    cin>>t;
    while(t--){
        LL aa, bb, kk;
        cin>>aa>>bb>>kk;
        LL v = aa*bb;
        if(kk >= aa && kk >= bb){
            cout<<"Case #"<<chk++<<": "<<v<<"\n";
            continue;
        }

        aa--, bb--;kk--;

        a = toBase(aa, 2);
        b = toBase(bb, 2);
        k = toBase(kk, 2);
        while(a.size() > b.size()){
            b = "0"+b;
        }

        while(b.size() > a.size()){
            a = "0"+a;
        }

        while(k.size() < a.size()){
            k = "0" + k;
        }
        ms(mem, -1);


        v = v - dp(0, 0, 0, 0,0);
        cout<<"Case #"<<chk++<<": "<<v<<"\n";
    }
    return 0;
}
