#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int main()
{
	int t,test,i,k;
	char s[2001];
	int ans[2001];
	int hash[200];
	scanf("%d",&test);
	for(t=1;t<=test;t++)
	{
		scanf("%s",s);
		memset(hash,0,sizeof(hash));
		for(i=0;i<strlen(s);i++)
		{
			hash[s[i]]++;
		}
		k=0;
		// checking all 0s
		while(hash['Z']>0)
		{
			ans[k++]=0;
			hash['Z']--;
			hash['E']--;
			hash['R']--;
			hash['O']--;
		}
		// checking all 2s
		while(hash['W']>0)
		{
			ans[k++]=2;
			hash['W']--;
			hash['T']--;
			hash['O']--;
		}
		//4s
		while(hash['F']>0 && hash['O']>0 && hash['R']>0 && hash['U']>0)
		{
			hash['F']--;
			hash['O']--;
			hash['R']--;
			hash['U']--;
			ans[k++]=4;
		}
		//6s
		while(hash['S']>0 && hash['I']>0 && hash['X']>0 )
		{
			hash['S']--;
			hash['I']--;
			hash['X']--;
			ans[k++]=6;
		}
		//8s
		while(hash['E']>0 && hash['I']>0 && hash['G']>0 && hash['H']>0 && hash['T']>0)
		{
			hash['E']--;
			hash['I']--;
			hash['G']--;
			hash['H']--;
			hash['T']--;
			ans[k++]=8;
		}
		// 1s
		while(hash['O']>0 && hash['N']>0 && hash['E']>0)
		{
			ans[k++]=1;
			hash['O']--;
			hash['N']--;
			hash['E']--;
		}
		//3s
		while(hash['T']>0 && hash['H']>0 && hash['R']>0 && hash['E']>1)
		{
			hash['H']--;
			hash['T']--;
			hash['R']--;
			hash['E']-=2;
			ans[k++]=3;
		}
		//5s
		while(hash['F']>0 && hash['I']>0 && hash['V']>0 && hash['E']>0)
		{
			hash['F']--;
			hash['I']--;
			hash['V']--;
			hash['E']--;
			ans[k++]=5;
		}
		
		//7s
		while(hash['S']>0 && hash['E']>1 && hash['V']>0 && hash['N']>0)
		{
			hash['S']--;
			hash['V']--;
			hash['N']--;
			hash['E']-=2;
			ans[k++]=7;
		}
		//9s
		while(hash['N']>1 && hash['I']>0 && hash['E']>0 )
		{
			hash['N']-=2;
			hash['I']--;
			hash['E']--;
			ans[k++]=9;
		}
		//sort it later
		sort(ans,ans+k);
		printf("Case #%d: ",t);
		for(i=0;i<k;i++) printf("%d",ans[i]);
		printf("\n");
	}
	return 0;
}
