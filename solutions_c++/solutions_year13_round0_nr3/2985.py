#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<cmath>

using namespace std;

long num_fair_squares(long long start, long long end) {
	long number_fair_squares = 0;
	for(; start <= end; start++) {
		bool should_continue = false;
		string str_num = to_string(start);
		int back = str_num.length() - 1;
		for(int front = 0; front < back; front++) {
			if(str_num[front] != str_num[back]) {
				should_continue = true;
				break;
			}
			back--;
		}
		if(should_continue) {
			continue;
		}
		long double root_double = sqrt(start);
		long long root = (long long) root_double;
		if(root_double - root != 0) {
			continue;
		}
		str_num = to_string(root);
		back = str_num.length() - 1;
		for(int front = 0; front < back; front++) {
			if(str_num[front] != str_num[back]) {
				should_continue = true;
				break;
			}
			back--;
		}
		if(should_continue) {
			continue;
		}
		number_fair_squares++;
	}
	return number_fair_squares;
}

int main(int argc, char* argv[]) {
	if(argc != 3) {
		cout << "Please provide the input name followed by the output name\n";
	}
	ifstream file_in(argv[1]);
	ofstream file_out(argv[2]);
	vector<long> results;
	int cases;
	file_in >> cases;
	for(int index = 0; index < cases; index++) {
		long long start, end;
		file_in >> start;
		file_in >> end;
		results.push_back(num_fair_squares(start, end));
	}
	for(int index = 0; index < cases; index++) {
		file_out << "Case #" << index + 1 << ": " << results[index] << "\n";
	}
	return 0;
}

