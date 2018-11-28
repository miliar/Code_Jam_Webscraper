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
	OPENFILE("E:\\VSWorkSpace\\2014 code jam\\QU66Q_B\\B-large.in");
	if( !fin.is_open() ) return 0;
	char * file = "E:\\VSWorkSpace\\2014 code jam\\QU66Q_B\\B-large.out";
	ofstream fout( file, ios::out | ios::app );

	string line;
	string temp;
	ULL case_num;
	stringstream is;

	getline( fin, line );
	is<<line;
	is>>case_num;
	is.clear();

	LOOP( i, case_num )
	{
		double C = 0.0;
		double F = 0.0;
		double X = 0.0;
		double S = 2.0;

		getline( fin, line );
		istringstream iss(line);

		iss>>C;
		iss>>F;
		iss>>X;

		double current = 0.0;
		double nest_time = 0.0;
		double time = 0.0;
		while(1)
		{
			current = X / S;
			nest_time = (X / (S + F)) + (C / S);
			if( current < nest_time )
			{
				time += current;
				break;
			}
			time += C / S;
			S += F;
		}

		fout<<"Case #"<<i+1<<": ";
		fout<<setiosflags(ios::fixed)<<setprecision(8)<<time<<endl;
	}

	return 0;
}