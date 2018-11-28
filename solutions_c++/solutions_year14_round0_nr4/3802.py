
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int t,i,count,count1;
	int k=1;
	double temp;
	vector<double> A;
	vector<double> B;
	int n;
	scanf("%d",&t);
	while(t--)
	{
		count=0;
		count1=0;
		scanf("%d",&n);
		A.clear();
		B.clear();
		for(i=0;i<n;i++)
		{
			scanf("%lf",&temp);
			A.push_back(temp);
		}
		for(i=0;i<n;i++)
		{
			scanf("%lf",&temp);
			B.push_back(temp);
		}

		vector<double> A1(A);
		vector<double> B1(B);
		sort(A1.begin(),A1.end());
		sort(B1.begin(),B1.end());
		while(1)
		{
			if(A1.size()==0||B1.size()==0)
			{
				break;
			}
			if(A1[A1.size()-1]>B1[B1.size()-1])
			{
				A1.erase(A1.begin()+A1.size()-1);
				B1.erase(B1.begin());
				count1++;
			}
			else if(A1[A1.size()-1]<B1[0])
			{
				break;
			}
			else
			{
				for(i=B1.size()-1;i>=0;i--)
				{
					if(B1[i]<A1[A1.size()-1])
					{
						break;
					}
				}
				A1.erase(A1.begin()+A1.size()-1);
				B1.erase(B1.begin()+i+1);
			}
		}

		while(1)
		{
			if(A.size()==0||B.size()==0)
			{
				break;
			}
			double min=1.0;
			int index=-1;
			int flag=1;
			for(i=0;i<B.size();i++)
			{
				if(B[i]<min)
				{
					min=B[i];
					index=i;
				}
			}
			for(i=0;i<A.size();i++)
			{
				if(min<A[i])
				{
					flag=0;
					break;
				}
			}
			//printf("%d\n",flag);
			if(flag)
			{
				break;
			}

			int index2=-1;
			double diff=1.0;
			for(i=0;i<A.size();i++)
			{
				if(A[i]>min&&(A[i]-min<diff))
				{
					diff=A[i]-min;
					index2=i;
				}
			}
			A.erase(A.begin()+index2);
			B.erase(B.begin()+index);
			count++;
		}
		printf("Case #%d: %d %d\n",k,count,count1);
		k++;
	}
	return 0;
}