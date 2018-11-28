#include <iostream>
#include <cstdio>

using namespace std;

int test, n, count;
string s;

int sum(int n1){
	int su=0;
	for(int i=0;i<n1;i++)
		su+=s[i];
	return su;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out2","w",stdout);
	int c;
	scanf("%d",&test);
	for(int i=0;i<test;i++){
		scanf("%d",&n);
		count=0;
		cin>>s;
		for(int j=0;j<=n;j++)
			s[j]=s[j]-48;
		for(int j=1;j<=n;j++){
			c=sum(j)+count;
			if(c<j){
				count+=j-c;
			}
		}
		printf("Case #%d: %d\n",i+1,count);
	}
	printf("\n");
	return 0;
}