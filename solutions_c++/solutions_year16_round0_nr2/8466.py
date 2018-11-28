#include<iostream>
#include<string.h>
int main()
{
 using namespace std;
 int i,s,flag,z=1,t,c;
 char a[100];
 cin>>t;
 while(t>0)
 {
  c=0;
 cin>>a;
 s=strlen(a);
 if(a[s-1]=='+')
 {
  for(i=s-1;i>=0;i--)
  {
	if(a[i]=='+')
	 a[i]='\0';
	else
	 break;
  }
 }
 flag=0;
 s=strlen(a);
 for(i=0;i<s;i++)
 {
  if(a[i]!='+')
  {
	flag=1;
	break;
  }
 }
 if(flag==0)
 {
  cout<<"Case #"<<z++<<": "<<0<<endl;
    goto xy;
 }
  for(i=0;i<s;i++)
 {
  if(a[i]!='-')
  {
	flag=1;
	break;
  }
 }
 if(flag==0)
 {
  cout<<"Case #"<<z++<<": "<<1<<endl;
    goto xy;
 }
 for(i=0;i<s-1;i++)
 {
  if(a[i]-a[i+1]==2 || a[i]-a[i+1]==-2)
	c++;
 }

 cout<<"Case #"<<z++<<": "<<c+1<<endl;
 xy: t--;
 }
}
