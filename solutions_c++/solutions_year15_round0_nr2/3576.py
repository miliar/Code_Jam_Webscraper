#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int A[1010];

int main()
{
	int z;
	cin>>z;
	for(int v=0;v<z;v++)
	{
		int n;
		cin>>n;
		int maxa=0;
		for(int i=0;i<n;i++)
		{
			cin>>A[i];
			maxa=max(A[i],maxa);
		}
		int minczas=1000000;
		for(int i=1;i<=maxa;i++)
		{
			int czas=i;
			for(int j=0;j<n;j++)
			{
				if(A[j]>i)
				czas+=((A[j]-i)%i==0)?(A[j]-i)/i:(A[j]-i)/i+1;
			}
			minczas=min(czas,minczas);
		}
		cout<<"Case #"<<v+1<<": "<<minczas<<endl;
	}
}

