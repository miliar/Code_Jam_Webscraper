#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <fstream>

using namespace std;

int main()
{
	int t;
	ifstream fin("A-small-attempt1.in");
	fin >> t;
	
	ofstream fout("A-small-attempt1.out");
	for (int test = 1; test <= t; test++) {
		int ans_1;
		fin >> ans_1;
		int cur;
		set<int> first;
		for (int i=0; i < 4; i++) {			
			for (int j = 0; j < 4; j++) {
				fin >> cur;
				if (i == ans_1 - 1) {
					first.insert(cur);
				}
			}
		}
		int ans_2;
		fin >> ans_2;
		set<int> second;
		for (int i=0; i < 4; i++) {			
			for (int j = 0; j < 4; j++) {
				fin >> cur;
				if (i == ans_2 - 1) {
					second.insert(cur);
				}
			}
		}
		vector<int> v;
		v.resize(5);
		vector<int>::iterator it;
		it = set_intersection(first.begin(), first.end(), second.begin(), second.end(), v.begin());
		v.resize(it-v.begin()); 

		if (v.size() == 0) {
			fout << "Case #" <<test <<": Volunteer cheated!" <<endl;
		} else if (v.size() == 1) {
			fout << "Case #" <<test <<": " << v[0] <<endl;
		} else {
			fout << "Case #" <<test <<": Bad magician!"<<endl;
		}
		
	}
	fout.close();
	return 0;
}
