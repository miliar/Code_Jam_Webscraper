#include<stdio.h>
#include<set>
#include<iostream>
using namespace std;
int main()
{
	int T,N;
	scanf("%d",&T);
	float Na[1000],Ke[1000];
	for(int i=1;i<=T;i++)
	{
		scanf("%d",&N);
		set<float> Naomi,Ken;
		float val;
		for(int j=0;j<N;j++)
		{
			scanf("%f",&val);
			Naomi.insert(val);
			Na[j] = val;
		}
		for(int j=0;j<N;j++)
		{
			scanf("%f",&val);
			Ken.insert(val);
			Ke[j] = val;
		}


		int NC=0,KC=0;
		set<float>::iterator itr,itr1,itr2;
//		set<float>::reverse_iterator itr2;
		for(itr=Naomi.begin();itr!=Naomi.end();itr++)
		{
			itr1= Ken.lower_bound(*itr);
			if(itr1==Ken.end())
			{
				NC += Ken.size();
				Ken.clear();
				break;
			}
			else
			{
			//	printf("%lf %lf\n",*itr,*itr1);
				Ken.erase(itr1);
			}
		}
//		printf("Ken size %d Naomi size%d\n",Ken.size(),Naomi.size());
		
		for(int j=0;j<N;j++)
		{
			Ken.insert(Ke[j]);
		}
		
		for(itr=Naomi.begin();itr!=Naomi.end();itr++)
		{
			itr1= Ken.lower_bound(*itr);
			itr2= Ken.upper_bound(*itr);
			itr2--;
			if(itr1==Ken.begin())
			{
				itr1 = Ken.end();
				--itr1;
//				printf("%lf %lf\n",*itr,*itr1);
				Ken.erase(itr1);
			}
			else if(itr2 != Ken.end())
			{
//				printf("%lf %lf\n",*itr,*itr2);
				Ken.erase(itr2);
				KC++;
			}
		}
//		printf("Ken size %d Naomi size%d\n",Ken.size(),Naomi.size());
		printf("Case #%d: %d %d\n",i,KC,NC);
		

	}
}
