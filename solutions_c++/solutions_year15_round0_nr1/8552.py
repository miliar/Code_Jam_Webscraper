#include<iostream>
#include<stdio.h>
#include<vector>

using namespace std;

int main()
{
	int t;
	FILE *f1=fopen("A-large.in","r");
	FILE *f2=fopen("A-large.out","w");
	fscanf(f1,"%d",&t);
	int s,k=0,q=0,w=1;
	char c[1002];
	while(t>0)
	{
		fscanf(f1,"%d%s",&s,&c[0]);
		k=0;
		q=0;
		for(int i=0;i<=s;i++)
		{
			if(c[i]>0 &&k<i)
			{
				q+=(i-k);
				k+=(i-k);
			}
			k+=(c[i]-'0');
		}
		fprintf(f2,"Case #%d: %d\n",w,q);
		t--;
		w++;
	}
	return 0;
}
