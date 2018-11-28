#include<iostream>
#include<cstring>
#include<cstdlib>
#include<cstdio>
using namespace std;
char c[120];
int main()
{
	int T;
	cin>>T;
	for(int ii=1;ii<=T;++ii)
	{
		printf("Case #%d: ",ii);
		scanf("%s",c);
		bool flag=false;
		int sum=0;
		if(c[0]=='+') flag=true;
		else sum++;
		int n=strlen(c);
		for(int i=1;i<n;++i)
			if(c[i-1]=='+'&&c[i]=='-')
				sum+=2;
		printf("%d\n",sum);
	}
	return 0;
}