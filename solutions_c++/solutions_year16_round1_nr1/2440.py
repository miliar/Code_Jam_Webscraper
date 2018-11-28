#include <iostream>
#include<cstring>
#include<string>
using namespace std;

int main() {
	int t,n,i,ca=0;;
	cin>>t;
	while(t--)
	{
		ca=ca+1;
	char str[10000];
	char str1[10000];
	for(i=0;i<=3500;i++)
	{
		str1[i]=NULL;
	}
	scanf("%s",str);
	n=strlen(str);
	str1[1001]=str[0];
	int p=1001;
	int q=1001;
	for(i=1;i<n;i++)
	{
		//cout<<p<<" ";
		//cout<<str1[p]<<str[i]<<" ";
		if(str1[p]<=str[i])
		{
			p=p-1;
			str1[p]=str[i];
		}
		else
		{
			//cout<<"h";
			q=q+1;
			str1[q]=str[i];
		}
	}
	printf("Case #%d: ",ca);
	for(i=0;i<3000;i++)
	{
		if(str1[i]!=' ')
		{
			cout<<str1[i];
		}
	}
	cout<<endl;
	}
	return 0;
}