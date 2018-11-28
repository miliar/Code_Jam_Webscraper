#include <stdio.h>
#include <stdlib.h>
#include "vector"
#include "algorithm"
using namespace std;

#define rep(i,n) for(i=0;i<n;++i)
#define REP(i,s,n) for(i=s;i <n;++i)

int main()
{
	int T,i,j,count, k,ind=0,N,a[100];
	std::vector<float> naomi,naomi1,ken;
	float temp, x;
	FILE* in = fopen("input.txt","r");
	FILE* out= fopen("abc.txt","w");
	fscanf(in,"%d",&T);
	rep(k,T)
	{
		naomi.clear();naomi1.clear();ken.clear();
		count = 0;
		fscanf(in,"%d",&N);
		rep(i,N)
		{
			fscanf(in,"%f",&x);
			naomi.push_back(x);
		}
		rep(i,N)
		{
			fscanf(in,"%f",&x);
			ken.push_back(x);
		}
		
		std::sort(naomi.begin(), naomi.end());
		std::sort(ken.begin(), ken.end());
		
		rep(i,N)
			naomi1.push_back( naomi.at(i) );		

		rep(i,N)
		{	
			rep(j,N)
			{
				if(ken[i]<naomi[j])
				{
					count++;
					naomi[j]=0;
					break;
				}
			}
		}
		a[ind++]=count;
		count=0;
		rep(i,N)
		{	
			rep(j,N)
			{
				if(naomi1[i]<ken[j])
				{
					count++;
					ken[j]=0;
					break;
				}
			}
		}
		a[ind++]=N-count;
		fprintf(out,"Case #%d: %d %d\n",k+1,a[ind-2],a[ind-1]);
	}
	return 0;
}

