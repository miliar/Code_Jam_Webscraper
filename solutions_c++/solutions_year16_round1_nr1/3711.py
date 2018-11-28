#include<bits/stdc++.h>
#define lld long long int
#define llu unsigned long long int
#define pb(x) push_back(x)
#define pii pair<int,int>
#define pll pair<lld,lld>
#define pq priority_queue<int> 
#define mp(x,y) make_pair(x,y)
#define sz size()
#define inp1(x) scanf("%d",&x)
#define inp2(x,y) scanf("%d%d",&x,&y)
#define inp3(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define print(x) printf("%d",x)
#define println(x) printf("%d\n",x)
#define _for(i,x,y) for(int i=x;i<y;i++)
using namespace std;
const int maxx=1e5+3;
lld mod=1e9+7;


int main()
{
    freopen("A.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,N;
    cin>>t;
    string S;
    _for(tc,1,t+1)
    {
        cin>>S;
        int len=S.length();
        string tmp,ans;
        ans+=S[0];
        _for(i,1,len)
        {
            if(S[i]>=ans[0])
            {
                tmp.clear();
                tmp+=S[i];
                tmp+=ans;
                ans.clear();
                ans+=tmp;    
            }
            else
            {
                ans+=S[i];
            }
        }
        cout<<"Case #"<<tc<<": "<<ans<<endl;
    }
    return 0;
}