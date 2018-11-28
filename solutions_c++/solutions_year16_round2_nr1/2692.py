#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
string str[10]={"zero","one","two","three","four","five","six","seven","eight","nine"};
char inp[1111];
int p[10][26],ans[26],used[26],test;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A2.out","w",stdout);
	string nmb="zwuorxftse";
	int hehe[10]={0,2,4,1,3,6,5,8,7,9};
	for (int i=0;i<10;i++)
	for (int j=0;j<str[i].length();j++)
	p[i][str[i][j]-'a']++;
	cin>>test;
	for (int kk=1;kk<=test;kk++)
	{
		memset(used,0,sizeof(used));
		memset(ans,0,sizeof(ans));
		scanf("%s",inp);
		int len=strlen(inp);
		printf("Case #%d: ",kk);
		for (int i=0;i<len;i++)
		used[inp[i]-'A']++;
		for (int i=0;i<10;i++)
		{
			ans[hehe[i]]=used[nmb[i]-'a'];
			for (int j=0;j<str[hehe[i]].length();j++)
			used[str[hehe[i]][j]-'a']-=ans[hehe[i]];
		}
		for (int i=0;i<10;i++)
		for (int j=0;j<ans[i];j++)
		printf("%d",i);
		printf("\n");
	}
	return 0;
}
