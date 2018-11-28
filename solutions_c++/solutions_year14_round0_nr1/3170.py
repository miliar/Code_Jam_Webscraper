#include<algorithm>
#include<cassert>
#include<complex>
#include<map>
#include<iomanip>
#include<sstream>
#include<queue>
#include<set>
#include<string>
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
#define X first
#define Y second
#define FI X
#define SE Y
#define SQR(a) ((a)*(a))
#define DEBUG 1
#define debug(x) {if (DEBUG)cerr <<#x <<" = " <<x <<endl; }
#define debugv(x) {if (DEBUG) {cerr <<#x <<" = "; FORE(it, (x)) cerr <<*it <<", "; cout <<endl; }}
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int, int>P;
typedef vector<int>VI;
const int INF=1E9+7;
template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }
#define MAXN 100007

int main(){

    int T,R1,R2;
    int caseno=0;
    cin>>T;
    while(T--){
        caseno++;
        int table[17]={0};

        cin>>R1;
        for(int i=1;i<=4;i++){
            int x;
            if(i==R1){
                cin>>x;
                table[x]++;
                cin>>x;
                table[x]++;
                cin>>x;
                table[x]++;
                cin>>x;
                table[x]++;
            }else{
                cin>>x;
                cin>>x;
                cin>>x;
                cin>>x;
            }
        }

        cin>>R2;
        for(int i=1;i<=4;i++){
            int x;
            if(i==R2){
                cin>>x;
                table[x]++;
                cin>>x;
                table[x]++;
                cin>>x;
                table[x]++;
                cin>>x;
                table[x]++;
            }else{
                cin>>x;
                cin>>x;
                cin>>x;
                cin>>x;
            }
        }

        int twos = 0;
        int val=0;
        for(int i=1;i<=16;i++){
            if(table[i]==2) {twos++;val=i;}
        }

        if(twos==1){
            cout<<"Case #"<<caseno<<": "<<val<<endl;
        }else if(twos>1){
            cout<<"Case #"<<caseno<<": "<<"Bad magician!"<<endl;
        }else{
            cout<<"Case #"<<caseno<<": "<<"Volunteer cheated!"<<endl;
        }
    }

	return 0;
}

