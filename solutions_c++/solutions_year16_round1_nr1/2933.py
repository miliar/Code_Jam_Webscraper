#include <bits/stdc++.h>

using namespace std;

int main()
{

    freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
int t,i,j;
string s,l;
scanf("%d",&t);
for(i=1;i<=t;i++)
{
    l="";
    cin>>s;
    for(j=0;j<s.size();j++)
    {
        if(j==0)
            l=l+s[0];
        else
            if(s[j]<l[0])
        {
            l=l+s[j];

        }
        else
        {
            l=s[j]+l;
        }
    }
    cout<<"Case #"<<i<<":"<<" "<<l<<"\n";
}
    return 0;
}
