#include<iostream>
#include<cstring>
#include<string>
#include<cstdio>
#include<fstream>

using namespace std;

int main()
{
fstream cin("B-large.in",ios::in);
fstream cout("B-large.out",ios::out);
int t;
cin>>t;int q=1;
while(t--)
{  
int D;
int  P[1001];
cin>>D;
int max=0;
for (int i=1;i<=D;i++)
 {
   cin>>P[i];
   if (max<P[i]) max=P[i];
 }
  int ans=max;
 for (int i=1;i<=max;i++)
  {
  	int cnt=0;
  	for (int j=1;j<=D;j++)
  	  {
  	  	int p=P[j];
  	  	if (p>i)
  	  	 {  
  	  	 	cnt+=(p-i+i-1)/i;
  	  	 }
  	  }
  	  if (ans>(i+cnt)) ans=i+cnt;
  }
  cout<<"Case #"<<q++<<": "<<ans<<endl;
}
return 0;	
}
