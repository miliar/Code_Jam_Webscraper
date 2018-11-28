#include <iostream>
#include<string.h>
#include<cstdlib>
using namespace std;

int main() {
	int a[1001],s,v,t,n,i,j,f,count;
	char str[1001];

	cin>>t;
	for(v=0;v<t;v++){
		f=0,n=0;
	cin>>s>>str;
	count=int(str[0])-'0';
	
	for(i=0;i<strlen(str);i++){
		a[i]=int(str[i])-'0';
		}
		n=i;
		for(i=1;i<n;i++){
			if(count>=i||a[i]==0)
			count=count+a[i];
			else
			{
			f=(i-count)+f;
			 count=count+f+a[i];
			 
			}
			
		}
		cout<<"Case #"<<v+1<<": "<<f<<"\n";
	
	}
	return 0;
}