///////////////////////////// TestCase::solve is the problem specific code

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <cstdint>
#include <algorithm>
#include <map>
using namespace std;

bool debug = false;

enum Value : char
{
	NONE = 0,
	p1 = 1,
	n1 = 2,
	pi = 3,
	ni = 4,
	pj = 5,
	nj = 6,
	pk = 7,
	nk = 8,
};

class TestCase
{
public:
	vector<Value> values;

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
			int str_len;
			int multiples;
			iss >> str_len;
			iss >> multiples;
			getline(in_file, line);
			iss.clear();
			iss.str( line );
			vector<char> temp;
			for (uint32_t i = 0; i < line.length(); i++)
			{
				if (line[i] == 'i') temp.push_back(pi);
				if (line[i] == 'j') temp.push_back(pj);
				if (line[i] == 'k') temp.push_back(pk);
			}
			for (int i = 0; i < multiples; i++)
				for (uint32_t j = 0; j < temp.size(); j++)
					t.values.push_back( Value(temp[j]) );
		}
	}
	void solve()
	{
		for ( uint32_t i = 0 ; i < test_cases.size() ; i++ )
		{
			cout<<i<<endl;
			test_cases[i].solve();
		}
	}
	void print()
	{
		ofstream out_file( "out.txt" );
		ostream& out = debug ? cout : out_file;
		for ( uint32_t i = 0; i<test_cases.size() && ( !i || &(out<<endl) ); i++ )
			out<<"Case #"<<(i+1)<<": "<<(test_cases[i].answer ? "YES" : "NO");
//			out<<"Case #"<<(i+1)<<": "<<test_cases[i].answer;
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

map<pair<Value,Value>,Value> lookup = {
		{{NONE,pi},pi},{{NONE,ni},ni},{{NONE,pj},pj},{{NONE,nj},nj},{{NONE,pk},pk},{{NONE,nk},nk},
		{{p1,pi},pi},{{p1,ni},ni},{{p1,pj},pj},{{p1,nj},nj},{{p1,pk},pk},{{p1,nk},nk},
		{{n1,pi},ni},{{n1,ni},pi},{{n1,pj},nj},{{n1,nj},pj},{{n1,pk},nk},{{n1,nk},pk},
		{{pi,pi},n1},{{pi,ni},p1},{{pi,pj},pk},{{pi,nj},nk},{{pi,pk},nj},{{pi,nk},pj},
		{{ni,pi},p1},{{ni,ni},n1},{{ni,pj},nk},{{ni,nj},pk},{{ni,pk},pj},{{ni,nk},nj},
		{{pj,pi},nk},{{pj,ni},pk},{{pj,pj},n1},{{pj,nj},p1},{{pj,pk},pi},{{pj,nk},ni},
		{{nj,pi},pk},{{nj,ni},nk},{{nj,pj},p1},{{nj,nj},n1},{{nj,pk},ni},{{nj,nk},pi},
		{{pk,pi},pj},{{pk,ni},nj},{{pk,pj},ni},{{pk,nj},pi},{{pk,pk},n1},{{pk,nk},p1},
		{{nk,pi},nj},{{nk,ni},pj},{{nk,pj},pi},{{nk,nj},ni},{{nk,pk},p1},{{nk,nk},n1},
	};

class StateMachine
{
public:
	Value value;
	void parse(Value in_value)
	{
		value = lookup[pair<Value,Value>{value,in_value}];
	}

};

void TestCase::solve()
{
	StateMachine sm;
	sm.value = NONE;
	int progress = 0;
	for ( uint32_t i = 0; i < values.size(); i++ )
	{
		// Let's assume the first time the symbol appears is the best time to take it because it's 2:40am :)
		if ( sm.value == pi && progress == 0 ) { progress++; sm.value = NONE;}
		if ( sm.value == pj && progress == 1 ) { progress++; sm.value = NONE;}
		sm.parse(values[i]);
	}
	answer = (sm.value == pk && progress == 2) ? 1 : 0;
}











