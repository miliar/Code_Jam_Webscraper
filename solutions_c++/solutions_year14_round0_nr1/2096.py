#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <fstream>
#include <sstream>
#include <map>
#include<iomanip>
using namespace std;

#define LOOP(X,Y) for( int X = 0; X < Y; X++ )
#define LOOPP(X, Y, Z) for( int X = Y; X < Z; X++ )
#define OPENFILE(PATH) ifstream fin; fin.open(PATH)
#define PB push_back
#define ULL unsigned long long
#define LL long long

int main()
{
	OPENFILE("E:\\VSWorkSpace\\2014 code jam\\a\\A-small-attempt0.in");
	if( !fin.is_open() ) return 0;
	char * file = "E:\\VSWorkSpace\\2014 code jam\\a\\Output_small_a.out";
	ofstream fout( file, ios::out | ios::app );

	string line;
	int temp;
	ULL case_num;
	stringstream is;

	getline( fin, line );
	is<<line;
	is>>case_num;
	
	LOOP( i, case_num )
	{
		is.clear();
		int answer1 = 0, answer2 = 0;
		vector< vector<int> > v1(4);
		vector< vector<int> > v2(4);
		
		getline(fin, line);
		is<<line;
		is>>answer1;
		is.clear();

		LOOP( j, 4 )
		{
			getline(fin, line);
			istringstream is(line);
			while( is>>temp )
			{
				v1[j].PB(temp);
			}
		}

		getline(fin, line);
		is<<line;
		is>>answer2;
		is.clear();

		LOOP( j, 4 )
		{
			getline(fin, line);
			istringstream is(line);
			while( is>>temp )
			{
				v2[j].PB(temp);
			}
		}

		int tag = 0;
		int result = 0;
		answer1--;
		answer2--;
		LOOP(m,4)
		{
			LOOP( k, 4 )
			{
				if( v1[answer1][m] == v2[answer2][k] )
				{
					tag++;
					result = v1[answer1][m];
				}
			}
		}
		
		if( tag == 1 )
		{
			fout << "Case #" <<i+1<<": "<<result<<endl;
		}
		else if( tag > 1 )
		{
			fout << "Case #" <<i+1<<": Bad magician!"<<endl;
		}
		else 
		{
			fout << "Case #" <<i+1<<": Volunteer cheated!"<<endl;
		}

	}

	return 0;
}