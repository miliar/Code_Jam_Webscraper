#include<stdio.h>
#include "stdafx.h"
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
	FILE *fr=fopen("a-large.in","r");
	FILE *fw=fopen("out.txt","w");
	int data;
	fscanf(fr,"%d",&data);
	for(int p=0;p<data;p++)
	{
		int num,siz;
		fscanf(fr,"%d%d",&num,&siz);
		vector<int>vec;
		for(int i=0;i<num;i++)
		{
			int zan;
			fscanf(fr,"%d",&zan);
			vec.push_back(zan);
		}
		sort(vec.begin(),vec.end());
		int ans=num;
		int pt=num-1;
		for(int i=0;i<num;i++)
		{
			for(;;)
			{
				if(i>=pt)
				{
					break;
				}
				if(vec[i]+vec[pt]<=siz)
				{
					ans--;
					pt--;
					break;
				}
				else
				{
					pt--;
				}
			}
		}
		fprintf(fw,"Case #%d: %d\n",p+1,ans);
	}
}