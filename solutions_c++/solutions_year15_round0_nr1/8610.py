#include<algorithm>
#include<string.h>
#include <iostream>
using namespace std;

int main() {
	
	freopen("D:\\input.txt","r",stdin);	
FILE * fp=fopen("D:\\output.txt","w");
	int t;
	cin>>t;
	int k=1;
	while(k<=t)
	{
		int s;
		cin>>s;
		char str[1005];
		cin>>str;
		int n=strlen(str);
		int count=0;
		int tot=0;
		for(int i=0;i<n;i++)
		{
			
			if(count<i)
			count=i;
			
			count=count+str[i]-48;
			tot=tot+str[i]-48;
		}
		fprintf(fp,"Case #%d: ",k);		
		fprintf(fp,"%d\n",count-tot);	
	
		k++;
	
	}
	// your code goes here
	return 0;
}