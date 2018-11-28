#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif
#include<stdio.h>
#include<vector>
using namespace std;
int compare (const void * a, const void * b)
{
  if (*(double*)a > *(double*)b) return 1;
  else if (*(double*)a < *(double*)b) return -1;
  else return 0;
}
void main()
{
	//freopen("D-small-attempt0.in","r",stdin);
	//freopen("D-small-attempt0.out","w",stdout);
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++)
	{
		int n,y=0,z=0;
		double temp;
		vector<double> A,B;
		vector<int> S1,S2;
		scanf("%d",&n);
		for(int i=0;i<n;++i)
		{
			scanf("%lf",&temp);
			A.push_back(temp);
		}
		for(int i=0;i<n;++i)
		{
			scanf("%lf",&temp);
			B.push_back(temp);
		}
		std::qsort(&A[0], A.size(), sizeof(double), compare);
		std::qsort(&B[0], B.size(), sizeof(double), compare);
		for(int i=0,j=0;i<n||j<n;)
		{
			if(i==n)
			{
				S1.push_back(0);
				S2.push_back(0);
				j++;
			}
			else if(j==n)
			{
				S1.push_back(1);
				S2.push_back(1);
				i++;
			}
			else if(A[i]<B[j])
			{
				S1.push_back(1);
				S2.push_back(1);
				i++;
			}
			else
			{
				S1.push_back(0);
				S2.push_back(0);
				j++;
			}
		}
		for(;S1.size()>=2;)
		{
			int cnt=0;
			for(int i=0;i != S1.size() && i != S1.size()-1; ++i)
			{
				if(S1[i]==0&&S1[i+1]==1){ S1.erase(S1.begin()+i+1); S1.erase(S1.begin()+i); cnt++; i--;}
			}
			if(cnt==0) break;
			y+=cnt;
		}
		for(;S2.size()>=2;)
		{
			int cnt=0;
			for(int i=0;i != S2.size() && i != S2.size()-1; ++i)
			{
				if(S2[i]==1&&S2[i+1]==0){ S2.erase(S2.begin()+i+1); S2.erase(S2.begin()+i); cnt++; i--;}
			}
			if(cnt==0) break;
		}
		z=S2.size()/2;
		printf("Case #%d: %d %d\n",t+1,y,z);
	}
}