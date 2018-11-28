#include<iostream>
#include<string.h>
using namespace std;
typedef long long int ll;
ll count[2];
void flip(char *s,ll &loc)
{ll i,temp;
 for(i=0;i<=loc;i++)
 {if(s[i]=='+')
  {count[1]--;
  count[0]++;
  s[i]='-';
  temp=i;
  }
  else
  {count[1]++;
   count[0]--;
   s[i]='+';
  }
 }
 loc=temp;
}
int main()
{ freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
 ll k,t;
 cin>>t;
 for(k=1;k<=t;k++)
 {char s[105];
 cin>>s;
 ll i,len=strlen(s),loc,ans=0; 
 count[0]=0;
 count[1]=0;
 cout<<"Case #"<<k<<": ";
 for(i=0;i<len;i++)
 {if(s[i]=='+')
  count[1]++;
  else
  {count[0]++;
   loc=i;
  }
 }
 while(count[1]<len)
 {
   flip(s,loc);
   ans++;
 }
 
 cout<<ans<<endl;
 }
return 0;
}
