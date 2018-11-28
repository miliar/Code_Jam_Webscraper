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
    int t,x=1;scanf("%d",&t);
    while(t--){
        int n;
        scanf("%d",&n);
        string s;
        cin>>s;
        int cnt = 0;
        int ans = 0;
        for(int i=0;i<=n;++i){
            int need = max(0 , i-cnt);
            ans += need;
            cnt += s[i]-'0'+need;
        }
        printf("Case #%d: %d\n",x++,ans);
    }
    return 0;
}
