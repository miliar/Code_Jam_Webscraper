#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
freopen("input.in","r",stdin);
freopen("output.txt","w",stdout);
ll t,i,len,k;
char c;
string st,str,temp;
cin>>t;

for(k=1;k<=t;k++)
{
    cin>>st;
    len=st.length();
    str=st[0];
    for(i=1;i<len;i++)
    {
        temp=st[i];

        if(str[0]<=st[i])
        {
           str=temp+str;
        }
        else
            str+=temp;
    }

    cout<<"Case #"<<k<<": ";
    for(i=0;i<len;i++)
        cout<<str[i];
    cout<<"\n";

}


return 0;
}
