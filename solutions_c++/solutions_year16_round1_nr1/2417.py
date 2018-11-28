#include<iostream>
#include<string.h>
using namespace std;
int main()
{ long int t,j;
cin>>t;
for(j=1;j<=t;j++)
{ string s; char a[1005]={"/0"}; long int i;
 cin>>s; int len=1;
 a[0]=s[0];
 for(i=1;i<s.length();i++)
  {  if(s[i]>=a[0])
      { memmove(a+len,a,strlen(a));
        a[0]=s[i];
	  }
      else
      a[i]=s[i];
  }
    cout<<"Case #"<<j<<": ";
     for(i=0;i<s.length();i++)
     cout<<a[i];
     cout<<endl;
}
}