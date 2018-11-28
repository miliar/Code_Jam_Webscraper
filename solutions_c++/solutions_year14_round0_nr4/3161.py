#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;
vector<double> Naomi;
vector<double> Ken;
vector<double> Naomi1;
vector<double> Ken1;
vector<double>::iterator it;
void init();
int main()
{
	int t,N,i,k;
	int pointsNaomiWins;
	double temp;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	
	{
		pointsNaomiWins=0;
		
		scanf("%d",&N);
	
		init();
		for(i=1;i<=N;i++)
		{
			scanf("%lf",&temp);
			Naomi.push_back(temp);
		}
		for(i=1;i<=N;i++)
		{
			scanf("%lf",&temp);
			Ken.push_back(temp);
		}
		
		sort(Naomi.begin()+1,Naomi.begin()+N+1);
		sort(Ken.begin()+1,Ken.begin()+N+1);
		//sorting done
		Naomi1=Naomi;
		Ken1=Ken;
		int cnt=0;
		while(Naomi.size()>1)
		{
			N=Naomi.size()-1;
			//check which player has the largest number with it
			if(Naomi[N]<Ken[N])
			{
				Naomi.erase(Naomi.begin()+1);
				Ken.erase(Ken.begin()+N);
			}
			else
			{
				//last limit is probably exclusive
				it=upper_bound(Naomi.begin()+1,Naomi.begin()+N+1,Ken[1]);
				//finding the element which is just greater than the Ken's smallest element(THAT MEAN'S UPPER BOUN
		        
	            Naomi.erase(it);
	            Ken.erase(Ken.begin()+1);
	            pointsNaomiWins+=1;
			}
			cnt++;
			
		}
		//WAR BEGINS
		printf("Case #%d: %d ",k,pointsNaomiWins);
		pointsNaomiWins=0;
		Naomi=Naomi1;
		Ken=Ken1;
		while(Naomi.size()>1)
		{
			N=Naomi.size()-1;
			it=upper_bound(Ken.begin()+1,Ken.begin()+N+1,Naomi[1]);
			
			if(it!=Ken.end())
			{
			
				Naomi.erase(Naomi.begin()+1);
				Ken.erase(it);
			}
			else
			{
				Naomi.erase(Naomi.begin()+1);
				Ken.erase(Ken.begin()+1);
				pointsNaomiWins+=1;
				
			}
		}
		printf("%d\n",pointsNaomiWins);
	}
	return 0;
}
void init()
{
	Naomi.clear();
	Ken.clear();
	Naomi.push_back(0);
	Ken.push_back(0);
}
