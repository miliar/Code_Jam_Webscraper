#include <iostream>
#include<string.h>
using namespace std;
 
int main() {
 int t,i,j,k=0,m;
 cin>>t;
 for(i=1;i<t+1;i++)
	{   k=0,m=0;
		char a[101];
		cin>>a;
		if(a[0]=='-')
		   k=k+1;
		 for(j=strlen(a)-1;j>=0;j--)
		 {if(a[j]=='-'&&a[j-1]=='+')
		    k+=2;
		 }
		cout<<"Case #"<<i<<": "<<k<<endl;
	}
	return 0;
}

