#include<iostream>
using namespace std;

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("outputS.txt","w",stdout);

	int T;
	cin>>T;

	for (int i=0 ; i<T ; i++)
	{
		int A,B,K;
		cin>>A>>B>>K;
		int Count=0;

		int k,j;
		k=0;
		j=0;
		do
		{
			do
			{
				if ( (j&k) < K)
					Count++;
				k++;
			}while(k<B);
			k=0;
			j++;
		}while(j<A);
		cout<<"Case #"<<i+1<<": "<<Count<<endl;
	}
}