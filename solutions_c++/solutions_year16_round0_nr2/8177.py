#include<iostream>
#include<string.h>
#include<algorithm>
using namespace std;
int c;
char s[1000];
int swap(int l)
{
	int i=0;
	int x=strlen(s);
	for(i=0;i<x;i++)
	{
	if(s[i]=='-')
	break;
	else
	s[i]='-';
    }
    if(i>0)
    c++;
    reverse(s,s+l+1);
    for(i=0;i<=l;i++)
    {
    if(s[i]=='+')
    s[i]='-';
    else
    s[i]='+';
    }
    c++;
    
	
	
}
int search(char s[])
{
	int x=strlen(s),i;
	for(i=x-1;i>=0;i--)
	{
	if(s[i]=='-')
	return i;
    }
	return -1;
}
int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	cin>>t;
	int q=1;
	while(t--)
	{
		c=0;
		cin>>s;
	 while(1)
	 {
	 	int z=search(s);
	 	if(z==-1)
	 	break;
	 	swap(z);
	 	
	 	
	 }
	 cout<<"Case #"<<q<<": "<<c<<"\n";
	 q++;
	 	
	}
}
