#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll sum[1010];
int main()
{
    ll ans,temp,i,t,smax,var=0;
    string str;
    char ch;
    ifstream in("a.txt");
    ofstream out("b.txt");
    in>>t;
    while(t--)
    {
        var++;
        in>>smax;
        in>>str;
        ans=0;
        for(i=0;i<str.size();i++)
        {
            ch=str[i];
            temp=ch-48;
            if(i==0)
                sum[i]=temp;
            else
            sum[i]=sum[i-1]+temp;
        }
        for(i=0;i<str.size();)
        {
            if(sum[i]==0 && i==0)
                {
                    ans++;
                    i++;
                }
            else if(sum[i-1]+ans>i)
                i+=sum[i]+ans-i;
            else if(sum[i-1]+ans==i)
                i++;
            else
            {
                i++;
                ans++;
            }
        }
        out<<"Case #"<<var<<": "<<ans<<endl;
    }
}
