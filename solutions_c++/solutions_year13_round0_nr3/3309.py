#include <iostream>
#include <string>
#include <Cmath>
#include <algorithm>
#include <sstream>
#include <fstream>

using namespace std;

bool pal(int x)
{
	string P = static_cast<ostringstream*>( &(ostringstream() << x) )->str();
	double panjang = P.length();
	for (int i=0; i< (int)ceil(panjang/2); i++)
	{
		if(P[i]!=P[panjang-i-1]) 
		{
			return false;
			break;
		}
	}
	return true;
}
int main()
{
	ofstream output;
	output.open ("output3.in");
	int T;
	
	double A, B;
	cin >> T;
	
	for (int i=0; i< T; i++)
	{
		int count=0;
		cin >> A >> B;
		A = ceil(sqrt(A));
		B = floor(sqrt(B));
		
		for ( int j=A; j<=B; j++)
		{
			if(pal(j)) 
			{
				int Q = j*j;
				if (pal(Q)) 
				{
					count++;
					//cout << "angka = " << j << " " << Q << endl;
				}
			}
		}
		output << "Case #"<<i+1<<": "<<count<< endl;
	}
	output.close();
	return 0;
}