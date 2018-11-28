#include<iostream>
#include<string.h>
#include<ctype.h>
using namespace std;
int main()
{
int t,n,i,st,en,j,max,pos,k=1;
char s[1050],w[3000];
cin>>t;
while(t>0)
{
cout<<"Case #"<<k<<": ";
	max=0;
	pos=-1;
	st=1,en=1;
	cin>>s;
	w[1500]=s[0];
	n=strlen(s);
	for(i=1;i<n;++i)
	if(s[i]>=w[1500-st+1])
	{
	w[1500-st]=s[i];
	++st;
	}
	else
	{
	w[1500+en]=s[i];
	++en;
	}
for(j=1500-st+1;j<1500+en;++j)
		cout<<w[j];
		cout<<endl;
		--t;
		++k;
	}
	return 0;
}
