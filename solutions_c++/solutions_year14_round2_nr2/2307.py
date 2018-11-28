#include <iostream>
using namespace std;

int main(){
	int nT, A, B, K;
	cin >> nT;
	for( int t=1; t <= nT; ++t )
	{
		int cnt = 0;
		cin >> A >> B >> K;

		for( int a=0; a < A; ++a ){
			for( int b=0; b < B; ++b ){
				int gen = a & b;
				if( gen < K ){
					cnt++;
				}
			}
		}

		cout<<"Case #"<< t <<": "<< cnt <<endl;
	}
	return 0;
}
