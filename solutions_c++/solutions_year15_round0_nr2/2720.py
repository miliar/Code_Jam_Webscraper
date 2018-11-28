//Hello. I'm Peter.
#include<cstdio>
#include<iostream>
#include<sstream>
#include<cstring>
#include<string>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<functional>
#include<cctype>
#include<ctime>
#include<stack>
#include<queue>
#include<vector>
#include<set>
#include<map>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
#define peter cout<<"i am peter"<<endl
#define input freopen("data.txt","r",stdin)
#define randin srand((unsigned int)time(NULL))
#define INT (0x3f3f3f3f)*2
#define LL (0x3f3f3f3f3f3f3f3f)*2
#define gsize(a) (int)a.size()
#define len(a) (int)strlen(a)
#define slen(s) (int)s.length()
#define pb(a) push_back(a)
#define clr(a) memset(a,0,sizeof(a))
#define clr_minus1(a) memset(a,-1,sizeof(a))
#define clr_INT(a) memset(a,INT,sizeof(a))
#define clr_true(a) memset(a,true,sizeof(a))
#define clr_false(a) memset(a,false,sizeof(a))
#define clr_queue(q) while(!q.empty()) q.pop()
#define clr_stack(s) while(!s.empty()) s.pop()
#define rep(i, a, b) for (int i = a; i < b; i++)
#define dep(i, a, b) for (int i = a; i > b; i--)
#define repin(i, a, b) for (int i = a; i <= b; i++)
#define depin(i, a, b) for (int i = a; i >= b; i--)
const double pi=acos(-1.0);
//const double eps=1e-9;
#define MOD 1000000007
#define MAXN 200100
#define N
#define M
int T;
int dp[1024],a[1024];
int ans;
int main(){
    //    input;
    //freopen("B-small-attempt2.in","r",stdin);
    //freopen("output.txt","w",stdout);
    scanf("%d",&T);
    repin(Case,1,T){
        int n;
        scanf("%d",&n);
        int maxi=0;
        repin(i,1,n){
            scanf("%d",a+i);
            maxi=max(maxi,a[i]);
        }
        int ans=INT;
        repin(j,1,maxi){
            int anst=j;
            repin(i,1,n){
                int t=a[i]/j;
                if(a[i]%j==0) t--;
                anst+=t;
            }
            ans=min(ans,anst);
        }
        printf("Case #%d: %d\n",Case,ans);
    }
    return 0;
}














































