#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ofstream myfile;
    myfile.open ("OminousOmino.txt");
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		
		int R, X, C;
		cin >> X >> R >> C;
		if(!((R * C) % X) && (R >= X || C >= X) && (R >= X-1 && C >= X-1))
			myfile << "Case #" << i+1 << ": " << "Gabriel" << endl;
		else
			myfile << "Case #" << i+1 << ": " << "Richard" << endl;
	}
	return 0;
}