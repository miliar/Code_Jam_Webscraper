#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

bool all(const vector <bool>& nums);
int get_flips(string ncase);
void gen_list(vector <bool>& list, string ncase);
void flip_to (vector <bool>& nums, int n);

int main() {
	ifstream in("B-small-attempt0.in");
	ofstream out;
	vector <int> nums;
	
	int num_cases;
	in >> num_cases;
	nums.reserve(num_cases);
	while ( num_cases > 0){
		string ncase;
		in >> ncase;
		nums.push_back(get_flips(ncase));
		num_cases--;
	}
	out.open("B-small-attempt0-out.txt");
	for(int i = 0; i < nums.size(); ++i){
		out << "Case #" << i+1 << ": " << nums[i] << endl;
	}
	
	return 0;
}

int get_flips(string ncase) {
	vector <bool> list;
	list.resize(ncase.length());
	gen_list(list, ncase);
	int steps = 0;
	for (int i = ncase.length() - 1;!all(list); --i){
		if (i < 0)
			i = ncase.length() - 1;
		if(!list[i]) {
			flip_to(list, i);
			++steps;
		}
	}
	return steps;
}

void gen_list(vector <bool>& list, string ncase) {
	for (int i = 0; i < ncase.length(); ++i) {
		if (ncase[i] == '+')
			list[i] = true;
		else
			list[i] = false;
	}
}

void flip_to (vector <bool>& nums, int n) {
	while (n >= 0) {
		nums[n] = !nums[n];
		n--;
	}
}

bool all(const vector <bool>& nums) {
	bool done = true;
	for (int i = 0; done && i < nums.size(); i++)
		done = nums[i];
	return done;
}