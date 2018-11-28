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

int decietwar(float *N, float *K,int sn, int sk)
{	
	if(sn < 0)
		return 0;
	
	if(K[sk] < N[sn]){
		return 1+decietwar(N,K,sn-1,sk-1);
	}
	else
		return decietwar(N,K,sn-1,sk);
}
	
int nocheatwar(float *N, float *K, int en , int bn , int ek , int bk )
{
	if(en - bn == -1)
		return 0;
	if(N[bn]>K[bk])
	{
		return 1+nocheatwar(N, K, en , bn + 1, ek -1 , bk);
	}
	else
	{
		return nocheatwar(N, K, en , bn + 1 , ek , bk + 1);
	}
}

int main()
{
	int ctest;
	cin>>ctest;
	for(int i = 0; i<ctest; i++)
	{
		int n;
		cin>>n;
		float Naomi[n],Ken[n];
		for(int j = 0; j<n; j++)
			cin>>Naomi[j];
		for(int j = 0; j<n; j++)
			cin>>Ken[j];
		sort(Naomi,n);
		sort(Ken,n);
		cout<<"Case #"<<i+1<<": "<<decietwar(Naomi,Ken,n-1,n-1)<<" "<<nocheatwar(Naomi,Ken,n-1,0,n-1,0)<<endl;
	}
}
