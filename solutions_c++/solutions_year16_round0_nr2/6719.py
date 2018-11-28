#include <iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main() {
	// your code goes here
	int t,k;
	cin>>t;
	for(k=1;k<=t;k++)
	{
	    char s[1000];
	    scanf("%s",s);
	    int l=strlen(s);
	    int a[l],count=0;
	    for(int i=0;i<l;i++)
	    {
	    if(s[i]=='-')
	    a[i]=0;
	    else if(s[i]=='+')
	    a[i]=1;
	    }
	    int n=l;
	    for(int i=0;i<n-1;i++)
	    {
	        if(a[i+1]==0 && a[i]==1)
	        { count++;  }
	        else if(a[i+1]==1 && a[i]==0)
	        { count++; }
	    }
	    if(a[l-1]==0)
	    cout<<"Case #"<<k<<": "<<count+1<<endl;
	    else
	    cout<<"Case #"<<k<<": "<<count<<endl;
	}
	return 0;
}
