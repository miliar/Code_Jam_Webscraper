#include<stdio.h>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;
#ifdef DEBUG
void print (vector<long int>A)
{
	printf("ARR LEN = %d\n",A.size());
	for(int i= 0;i<A.size();i++)
		printf("%ld ",A[i]);
	printf("\n");
}
#endif
int func(long int val, int p, vector<long int>&ARR,map< long int, map<long int, int> >&table)
{
	if(table[val][p]!=0)return table[val][p];
	if(p==ARR.size())return 0;
	int ret;
	if(val>ARR[p])
	{
		ret = func(val+ARR[p], p+1,ARR,table);
	}
	else
	{	
		if(val<2)
			ret=1+func(val,p+1,ARR,table);
		else
			ret = min(func(val, p+1, ARR,table), func(val+(val-1), p, ARR,table))+1;
	}
	table[val][p]=ret;
	return ret;
}
int main()
{
	int T;
	scanf("%d",&T);
	for(int itr=1;itr<=T;itr++)
	{
		long int A,N;
		scanf("%ld %ld",&A,&N);
		vector<long int> ARR;
		//printf("CASE %d %ld\n",itr,A);
		for(int i=0;i<N;i++)
		{
			long int temp;
			scanf("%ld",&temp);
			ARR.push_back(temp);
		}
		sort(ARR.begin(),ARR.end());
		//print(ARR);	
		/*int ANS=0;
		long int val=A;
		int MAX = ARR.size();
		for(int i=0;i<MAX;i++)
		{	
			printf("\nD%d %d %ld %d\n",i,MAX,val,ANS);
			if(val > ARR[i])
			{
				val=val+ARR[i];
			}
			else
			{
				ANS++;
				val=val+val-1;
				MAX--;	
				i--;
			}
		}*/
		map< long int, map<long int, int> >table;
		int ANS=func(A,0,ARR,table);
		printf("Case #%d: %d\n",itr,ANS);
	
	}
	return 0;
}
