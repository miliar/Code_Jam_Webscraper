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
char s[1024];
int lens;
int main(){
    //    input;
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("output.txt","w",stdout);
    scanf("%d",&T);
    int kase=1;
    while(T--){
        scanf("%d",&lens);
        scanf("%s",s);
        int ans=0,sum=0;
        repin(i,0,lens){
            int t=s[i]-'0';
            if(sum<i&&t){
                int t1=i-sum;
                ans+=t1;
                sum+=t1;
            }
            sum+=t;
        }
        printf("Case #%d: %d\n",kase++,ans);
    }
    return 0;
}


