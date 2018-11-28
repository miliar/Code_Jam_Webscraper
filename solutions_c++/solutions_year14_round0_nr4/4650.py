#include<cstdio>
#include<algorithm>
#include<deque>
using namespace std;
int N,T;
deque<double>A,B;
int W,DW;
int main()
{
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		A.clear();
		B.clear();
		scanf("%d",&N);
		double x;
		for(int j=0;j<N;j++)
		{
			scanf("%lf",&x);
			A.push_back(x);
		}
		for(int j=0;j<N;j++)
		{
			scanf("%lf",&x);
			B.push_back(x);
		}
		sort(A.begin(),A.end());
		sort(B.begin(),B.end());
		W=0;
		DW=0;
		int najw=N-1,najm=0;
		for(int j=0;j<N;j++)
		{
			if(A[j]>B[najm])
			{
				DW++;
				najm++;
			}
			else najw--;
		}
		najw=N-1;
		najm=0;
		for(int j=N-1;j>=0;j--)
		{
			if(B.back()>A.back())
			{
				A.pop_back();
				B.pop_back();
			}
			else
			{
				A.pop_back();
				B.pop_front();
				W++;
			}
		}
		printf("Case #%d: %d %d\n",i,DW,W);
	}
	return 0;
}
