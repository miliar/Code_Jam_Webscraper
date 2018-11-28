#include <iostream>
using namespace std;

int main() {
	// your code goes here
	double T, A, B, K;
	cin>>T;
	int count;
	for(int i = 1; i <= T; i++)
	{
		count = 0;
		cin>>A;
		cin>>B;
		cin>>K;
		for(int j = 0; j < A; j++)
		{
			for (int k = 0; k < B; k++)
			{
				if((j&k) < K)
				{
					count++;	
				}
			}
		}
		cout<<"Case #"<<i<<": "<< count<<endl;
	}
	return 0;
}
