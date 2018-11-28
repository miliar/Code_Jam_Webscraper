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

    int T;
    cin>>T;
    int caseno= 0;
    while(T--){
        caseno++;
        int N;
        cin>>N;
        //float Naomi[1000+1];
        vector<float> Naomi;
        //float Ken[1000+1];
        vector<float> Ken;

        for(int i=0;i<N;i++){
            float x;
            cin>>x;
            Naomi.push_back(x);
        }
        for(int i=0;i<N;i++){
            float x;
            cin>>x;
            Ken.push_back(x);
        }

        sort(Naomi.begin(),Naomi.end());
        sort(Ken.begin(),Ken.end());

        int deciet=0;

        int curN=0, lastN=N-1;
        int curK=0, lastK=N-1;

        //deciet
        while(curN<= lastN){
            if(Naomi[curN]> Ken[curK]){
                deciet++;
                curN++;
                curK++;
            }else{
                curN++;
                lastK--;
            }

        }

        // War
        int war =0;

        curN=0; lastN=N-1;
        curK=0; lastK=N-1;

        while(curN<= lastN){
            if(Naomi[lastN]>Ken[lastK]){
                    war++;
                    lastN--;
            }else{
                lastN--;
                lastK--;
            }
        }
        cout<<"Case #"<<caseno<<": "<<deciet<<" "<<war<<endl;
    }

	return 0;
}

