#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <cmath>
#include <map>




using namespace std;
static map<int, int> cache;
static int prev_root = -1;


bool check_p(int num) {
	string s = to_string(num);
	string s2 = string ( s.rbegin(), s.rend() );
	//cout << "Check_p: " << s << "  " << s2 << " " << (s == s2) << endl;
	return s == s2;
}

int count_f(int start, int end) {
	double intpart;
	int count;
	count = 0;
	
	for (int i = start; i <= end; ++i) {
		
		if (cache.find(i) != cache.end()) {
			count++;
			i = cache[i];
			continue;
		}
		if (check_p(i)) {
			double root = sqrt(i);
			if ( modf (root , &intpart) == 0) {
				if (check_p((int)intpart)) {
					count++;
					if (prev_root != -1) {
						cache[prev_root] = i - 1;
						prev_root = i;
					} else {
						prev_root = i;
					}
				}
			}
		}
	}
	return count;
}




vector <int> calc(int start, int end) {
	vector <int> vals(end - start + 1);
	for (int i=start; i <= end; ++i ) {
		//vals[i] = -1;
		if (check_p(i) == true) {
			int sq = i*i;
			if (check_p(sq) == true) {
				vals[sq] = i;
				//vals[i] = -1;
			}
		}
	}
	return vals;
}

int  check_in(vector<int> vals, int start, int end) {
	int c = 0;

	int vs = 0;
	//cout << "Checking rang: " << start << ", " << end << endl; 
	
	for (int i=start; i <= end; i++) {
		if (vals[i] > 0 ) {
			c++;
			//cout << " "<< i << " " << vals[i];
		}
	}

	return c;
}

int main(int argc, char *argv[]) {
	string line;
	int N;
	getline(cin, line);
	stringstream nstream(line);
	nstream >> N;
	vector <int> vals = calc(0, 1000);
	
	for (int i =0; i < N; i ++) {
		getline(cin, line);
		stringstream stream(line);
		int start, end;
		stream >> start;
		stream >> end;
		cout << "Case #" << i + 1 << ": " << check_in(vals, start, end) << endl;
	
					
	}
	return 0;
}