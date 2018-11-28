#include <bits/stdc++.h>
using namespace std;

typedef long long ll;


int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int t,l,k,j,cnt;
    cin>>t;
    int i=1;
    string s;
    while(i<=t)    {
        cnt=0;
        cin>>s;
        l=s.length();
        while(1)    {
            for(j=l-1;j>=0;j--)    {
                if(s[j]=='-')    break;
            }
            if(j==-1)    {
                cout<<"Case #"<<i<<": "<<cnt<<endl;
                break;
            }
            for(k=0;k<=j;k++)    {
                    if(s[k]=='-')    s[k]='+';
                    else    s[k]='-';
            }
            cnt++;
        }
        i++;
    }
    return 0;
}
