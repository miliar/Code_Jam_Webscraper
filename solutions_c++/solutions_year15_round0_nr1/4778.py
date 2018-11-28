#include<bits/stdc++.h>
#define F first
#define S second
#define mp(x,y) make_pair(x,y)
#define popb(x) pop_back(x)
#define pushb(x) push_back(x)
#define popf(x) pop_front(x)
#define pushf(x) push_front(x)
#define ALL(x) x.begin(),x.end()
#define INIT(x,y) memset(x,y,sizeof x)
#define fori(x,y) for(i=x;i<y;i++)
#define forj(x,y) for(j=x;j<y;j++)
#define INF 1e9
#define EPS 1e-9
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w+",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t,tt,i,n,temp,ans;
    string s;
    cin>>tt;
    for(t=1;t<=tt;t++)
    {
        ans=0;
        temp=0;
        cin>>n>>s;
        fori(0,n+1)
        {
            if(temp<i)
            {
                ans+=i-temp;
                temp=i;
            }
            temp+=s[i]-'0';
        }
        cout<<"Case #"<<t<<": "<<ans<<"\n";
    }
    return 0;
}
