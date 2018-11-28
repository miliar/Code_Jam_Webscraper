#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<cmath>

using namespace std;

int main(int argc, char *argv[])
{
    if (argc!=3) 
    {
	cout << "Missing arguments." << endl;
	return -1;
    }
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);

    int T;
    fin >> T;

    for (int i = 0; i < T; ++i)
    {
		int X, R, C;
		fin >> X >> R >> C;
		bool result = true;
		int m = min(R,C);
		int M = max(R,C);
		
		if ( X > M )
			result  = false;
		if ( m * M % X != 0)
			result = false;
		
		if (X == 3)
		{
			if ( m == 1 ) result = false;
		}
		
		if (X == 4)
		{
			if ( m <= 2 && M == 4)  result = false;
		}
		
		
		
		if (result)
			fout << "Case #" << i+1 << ": GABRIEL";
		else
			fout << "Case #" << i+1 << ": RICHARD";
		fout << endl;
    }
    return 0;
}
