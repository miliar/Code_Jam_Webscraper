#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,smax;
	char shy[1002];
	FILE *fpr=fopen("input.txt","r");
	FILE *fpw=fopen("output.txt","w");
	fscanf(fpr,"%d",&t);
	for(int i=1;t-->0;i++)
	{
		fscanf(fpr,"%d %s",&smax,shy);
		int people=0,temp;
		people=shy[0]-48;
		int ans=0;
		for(int j=1;shy[j]!='\0';j++)
		{
			if(people<j)
			{
				temp=j-people;
				people+=temp;
				ans+=temp;
			}
			people+=shy[j]-48;
		}
		fprintf(fpw,"Case #%d: %d\n",i,ans);
	}
	return 0;
}
