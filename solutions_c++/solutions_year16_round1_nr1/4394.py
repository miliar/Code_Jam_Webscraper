#include <iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main() {
	// your code goes here
	int t,l,i,j,k;
	
	cin>>t;
	for(k=1;k<=t;k++)
	{
	    char s[1000];
	    char a[1000];
	    char temp;
    	scanf("%s",s);
    	l=strlen(s);
    	a[0]=s[0];
    	temp=a[0];
        for(i=0;i<l;i++)
    	{
    	if(s[i+1]<temp)
    	a[i+1]=s[i+1];
    	else
    	{for(j=i+1;j>0;j--)
    	a[j]=a[j-1];
    	a[j]=s[i+1];
    	temp=a[0];
    	}
    	}
    	a[l]='\0';
    	cout<<"Case #"<<k<<": "<<a<<endl;
    	}
    	
	return 0;
}