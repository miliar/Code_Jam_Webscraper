#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    int t;
    cin>>t;
    int s,count1,n;
    string r;
    for(int i=1;i<=t;i++)
    {
        count1=0;
        n=0;
        cin>>s>>r;
        for(int i=0;i<r.length();i++)
        {
            if(i>count1&&r[i]!='0')
            {
                n=n+i-count1;
                count1=count1+r[i]-'0'+n;
            }
            else if(i<=count1&&r[i]!='0')
                count1=count1+r[i]-'0';
        }
        cout<<"Case #"<<i<<": "<<n<<endl;
    }
}
