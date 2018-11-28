//Copyright of code reserved with Arpit Bajaj
//Date : 09-04-2016
#include<bits/stdc++.h>
#define pii pair<int,int>
#define ll long long
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define ll long long
#define debug(x) cout<<">value ("<<#x<<") : "<<x<<endl;
#define MOD 1000000007
using namespace std;
string flip(string s, int idx)
{
    string temp=s;
    int i,j=idx;
    for(i=0;i<=idx;i++)
    {
        if(s[j]=='+')
            temp[i]='-';
        else
            temp[i]='+';
        j--;
    }
    return temp;
}
int main()
{
    ios_base::sync_with_stdio(false);
        cin.tie(NULL);
    freopen("inlarge.in","r",stdin);
    freopen("outlarge.txt","w",stdout);
    int t,test;
    cin>>test;
    for(t=1;t<=test;t++)
    {
        string s,p;
        cin>>s;
        p=s;
        int i,n=s.size(),j,ans=0;
        for(i=n-1;i>=0;i--)
        {
            if(s[i]=='-')
            {
                int maxi=INT_MIN,tmaxi=0,maxidx=-1;
                //debug(maxi);
                //debug(tmaxi);
                //debug(maxidx);
                for(j=0;j<i;j++)
                {
                    if(s[j]=='+')
                    {
                        tmaxi+=1;
                        if(tmaxi>maxi)
                        {
                            maxi=tmaxi;
                            maxidx=j;
                        }
                    }
                    else
                    {
                        tmaxi-=1;
                    }
                    //debug(j);
                    //debug(tmaxi);
                }
                //debug(maxi);
                //debug(maxidx);
                if(maxi>0)
                {
                    int m=0;
                    if(s[m]=='-')
                    {
                        while(s[m]=='-')
                        {
                            s[m]='+';
                            m++;

                        }
                        ans++;
                    }
                    if(s[i]=='-')
                    {
                        s=flip(s,maxidx);
                        ans++;
                    }
                    //debug(s);
                }
                if(s[i]=='-')
                {
                s=flip(s,i);
                //debug(s);
                ans++;
                }
            }
        }

        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}
