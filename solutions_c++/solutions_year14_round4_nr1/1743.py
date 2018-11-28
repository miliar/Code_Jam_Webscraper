#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N,X;
vector<int> S;

void handle_input() {
	cin >> N >> X;
	int s;
	S.clear();
	for(int i = 0; i < N; i++) {
		cin >> s;
		S.push_back(s);
	}
}

int brute_force() {
	vector<int> Z;
	for(int i = 0; i < S.size(); i++)
		Z.push_back(S[i]);
	sort(Z.begin(), Z.end());
	int result =0;
	for(int i = Z.size()-1; i >= 0; i--) {
		if(Z[i] == 0)
			continue;
		result++;
		for(int j = i-1; j >= 0; j--) {
			if(Z[j] == 0)
				continue;
			if(Z[j] <= X - Z[i]) {
				Z[j] = 0;
				j = 0;
			}
		}
	}
	return result;
}

void process_testcase() {
	//int z = brute_force();
	sort(S.begin(), S.end());
	int result = 0;
	//cout << endl;
	while(S.size() > 0) {
		result++;
		// for(int i = 0; i < S.size(); i++)
			// cout << S[i] << " ";
		// cout << ": ";
		
		int x = S[S.size()-1];
		//cout << x << " ";
		S.pop_back();
		
		if(S.size() > 0) {
			int lo = 0;
			int hi = S.size()-1;
			while(lo < hi) {
				int mid = (hi+lo+1)/2;
				if(S[mid] > X-x)
					hi = mid-1;
				else if(S[mid] < X-x)
					lo = mid;
				else
					lo = hi = mid;
			}
			if(S[lo] <= X-x)
				S.erase(S.begin()+lo);
		}
		//cout << endl;
	}
	//if(result != z)
//		cout << "BAD " << z << " "; 
	cout << result << endl;
}
	
int main() {
	// cout << 100 << endl;
	// for(int j = 0; j < 100; j++) {
		// cout << 10000 << " " << 700 << endl;
		// for(int i = 0; i < 10000; i++)
			// cout << 700 << " ";
		// cout << endl;
	// }
// return 0;
	int T; 
	cin >> T;
	for(int Z = 1; Z <= T; Z++) {
		cout << "Case #" << Z << ": ";
		handle_input();
		process_testcase();
	}
}