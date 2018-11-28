#include <iostream>
#include<string>
using namespace std;
int main()
{
   freopen("input.txt","r" , stdin);
   freopen("ans.txt","w" , stdout);
    int T; cin>>T;
    for(int w=0;w<T;w++)
    {
       string s; cin>>s; int k; cin>>k; int ans=0; bool flag=true;
       for(int i=0;i<s.size()-k+1;i++)
       {
           if(s[i]=='-')
           {
               for(int j=0;j<k;j++) {if(s[i+j]=='+') s[i+j]='-'; else s[i+j]='+';}
               ans++;
           }
       }
       for(int i=0;i<s.size();i++)
       {
           if(s[i]=='-'){flag=false; break;}
       }
       cout<<"Case #"<<w+1<<":"<<" ";
       if(flag) cout<<ans; else cout<<"IMPOSSIBLE";
       cout<<endl;
    }
}
