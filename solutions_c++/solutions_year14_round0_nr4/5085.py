#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
using namespace std;

int main()
{
	vector<float> v1,v2;
	int t,i,j,num,normal=0,dec=0;
	float num_;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{	v1.clear();
		v2.clear();
		normal=0,dec=0;
		scanf("%d",&num);
		for(j=0;j<num;j++)
		{
			scanf("%f",&num_);
			v1.push_back(num_);
		}
		for(j=0;j<num;j++)
		{
			scanf("%f",&num_);
			v2.push_back(num_);
		}
		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end());
		int ptr1,ptr2;
		int fir_tot=num;
		ptr1=num-1;
		ptr2=num-1;
		while(1)
		{
			if(v1[ptr1]>v2[ptr2])
			{
				ptr1--;
				ptr2--;
				fir_tot--;
				dec++;
			}
			else
			{
				ptr2--;
				fir_tot--;
			}
			if(fir_tot==0)
				break;
		}
		fir_tot=num;
		ptr1=num-1;
		ptr2=num-1;
		while(1)
		{
			if(v1[ptr1]<v2[ptr2])
			{
				ptr1--;
				ptr2--;
				fir_tot--;
			}
			else
			{
				ptr1--;
				normal++;
				fir_tot--;
			}
			if(fir_tot==0)
				break;
		}
		printf("Case #%d:%d %d\n",i+1,dec,normal);
		
	}
	return 0;
}