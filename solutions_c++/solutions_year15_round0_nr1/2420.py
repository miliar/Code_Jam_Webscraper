#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define mp make_pair
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,q=0;
    cin>>t;
    while(t--)
    {
        q++;
        ll n,i,j,ans=0;
        string s;
        cin>>n>>s;
        ll len=n+1;
        ll req=0,cl=0;
        cl=s[0]-'0';
        for(i=1;i<len;i++)
        {
            req=i;
            if(req<=cl)
            {
                cl+=s[i]-'0';
            }
            else
            {
                ans+=req-cl;
                cl=req+s[i]-'0';
            }
        }
        cout<<"Case #"<<q<<": "<<ans<<"\n";
    }
    return 0;
}
/*
6
4 11111
1 09
5 110011
0 1
6 0000006
9 0000021001
*/
