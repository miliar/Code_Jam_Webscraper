#include<bits/stdc++.h>
#define ll long long
using namespace std;


int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    ll tc,ca,i,n,shy,sum,len,a[1010];
    string s;

    cin>>tc;
    ca=0;
    while(tc--)
    {
        cin>>n>>s;

        len=s.size();
        shy=0;
        sum=s[0]-'0';
        for(i=1;i<len;i++)
        {

            if(i>sum)
            {
                shy+=(i-sum);
                sum+=(i-sum);
            }
            sum+=(s[i]-'0');
        }

        cout<<"Case #"<<++ca<<": "<<shy<<endl;
    }
}
