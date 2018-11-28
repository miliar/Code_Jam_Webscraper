#include <bits/stdc++.h>
using namespace std;
 
int main() {
    long long int t,ans,pos,count;
    cin>>t;
count=0;
    while(t--)
    {ans=0;
count++;
       char s[200];
       cin>>s;
       pos=-1;
       ans=0;
       for(int i=0;i<strlen(s);i++)
       {
           if(s[i]=='+')
           pos=i;
           if(s[i]=='-')
           {
               while(s[i]=='-' && i<strlen(s))
               {
                   i++;
               }
               i--;
               if(pos==-1)
               ans+=1;
               else
               ans+=2;
           }
       }
       cout<<"Case #"<<count<<": "<<ans<<"\n";
 
    }
	// your code goes here
	return 0;
}
 
