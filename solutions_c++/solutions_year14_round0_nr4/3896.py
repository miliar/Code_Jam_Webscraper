#include <iostream>
using namespace std;

void sort(float A[], int n)
{
	bool exchange = true;
	while(exchange)
	{
		exchange = false;
		for(int i = 0; i < n; i++)
			for(int j = 0; j<n-i-1; j++)
				if(A[j]<A[j+1])
				{
					float tmp = A[j];
					A[j] = A[j+1];
					A[j+1] = tmp;
					exchange = true;
				}
	}
}

int dwar(float *N, float *K,int sn, int sk)
{	
	if(sn < 0)
		return 0;
	
	if(K[sk] < N[sn]){
		return 1+dwar(N,K,sn-1,sk-1);
	}
	else
		return dwar(N,K,sn-1,sk);
}
	
int nwar(float N[], float K[], int n)
{
	if(n == 0)
		return 0;
	if(N[0]>K[0])
	{
		float nextN[n-1],nextK[n-1];
		for(int i = 0; i<n-1; i++)
		{
			nextN[i] = N[i+1];
			nextK[i] = K[i];
		}
		return 1+nwar(nextN, nextK, n-1);
	}
	else
	{
		int m = 0,count = 0;
		float nextN[n-1],nextK[n-1];
		for(int i = 0; i<n; i++)
			if(N[0]>K[i])
			{
				m = i-1;
				break;
			}
		for(int i = 0; i<n-1; i++)
			nextN[i] = N[i+1];
		for(int i = 0; i<n; i++)
		{
			if(i<m)
			{
				nextK[count] = K[i];
				count++;
				continue;
			}
			if(i == m)
				continue;
			nextK[count] = K[i];
			count++;
		}
		return nwar(nextN, nextK, n-1);
	}
}

int main()
{
	int ntest;
	cin>>ntest;
	for(int i = 0; i<ntest; i++)
	{
		int n;
		cin>>n;
		float N[n],K[n];
		for(int j = 0; j<n; j++)
			cin>>N[j];
		for(int j = 0; j<n; j++)
			cin>>K[j];
		sort(N,n);
		sort(K,n);
		cout<<"Case #"<<i+1<<": "<<dwar(N,K,n-1,n-1)<<" "<<nwar(N,K,n)<<endl;
	}
}
