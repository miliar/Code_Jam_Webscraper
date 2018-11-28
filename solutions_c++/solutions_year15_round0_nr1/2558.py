#include<cstdio>
#include<cstring>
#include<cmath>
#include<string>
#include<algorithm>
#include<iostream>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<stack>

#define msn(x) (memset((x),0,sizeof((x))))
#define msx(x) (memset((x),0x7f,sizeof((x))))
#define fuck(x) cerr << #x << " <- " << x << endl
#define acer cout<<"sb"<<endl
typedef long long ll;
using namespace std;
#define inf 0x3f3f3f3f
#define eps 1e-8
#define pi acos(-1.0)

string s;
int n;

int main()
{
   // freopen("A-small-attempt0.out","w",stdout);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        scanf("%d",&n);
        cin>>s;
        int ans=0;
        int now=s[0]-'0';
        int cmp;
        for(cmp=n;cmp>=0;cmp--)
        {
            if(s[cmp]>'0')break;
        }
       // fuck(cmp);
        for(int i=1;i<=cmp;i++)
        {
            if(now<i)ans+=i-now,now=i;
            now+=(int)(s[i]-'0');
        }
        printf("Case #%d: %d\n",cas,ans);
    }
     return 0;
}
