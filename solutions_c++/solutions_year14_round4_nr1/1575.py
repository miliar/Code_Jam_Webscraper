#include <fstream>
#include <iostream>
#include <vector>
#include <array>
#include <set>
#include <algorithm>

using namespace std;

int main() {
	ofstream fout("data.out");
	ifstream fin("data.in");

	int t;
	fin >> t;

	for (int caseNo = 1; caseNo <= t; caseNo++){
		int n, x;
		fin >> n >> x;

		vector<int> vec;
		for (int i = 0; i < n; i++){
			int in;
			fin >> in;
			vec.push_back(in);
		}
		sort(vec.begin(),vec.end());

		//for (int i = 0; i < n; i++)
		//	cout << vec[i] << endl;

		int discs = 0;
		//start with biggest
		while (vec.size()>0){
			int curr = vec[vec.size() - 1];
			for (int i = vec.size() - 2; i >= -1; i--){
				if (i == -1){
					discs++;
					//cout << "no match " << vec[vec.size() - 1] << endl;
					vec.erase(vec.end() - 1);
					break;
				}
				if (curr + vec[i] <= x){
					//found pair
					//cout << "pairing " << vec[vec.size() - 1] << " and " << vec[i] << endl;
					vec.erase(vec.end() - 1);
					vec.erase(vec.begin() + i);
					discs++;
					break;
				}
			}
		}
		cout << "Case #" << caseNo << ": " << discs << endl;
		fout << "Case #" << caseNo << ": " << discs << endl;
	}
	return 0;
}