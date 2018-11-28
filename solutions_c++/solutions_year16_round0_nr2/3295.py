#include<bits/stdc++.h>

using namespace std;

typedef long long int ll;

FILE *fin=freopen("B-large.in","r",stdin);
FILE *fout=freopen("jam_final_q2_large_out.txt","w",stdout);

int main()
{
    ll t;cin>>t;
    ll c2=1;
    for(ll i=1;i<=t;i++)
    {
        ll c=0;
        string s;cin>>s;
        for(ll x=1;x<s.size();x++)
        {
            if(s[x]=='-' && s[x-1]=='+')
            {
                c++;
                for(ll y=0;y<x;y++)
                {
                    s[y]='-';
                }
            }
            else if(s[x]=='+' && s[x-1]=='-')
            {
                c++;
                for(ll y=0;y<x;y++)
                {
                    s[y]='+';
                }
            }
        }
        if (s.find('-') != string::npos)
        {
                printf("Case #%lld: %lld\n",i,c+1);
        }
        else
        {
                //cout<<"@@@@@@@@@@@@"<<endl;
                printf("Case #%lld: %lld\n",i,c);
        }

        c2++;
    }

}
