#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
using namespace std;


int main()
{
	freopen("D:\\C++ Projects\\Minesweeper\\D-large.in","r",stdin); // For reading input
    freopen("D:\\C++ Projects\\Minesweeper\\Output2.txt","w",stdout); // for writing output
	double L, T;cin>>T;
	for (L=1;L<=T;L++)
	{
	double input;
	int N ,D =0,W =0,G=0,i,j;
	vector<double> V;
	vector<double> Y;
	vector<double> Z;
	cin >> N;
	
	for (i=0;i<N;i++) 
	{
    cin >> input;
    V.push_back(input);
	}
	
	for (i=0;i<N;i++) 
	{
    cin >> input;
    Y.push_back(input);
	}

	sort(V.begin(), V.end());
	sort(Y.begin(), Y.end());
	
	Z=Y;

	for (i=0;i<N;i++)
	{
		for (j=0;j<N;j++)
		{
			if (V[i] > Y[j])
			{
				D = D + 1;
				Y[j]= 10.0;
				break;
			}
		}
	}
	for (i=0;i<N;i++)
	{
		for (j=0;j<N;j++)
		{
			if (Z[i] > V[j])
			{
				W = W + 1;
				V[j]= 10.0;
				break;
			}
		}
	}
	G = N-W;
	cout <<"Case #" <<L << ": "<< D << " " << G <<'\n' ;
	}
return 0;
}