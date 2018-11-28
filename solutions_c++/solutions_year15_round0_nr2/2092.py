///////////////////////////// TestCase::solve is the problem specific code

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <cstdint>
#include <algorithm>
using namespace std;

bool debug = false;

struct Plate
{
	int id;
	int pancakes;
	int sections;
	int cep; // count effective pancakes (pancakes/sections)
	Plate(int i, int p) : id(i), sections(1), pancakes(p), cep(p) {}
//	Plate(){}
	bool inc_div()
	{
		if (sections == pancakes)
			return false;

		sections++;
		cep = pancakes/(sections);
		if (cep*sections < pancakes)
			cep++;

		return true;
	}
	bool operator<(const Plate& p2)
	{
		if (cep==p2.cep)
		{
			return id < p2.id;
		}
		else
		{
			return cep > p2.cep;
		}
	}
};

class TestCase
{
public:
	int diners;
	vector<Plate> plates;

	int answer;
	void solve();
};
class DataSet
{
	vector<TestCase> test_cases;
public:
	void init()
	{
		ifstream in_file( "in.txt" );

		string line;
		istringstream iss;

		getline(in_file, line);
		iss.str(line);
		int count_cases;
		iss >> count_cases;
		string s_str;
		test_cases.resize(count_cases);
		for ( int i = 0; i < count_cases; i++ )
		{
			getline(in_file, line);
			iss.clear();
			iss.str( line );
			TestCase& t = test_cases[i];
			iss >> t.diners;
			getline(in_file, line);
			iss.clear();
			iss.str( line );
			for ( int j = 0; j < t.diners; j++ )
			{
				int pancakes;
				iss >> pancakes;
				t.plates.push_back( Plate(j,pancakes) );
			}
		}
	}
	void solve()
	{
		for ( uint32_t i = 0 ; i < test_cases.size() ; i++ )
		{
			test_cases[i].solve();
		}
	}
	void print()
	{
		ofstream out_file( "out.txt" );
		ostream& out = debug ? cout : out_file;
		for ( uint32_t i = 0; i<test_cases.size() && ( !i || &(out<<endl) ); i++ )
			out<<"Case #"<<(i+1)<<": "<<test_cases[i].answer;
	}
};

DataSet data_set;

int main()
{
	data_set.init();
	data_set.solve();
	data_set.print();
	
	if ( debug )
		cin.get();
}

////////////////// Problem related code starts here


void TestCase::solve()
{
	int best_time = 1000;
	int eating_time = 1000;
	
	int divides = 0;
	while ( true )
	{
		eating_time--;
		int max_cep = 0;

		for (uint32_t i = 0; i < plates.size(); i++)
		{
			if ( plates[i].cep > eating_time )
			{
				if ( !plates[i].inc_div() )
					goto fail;
				divides++;
			}
			if (divides >= 1000)
				goto fail;
			max_cep = max(max_cep, plates[i].cep);
		}

		eating_time = min(eating_time,max_cep);
		int this_best = max_cep+divides;
		if ( this_best < best_time )
			best_time = this_best;
	}

fail:
	answer = best_time;
}











