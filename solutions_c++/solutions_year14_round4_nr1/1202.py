#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<map>
#include<set>
#include<cmath>

using namespace std;

#define mp make_pair
#define pb push_back
#define forn(i,n) for(int i=0;i<(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)
#define all(v) v.begin(),v.end()

int main()
{
    int T;
    cin>>T;
    forn(t,T)
    {
        int n,x;
        cin>>n>>x;
        vector<int>l(n),u(n);
        forn(i,n)cin>>l[i];
        int ans=0;
        sort(all(l));
        reverse(all(l));
        forn(i,n)if(u[i]==0)
        {
            u[i]=1;
            ans++;
            for(int j=i+1;j<n;j++)if(u[j]==0 and l[i]+l[j]<=x)
            {
                u[j]=1;
                break;
            }
        }
        cout<<"Case #"<<t+1<<": "<<ans<<endl;
    }
}
