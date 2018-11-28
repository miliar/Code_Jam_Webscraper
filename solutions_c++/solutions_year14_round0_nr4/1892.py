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
	OPENFILE("E:\\VSWorkSpace\\2014 code jam\\QU66Q_D\\D-large.in");
	if( !fin.is_open() ) return 0;
	char * file = "E:\\VSWorkSpace\\2014 code jam\\QU66Q_D\\D-large.out";
	ofstream fout( file, ios::out | ios::app );

	string line;
	ULL case_num;
	stringstream is;

	getline( fin, line );
	is<<line;
	is>>case_num;

	LOOP( i, case_num )
	{	
		is.clear();

		LL N = 0;
		double temp;

		getline( fin, line );
		is<<line;
		is>>N;
		
		vector< vector<double> > v1(2);
		vector< vector<double> > v2(2);

		for( int m = 0; m < 2; m++ )
		{
			getline( fin, line );
			istringstream iss(line);
			while( iss >> temp )
			{
				v1[m].PB(temp);
				v2[m].PB(temp);
			}
		}

		LL result1 = 0, result2 = 0, k = 0;

		sort( v1[0].begin(), v1[0].end() );
		sort( v1[1].begin(), v1[1].end() );

		
		for( LL p = 0; p < v1[0].size(); p++ )
		{
			if( v1[0][p] > v1[1][k] )
			{
				result1++;
				k++;
			}
		}

		sort(v2[1].begin(), v2[1].end() );
		LL h = 0;
		bool flag = false;
		for( LL p = 0; p < v2[0].size(); p++ )
		{
			flag = false;
			for( LL q = 0; q < v2[1].size(); q++ )
			{
				if( v2[0][p] < v2[1][q] )
				{
					v2[1][q] = -1;
					flag = true;
					break;
				}
				else
				{
					continue;
				}
			}
			if( !flag )
			{
				for( LL r = 0; r < v2[1].size(); r++ )
				{
					if( v2[1][r] != -1 )
					{
						result2++;
						v2[1][r] = -1;
						flag = false;
						break;
					}
				}
			}
		}
			
		fout<<"Case #"<<i+1<<": "<<result1<<" "<<result2<<endl;

	}

	return 0;
}