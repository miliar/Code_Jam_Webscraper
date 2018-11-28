#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int binary (vector<double> Ken, double target) {
	int low = 0, high = Ken.size() - 1, mid;
	while (low <= high){
		mid = low + (high - low) / 2;
		if (Ken[mid] > target) {
			high = mid - 1;
		}
		else {
			low = mid + 1;
		}
	}
	return low;
}

int war (vector<double> Naomi, vector<double> Ken) {
	int win = 0;
	while(Naomi.size() > 0) {
		if(Naomi.back() > Ken.back()) {
			Ken.erase(Ken.begin() );
			win++;
		}
		else {
			int index = binary(Ken, Naomi.back());
			Ken.erase(Ken.begin() + index );
		}
		Naomi.pop_back();
	}
	return win;
}

int dwar (vector<double> Naomi, vector<double> Ken) {
	int win = 0;
	while(Naomi.size() > 0){
		if(Naomi[0] > Ken [0]) {
			win ++;
			Naomi.erase(Naomi.begin() );
			Ken.erase(Ken.begin() );
		}
		else {
			Naomi.erase(Naomi.begin() );
			Ken.pop_back();
		}
	}
	return win;
}

int main() {
	int T; 
	ifstream fin;
	ofstream fout;
	fin.open("D-large.in");
	fout.open("D-large.out");
	fin >> T;
	for (int it = 0; it < T; it++) {
		int N;
		fin >> N;
		vector<double> Naomi, Ken;
		for (int i = 0; i < N; i++) {
			double dummy;
			fin >> dummy;
			Naomi.push_back(dummy);
		}
		for (int i = 0; i < N; i++) {
			double dummy;
			fin >> dummy;
			Ken.push_back(dummy);
		}
		sort(Naomi.begin(), Naomi.end());
		sort(Ken.begin(), Ken.end());
		fout << "Case #" << it+1 <<": ";
		fout << dwar(Naomi, Ken) << " " << war(Naomi, Ken) <<endl;
	}
}