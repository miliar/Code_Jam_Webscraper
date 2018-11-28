///////////////////////////// TestCase::solve is the problem specific code

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <cstdint>
using namespace std;

bool debug = false;

class TestCase
{
public:
	int s_max;
	vector<int> esses;
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
			iss >> t.s_max;
			iss >> s_str;
			for ( uint32_t j = 0; j < s_str.length(); j++ )
				t.esses.push_back( s_str[j] - '0' );
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
	int people_count = 0;
	answer = 0;
	for ( int i = 0; i < (int)(esses.size()); i++ )
	{
		int diff =  i - people_count;
		if ( diff > 0 )
		{
			people_count += diff;
			answer += diff;
		}
		people_count += esses[i];
	}
}