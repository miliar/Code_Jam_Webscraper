// Headers
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cassert>
#include<vector>
#include<map>
#include<fstream>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
#include<bitset>
#include<set>
using namespace std;
// Global declarations
typedef long long int ll;
typedef vector<int> vi;
typedef vector<char> vc;
typedef pair<int,int> pi;
const double eps = 1e-6;
int const mod  = 1e9+7;
int const INF = 1<<29;
// Macros
#define mp make_pair
#define el putchar('\n')
#define sp putchar(' ')
#define Fill(a,val) memset(a,val,sizeof a)
#define pb push_back
#define ppb pop_back
#define gcd __gcd
#define all(a) a.begin(),a.end()
#define ff first
#define ss second

int main(){
    freopen("ip.in","r",stdin);
    freopen("op.out","w",stdout);
    vi v[20];
    v[1].pb(1);
    v[2].pb(1);v[2].pb(2);
    v[3].pb(1);
    v[4].pb(1);v[4].pb(2);
    v[6].pb(1);v[6].pb(2);v[6].pb(3);
    v[8].pb(1);v[8].pb(2);
    v[9].pb(1);v[9].pb(3);
    v[12].pb(1);v[12].pb(2);v[12].pb(3);v[12].pb(4);
    v[16].pb(1);v[16].pb(2);v[16].pb(4);
    int t,x=1;scanf("%d",&t);
    while(t--){
        int X,R,C;
        cin>>X>>R>>C;
        R *= C;
        int sz = v[R].size();
        bool GABRIEL = 0;
        for(int i=0;i<sz;++i){
            if(v[R][i] == X) GABRIEL = 1;
        }
        printf("Case #%d: %s\n",x++,(GABRIEL?"GABRIEL":"RICHARD"));
    }
    return 0;
}
