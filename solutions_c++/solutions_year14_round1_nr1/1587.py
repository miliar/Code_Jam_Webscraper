#include<iostream>
#include<algorithm>
#include<cmath>
#include<string>
#include<climits>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<fstream>

#define ll long long int
#define pb push_back
#define mod 1000000007

using namespace std;

ll pow1(ll a,ll b)
{
    ll ans=1,i;
    for(i=0;i<b;i++)
        ans=ans*a;
    return ans;
}

int main()
{
    int t,w=1;
    cin>>t;
    while(t--)
    {
        ll i,j,k,l,m,n,ans=-1;
        string s[100],p[100];
        cin>>n>>l;
        for(i=0;i<n;i++)
        {
            cin>>s[i];
        }
        sort(s,s+n);
        for(i=0;i<n;i++)
        {
            cin>>p[i];
        }
        sort(p,p+n);

        m=pow1(2,l);

        for(i=0;i<m;i++)
        {
            int fr[20]={0},co=0;
            for(j=0;j<l;j++)
            {
                if((i&(1<<j)))
                {
                    fr[j]=1;
                    co++;
                }
            }
            string temp[100];
            for(j=0;j<l;j++)
            {
                for(k=0;k<n;k++)
                {
                    if(fr[j]==1)
                    {
                        if(s[k][j]=='0')
                            temp[k]+='1';
                        else
                            temp[k]+='0';
                    }
                    else
                        temp[k]+=s[k][j];
                }
            }

            sort(temp,temp+n);
            int flag=0;
            for(j=0;j<n;j++)
            {
                if(p[j]!=temp[j])
                    flag=1;
            }
            if(flag==0)
            {
                ans=co;
                break;
            }
        }
        if(ans==-1)
        {
            cout<<"Case #"<<w<<": "<<"NOT POSSIBLE\n";
        }
        else
        {
            cout<<"Case #"<<w<<": "<<ans<<"\n";
        }
        w++;
    }
    return 0;
}
