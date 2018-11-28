#include <iostream>
#include <string>
using namespace std;

int main(void)
{
	int T;
	int t;
	int N;
	int n;
	
	cin >> T;
	
	for (t=0;t<T;t++)
	{
		cin >> N;
		int* P = new int[N];
		
		for (n=0;n<N;n++)
		{
			cin >> P[n];
		}
		
		cout << "Case #" << t+1 << ": ";
		
		int votes=1;
		while (votes>0)
		{
			votes=0;
			int max = -1;
			int index1 = 0;
			int index2 = 0;
			for (n=0;n<N;n++)
			{
				votes = votes + P[n];
				if ( P[n] > max )
				{
					max = P[n];
					index1 = n;
					index2 = n;
				}
				else if ( P[n] == max )
				{
					index2 = n;
				}
			}
			
			/*
			cout << "index1: " << index1 << ", index2: " << index2 << endl;
			for (n=0;n<N;n++)
			{
				cout << P[n] << " ";
			}
			cout << endl;
			*/
			
			if ( votes/2 > 1 || votes==2 )
			{
				char e = 'A'+index1;
				cout << e;
				e = 'A'+index2;
				cout << e;
				cout << " ";
				P[index1]--;
				P[index2]--;
			}
			else
			{
				char e = 'A'+index1;
				cout << e;
				cout << " ";
				P[index1]--;
			}
			votes = 0;
			for (n=0;n<N;n++)
			{
				votes = votes + P[n];
			}
			
		}
		
		cout << endl;
		
	}
		
	return 0;
}