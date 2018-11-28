#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);i++)

int count_inversions(int* a, int n)
{
	int res=0;
	REP(i,n) REP(j,i)
		if(a[i]<a[j])
			res++;
	return res;
}

int update_inversions(int *a , int n, int i, int maxv)
{
	int diff=0;
	REP(j,n)
		if((i<j) != (a[i]<a[j]))
			diff--;
	a[i]=2*maxv-a[i];
	REP(j,n)
		if((i<j) != (a[i]<a[j]))
			diff++;
	a[i]=2*maxv-a[i];
	return diff;
}

int a[1000];

int main()
{
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		int n;
		scanf("%d",&n);
//		n=1000;
		REP(i,n)
//			a[i]=i+1;
//		random_shuffle(a,a+n);
			scanf("%d",&a[i]);

		int maxv=*max_element(a,a+n);
		int used[1000]={};
		bool should_invert[1000]={};
		bool over_max=0;
		REP(i,n)
		{
//			if(a[i]==maxv)
//				over_max=true;
//			if(over_max)
//				a[i]=2*maxv-a[i];
			if(update_inversions(a,n,i,maxv)<0)
				a[i]=2*maxv-a[i];
//			should_invert[i]=res>count_inversions(a,n);
//			a[i]=2*maxv-a[i];
		}
		int res=count_inversions(a,n);
		while(1)
		{
			int best_go=-1;
			int best=res;
			REP(i,n)
			{
				int cur_res=res+update_inversions(a,n,i,maxv);
				if(cur_res<best)
				{
					best=cur_res;
					best_go=i;
				}
			}
			if(best_go==-1) break;
			a[best_go]=2*maxv-a[best_go];
			assert(!used[best_go]);
			used[best_go]=1;
			res=best;
		}
//		REP(i,n)
//			assert(used[i]==should_invert[i]);
		res=count_inversions(a,n);
		printf("Case #%d: %d\n",test,res);
	}
	return 0;
}
