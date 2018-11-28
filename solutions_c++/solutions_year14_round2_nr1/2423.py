#include<cstdio>
#include<cstring>

using namespace std;

void test(int);

int main()
{
	int t,i=1;
	scanf("%d",&t);
	while(t--)
	{
		test(i);
		i++;
	}
	return 0;
}

void test(int c)
{
	int n,len1,len2,i,j,ctr1=0,ctr2=0,ans=0;
	int a1[26]={0},a2[26]={0};
	char s1[102]={'\0'}, s2[102]={'\0'};
	scanf("%d",&n);
	scanf("%s",s1);
	scanf("%s",s2);
	if(strcmp(s1,s2)==0)
	{
		printf("Case #%d: 0\n",c);
		return;
	}
	len1=strlen(s1);
	len2=strlen(s2);
	for(i=0 ; i<len1 ; i++)
		a1[s1[i]-97]++;
	for(i=0 ; i<len2 ; i++)
		a2[s2[i]-97]++;
	for(i=0 ; i<26 ; i++)
	{
		if((a1[i]==0 && a2[i]!=0) || (a2[i]==0 && a1[i]!=0))
		{
			printf("Case #%d: Fegla Won\n",c);
			return;
		}
	}
	i=0;
	j=0;
	while(true)
	{
		if((s1[i]!=s2[j]))
		{
			printf("Case #%d: Fegla Won\n",c);
			return;
		}
		while(true)
		{
			ctr1++;
			i++;
			if(s1[i] != s1[i-1])
				break;
		}
		while(true)
		{
			ctr2++;
			j++;
			if(s2[j] != s2[j-1])
				break;
		}
		if(ctr1>ctr2)
			ans+=ctr1-ctr2;
		else
			ans+=ctr2-ctr1;
		ctr1=ctr2=0;
		if(i==len1 && j==len2)
			break;
	}
	printf("Case #%d: %d\n",c,ans);
}