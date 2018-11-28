#include <iostream>
#include <sstream>
#include <iterator>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <string>

using namespace std; 

class testcase{
public:
	void parse_testcase();

	string solve() const;
	
private:
	vector<vector<int> >      _data;
	int                       _rows;
	int                       _cols;
};

class lawnmower {
public:
	void parse_testcase();

	void solve() const; 

private:
	vector<testcase> _tests;
};

void testcase::parse_testcase(){
	string line;
	getline(cin, line);
	istringstream is(line);
	is >> _rows >> _cols;

	for(int i = 0; i < _rows; ++i){
		vector<int> col_data;
		getline(cin, line);
		istringstream is(line);
		copy(istream_iterator<int>(is), istream_iterator<int>(), back_insert_iterator<vector<int> >(col_data));
		_data.push_back(col_data);
	}
	return;
}

string testcase::solve() const{
	vector<int> max_rows(_rows,-1);
	vector<int> max_cols(_cols,-1);

	for(int rindex = 0; rindex < _rows; ++rindex){
		for(int cindex = 0; cindex < _cols; ++cindex){
			max_rows[rindex] = max(max_rows[rindex], _data[rindex][cindex]);
			max_cols[cindex] = max(max_cols[cindex], _data[rindex][cindex]);
		}
	}

	for(int cindex = 0; cindex < _cols; ++cindex){
		for(int rindex = 0; rindex < _rows; ++rindex){
			if(_data[rindex][cindex] < max_rows[rindex] && _data[rindex][cindex] < max_cols[cindex])
				return "NO";
		}
	}
	return "YES";
}

void lawnmower::parse_testcase(){
	string line;
	int count;
	cin >> count;
	getline(cin,line);

	for(int i = 0; i < count; ++i){
		testcase t;
		t.parse_testcase();
		_tests.push_back(t);
	}

	return;
}

void lawnmower::solve() const {
	for(size_t i = 0; i < _tests.size(); ++i){
		cout << "Case #" << i + 1 << ": " << _tests[i].solve() << endl;
	}
}

int main(int argc, char* argv[])
{
	lawnmower lm;
	lm.parse_testcase();
	lm.solve();

	return 0;
}