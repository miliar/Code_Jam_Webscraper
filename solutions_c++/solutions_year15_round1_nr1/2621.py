#include<iostream>
using namespace std;
int main()
{
	int T,N;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		cin>>N;
		int M[1000];
		for(int j=0;j<N;j++)
			cin>>M[j];
		int a=0,rate=0,b=0;
		for(int j=0;j<N-1;j++)
			if(M[j]>M[j+1])
				{
					a+=M[j]-M[j+1];
					if(rate<M[j]-M[j+1])
							rate=M[j]-M[j+1];
				}
		for(int j=0;j<N-1;j++)
		{
			if(M[j]<rate) b+=M[j];
			else b+=rate;
		}
		cout<<"Case #"<<i+1<<": "<<a<<' '<<b<<endl;

	}
	return 0;
}