#include <bits/stdc++.h>

typedef long long ll;
using namespace std;

int m[1001];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    /*freopen("/Users/Ayur/Downloads/A-large.in","r",stdin);
    freopen("/Users/Ayur/Downloads/A-large-output.txt","w",stdout);*/
    int t,tt,n,i,soln1,soln2,r;
    cin>>t;
    for(tt=1;tt<=t;tt++)
    {
        cin>>n;
        for(i=0;i<n;i++)
        {
            cin>>m[i];
        }
        soln1=soln2=r=0;
        for(i=0;i<n-1;i++)
        {
            if(m[i]>m[i+1])
            {
                soln1 += m[i]-m[i+1];
                r = max(r,m[i]-m[i+1]);
            }
        }
        for(i=0;i<n-1;i++)
        {
            soln2 += min(m[i],r);
        }
        cout<<"Case #"<<tt<<": "<<soln1<<' '<<soln2<<'\n';
    }
    
    return 0;
}