#include <iostream>
#include <cstdlib>
using namespace std;
int compare (const void * a, const void * b)
{
  return ( *(int*)b - *(int*)a );
}
int main()
{
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		int n;
		cin>>n;
		float *A=new float[n];
		float *B=new float[n];
		float *B1=new float[n];
		int win1=0;
		int win2=0;
		for(int j=0;j<n;j++)
		{
			cin>>A[j];
		}
		
		for(int j=0;j<n;j++)
		{
			cin>>B[j];
			B1[j]=B[j];
		}
		
		qsort (A, n, sizeof(int), compare);
		qsort (B, n, sizeof(int), compare);
		qsort (B1, n, sizeof(int), compare);
		int ind1=0;
		int ind2=0;
		for(int j=0;j<n;j++)
		{
			if(A[ind1++]>B[ind2++])
			{
				win1++;
				//cout<<A[j]<<" "<<B[j]<<endl;
				ind2--;
			}
		}
		ind1=0;
		ind2=0;
		for(int j=0;j<n;j++)
		{
			if(A[ind1++]>B1[ind2++])
			{
				win2++;
				
			}
			else
			{
				ind1--;
			}
		}

		cout<<"Case #"<<i+1<<": "<<win2<<" "<<win1<<endl;
	}
}