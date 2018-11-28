// My solution for Google jam problem Problem A. Prima donna
// https://code.google.com/codejam/contest/2442487/dashboard#s=p1
// Jerome

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
#include <utility>
#include <cmath>
using namespace std;

const char* inFileName = "D-small-attempt1.in";
const char* outFileName = "out.txt";



int main()
{
	std::ifstream infile(inFileName);
	std::ofstream outfile(outFileName);
	if( infile.fail() || outfile.fail() )
	{
		return 0;
	}
	
	string line;
	getline(infile,line);
	int T = stoi(line);
	
	for( int Case = 1; Case <= T; Case++ )
	{
		getline(infile,line);
		istringstream iss(line); 
		int X,R,C;
		iss >> X >> R >> C;
		cout<<X<<","<<R<<","<<C<<endl;
		int temp = R;
		if( R > C )
		{
			R = C;
			C = temp;
		}

		bool richardWin = false;
		if( X > R &&  X > C )
		{
			richardWin = true;
		}
		if( X > R )
		{
			// do a L with a branch of size R+1
			int rem = X - R;
			if( rem > R )
			{
				richardWin = true;
			}
		}
		if( X >= 7 )
		{
			richardWin = true;
		}
		if( (R * C) % X != 0 )
		{
			richardWin = true;
		}
		if( X == 4 )
		{
			if( R <= 2 )
				richardWin = true;
		}
		if( X == 3 )
		{
			if( R <= 1 )
				richardWin = true;
		}

		string win = richardWin ? "RICHARD" : "GABRIEL";
		cout<<"Case #"<<Case<<": "<<win<<endl;
		outfile <<"Case #"<<Case<<": "<<win<<endl;
	}

    infile.close();
	outfile.close();
	system("pause");
	return 0;
}