#include<cstdio>
#include<cctype>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<iostream>
#include<complex>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<stack>
#include<algorithm>
#include<utility>
#include<list>
#include<bitset>
using namespace std;

#define LL long long
#define LL_ __int64
#define rep(i,j,k) for(int i=(j);i<=(k);i++)
#define repp(i,j,k) for(int i=(j);i>=(k);i--)
#define Add(u,v,w) {E[++tot]=(Edge){u,v,w,Last[u]}; Last[u]=tot;}
#define mst(i,j) memset(i,j,sizeof(i))
#define scf(i) scanf("%d",&(i))
#define scff(i,j) scanf("%d%d",&(i),&(j))
#define scfs(i) scanf("%s",(i))
#define pdd pair<double,double>
#define pii pair<int,int>
#define vec vector
#define mp make_pair
#define bt bitset
#define pq priority_queue
#define bgn begin
#define ist insert
#define fnd find
#define cnt count
#define rmv remove
#define psb push_back
#define lbd lower_bound
#define ubd upper_bound
#define bsc binary_search
#define fst first
#define scd second
#define psh push
#define frt front
#define ers erase
#define rvs reverse
#define it iterator

#define MOD 1000000007
#define maxn 500010
#define maxm 300010
#define pi acos(-1.0)
#define INF 0x7fffffff
#define eps 1e-5
#define IN freopen("In.txt","r",stdin)
#define OUT freopen("Out.txt","w",stdout)
#define CMP system("comp In.txt Out.txt")
#define mod 1000000000000000
#define double long double


int main(){//IN; OUT;
    int T; scf(T); int kase=1;
    while(T--){
        string s,ans; cin>>s;
        int len=s.length(); ans+=s[0];
        rep(i,1,len-1){
            if(s[i]>=ans[0]){
                char ch[2]={0}; ch[0]=s[i];
                ans.insert(0,ch);
            }
            else ans+=s[i];
        }
        printf("Case #%d: ",kase++); cout<<ans<<endl;
    }
    return 0;
}
