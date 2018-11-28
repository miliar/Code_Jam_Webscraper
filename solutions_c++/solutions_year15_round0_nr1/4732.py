// Jai sai ram
// Google Code Jam 2015
// Prob A
#include<stdio.h>
#include<algorithm>
#include<algorithm>
#include<string>
#include<iostream>
using namespace std;
#define ll long long
#define inp(a) fscanf(fp1,"%lld",&a);
#define outp(a) fprintf(fp2,"%lld\n",a);
int main()
{
	FILE *fp1,*fp2;
	fp1=fopen("INPUT1.in","r");
	if(!fp1)
		return 0;
	fp2=fopen("OUTPUT1.txt","w");
	if(!fp2)
		return 0;
	ll tc;
	inp(tc);
	//scanf("%d",&tc);
	int t=0;
	while(tc--)
	{
		t++;
		ll maxi;
		inp(maxi);
	//	scanf("%lld",&maxi);
		char st[10001];
		fscanf(fp1,"%s",st);
		int count=st[0]-'0';
		ll ans=0;
		for(int i=1;i<=maxi;i++)
		{
			if(count>=i)
				count+=(st[i]-'0');
			else if((st[i]-'0'))
			{
				ans+=(i-count);
				count+=(i-count)+(st[i]-'0');
			}
		}
		//printf("Case #%d: %lld\n",t,ans);
		fprintf(fp2,"Case #%d: %lld\n",t,ans);
	}
	return 0;
}
