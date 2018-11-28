#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	int base = 0;
	int cases,N,J;
	long long int number[9];
	string numstr;
	string div;
	string prn;
	
	cin >> cases;
	for( int i = 0 ; i < cases ; i++ )
	{
		cin >> N >> J;
		div.resize(N/2);
		div[0] = 1;
		div[N/2-1] = 1;
		
		cout << "Case #" << cases << ":" << endl;
		for( int i = 0 ; i < J ; i++ )
		{
			base = i;
			for( int j = 1 ; j < N/2-1 ; j++ )
			{
				div[j] = base%2;
				base /= 2;
			}
			
			prn = div;
			for( int j = 0 ; j < N/2 ; j++ )
				prn[j] += '0';
				
			cout << (prn + prn);
			
			for( int q = 0 ; q < 9 ; q++ )
			{
				number[q] = 0;
				for( int k = 0 ; k < N/2 ; k++ )
				{
					number[q] *= q+2;
					number[q] += div[k];
				}
				cout << " " << number[q];
			}
			cout << endl;
		}
	}
	return 0;
}
