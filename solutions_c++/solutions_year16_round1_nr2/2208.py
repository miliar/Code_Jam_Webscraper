#include <iostream>
#include <utility>
#include <cmath>
#include <vector>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <time.h>
#include <algorithm>
#include <string>

using namespace std;

int64_t cmp (int64_t a, int64_t b) {
	return a<b;
}

int64_t loop() {
}

int main() {
	int64_t T;
	int64_t N;
	int64_t count = 0;
	
	int64_t culprit = 0;
	int64_t culprit_loc = 0;
	
	vector<int64_t> in_vec;
	vector<int64_t> dupe_vec;
	vector<int64_t> out_vec;
	
	cin >> T;
	
	for(int64_t iii = 0; iii < T; iii++) {
		in_vec.clear();
		out_vec.clear();
		cin >> N;
		//in_vec.resize(2*N*N - 1);
		//in_vec.resize(2*N - 1);
		//Now we insert
		
		for(int i = 0; i < 2*N-1; i++) {
			int64_t put = 0;
			for(int j = 0; j < N; ++j) {
			cin >> put;
			in_vec.push_back(put);}
		}
		
		sort(in_vec.begin(), in_vec.end());
		
		int64_t found = 0;
		int64_t it = 0;
		
		while(in_vec.size() > 0) {
			if(in_vec.size() > 1) {
				if(in_vec[0] != in_vec[1]) {
					out_vec.push_back(in_vec[0]);
					in_vec.erase(in_vec.begin());
				} else {
					in_vec.erase(in_vec.begin());
					in_vec.erase(in_vec.begin());
				}
			} else {
				out_vec.push_back(in_vec[0]);
				in_vec.erase(in_vec.begin());
			}
		
		}
		
		/*
		for(int i = 0; i < in_vec.size(); i = i + 2) {
			//cout << i << endl;
			if(in_vec[i] != in_vec[i+1]) {
				out_vec.push_back(in_vec[i]);
				if(i+1 == in_vec.size()-1) {
					out_vec.push_back(in_vec[i+1]);
				} else if (in_vec[i+1] != in_vec[i+2]) {
					out_vec.push_back(in_vec[i+1]);
					i++;
				}
				i++;
			}
		}*/
		/*
		while(found < N-1) {
			int64_t base = it + (found %2);
			if(in_vec[base] != in_vec[base]) {
				found++;
				out_vec.push_back(in_vec[it]);
			}
		}
		*/
		/*for(int64_t i = 0; i < in_vec.size(); i++) {
			for(int64_t j = 0; j < N; j++) {
				cin >> put;
				in_vec.push_back(put);
			}
		}*/
		

		//cout << in_vec.size() << endl;
		cout << "Case #" << iii+1 << ":";
		for(int64_t i = 0; i < out_vec.size(); i++) {
			cout << " " << out_vec[i];
		}
		if(iii != T - 1) cout << endl;
	}
		/*
		culprit = 0;
		culprit_loc = 0;
		for(int64_t i = 0; i < N; ++i) {
			dupe_vec.clear(); 
			dupe_vec.resize(0);
			//cout << "N " << N << " " << 2*N-1 << endl;
			for(int64_t j = 0; j < 2*N-1; ++j) {
				dupe_vec.push_back(in_vec[j][i]); //= in_vec[][i];
				//cout << dupe_vec.back() << " ";
			}
			//cout << "Size " <<  dupe_vec.size() << endl;
		
			//cout << dupe_vec.size() << endl;
			sort(dupe_vec.begin(), dupe_vec.end());
			cout << endl << "STATS ";
			for(int i = 0; i < dupe_vec.size(); ++i) {
				cout << dupe_vec[i] << " ";
			} cout << endl;	
			//unique(dupe_vec.begin(), dupe_vec.end());
			for(int64_t j = 0; j < dupe_vec.size(); j = j + 2) {
				if(j == dupe_vec.size() - 1) {
					culprit = dupe_vec[j];
					culprit_loc = j/2;
					break;
				}
			
				//cout << j << " " << dupe_vec[j] << " " << dupe_vec[j+1] << endl;
			
				if(dupe_vec[j] != dupe_vec[j+1]) {
					culprit = dupe_vec[j];
					culprit_loc = j;
					//cout << "yay" << endl;
					//cout << culprit << " " << culprit_loc << endl;
					break;
				}
			}	
		}
		
		cout << endl << culprit << " " << culprit_loc << " " << 2*N-1 << " " << N << " STATS" << endl;
		//Now we have the specific row/column it's from...
		
		if(culprit_loc < 2*N - 1) { //There's something missing in the first half...
			for(int64_t i = N-1; i < 2*N-1; i++) {
				out_vec.push_back(in_vec[i][culprit_loc]);
				//cout << in_vec[i][culprit_loc];
				//cout << "woo" << endl;
			}
		} else {
			for(int64_t i = 0; i < N; i++) {
				//cout << in_vec[i][culprit_loc];
				out_vec.push_back(in_vec[i][culprit_loc]);
			}
		}
		
		sort(out_vec.begin(), out_vec.end());
		/*
				for(int64_t i = 0; i < in_vec.size(); i++) {
			for(int64_t j = 0; j < in_vec[i].size(); j++) {
				cout << in_vec[i][j] << " ";
			}
			cout << endl;
		}

		//unique(out_vec.begin(), out_vec.end());
		
		cout << "Case #" << iii + 1 << ": ";
		for(int64_t i = 0; i < N; ++i) {
			cout << out_vec[i] << " ";
		}
		cout << endl;
		
	}*/
	return 1;
}