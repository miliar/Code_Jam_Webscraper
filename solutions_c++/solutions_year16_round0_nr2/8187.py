#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll l,i,t,z,d;
string s;
int main()
{
    ios_base::sync_with_stdio(0);
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
   cin>>t;
   while(t--)
   {
       cin>>s;
       l=s.size();d=0;
       for(i=l-1;i>=0;i--)
       {
           if(d%2&&s[i]=='+')
           {
               while(i>0&&s[i]=='+')
                i--;
               d++;i++;
           }
           else if(d%2==0&&s[i]=='-')
           {
               while(i>0&&s[i]=='-')
                i--;
               d++;
               i++;
           }
       }
       cout<<"Case #"<<++z<<": "<<d<<endl;
   }
}
