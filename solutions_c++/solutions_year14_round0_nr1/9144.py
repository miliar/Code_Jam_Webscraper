#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <string>
#include <cstdlib>
#include <numeric>

using namespace std;


string magic_outcome(int first[], int second[], int size){
	vector<int> v(2*size);
	vector<int>::iterator it;

	sort(first,first+size);
	sort(second,second+size);

	it = set_intersection(first,first+size,second,second+size,v.begin());
	v.resize(it-v.begin());

	if(v.empty())
		return "Volunteer cheated!";
	else if(v.size() > 1)
		return "Bad magician!";
	else {
		ostringstream out; out << v[0];
		return out.str();
	}
}

int main(){
	std::ios::sync_with_stdio(false);
	string temp;

	int num_tests = 0;
	int row_f = 0, row_s = 0;

	int first[4] = { 0 };
	int second[4] = { 0 };

	int i = 0;

	getline(cin,temp);
	num_tests = atoi(temp.c_str());

	string lines[10];
	ostringstream out;
	for(int test = 1; test <=  num_tests; ++test){

		getline(cin,lines[0]);
		getline(cin,lines[1]);
		getline(cin,lines[2]);
		getline(cin,lines[3]);
		getline(cin,lines[4]);
		getline(cin,lines[5]);
		getline(cin,lines[6]);
		getline(cin,lines[7]);
		getline(cin,lines[8]);
		getline(cin,lines[9]);

		row_f = atoi(lines[0].c_str()), row_s = atoi(lines[5].c_str());

		istringstream first_in(lines[row_f]), second_in(lines[5+row_s]);

		first_in >> first[0] >> first[1] >> first[2] >> first[3];
		second_in >> second[0] >> second[1] >> second[2] >> second[3];

		out << "Case #" << test << ": " << magic_outcome(first,second,4) << '\n';

	}
	cout << out.str();
	
	return 0;
} 