#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;

typedef vector<int>vi;
typedef pair<int,int>ii;
typedef vector<ii>vii;
#define M 1000000007
const int INF = (int) 1e9;
const int MAX = (int) 1e5 + 10;

int main()
{
    freopen("input.in","r",stdin);
    freopen("out.in","w",stdout);
    int t,n;
    string s;
    cin>>t;
    for(int ll=1;ll<=t;ll++)
    {
        cout<<"Case #"<<ll<<": ";
        cin>>n>>s;
        int people=0,ans=0;
        for(int i=0;i<=n;i++)
        {
            int y=s[i]-'0';
            //cout<<y<<" P "<<i<<" "<<people<<endl;
            if(people>=i)
            {
                people+=y;
            }
            else if(y>0)
            {
                ans+=(i-people);
                people+=y+ans;
              //    cout<<ans<<endl;
            }

        }
        cout<<ans<<endl;
    }
    return 0;
}
