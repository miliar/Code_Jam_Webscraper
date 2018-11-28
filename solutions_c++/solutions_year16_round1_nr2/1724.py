#include <iostream>
#include <vector>
#include <utility>
#include <deque>
#include <cstring>
#include <unordered_map>
#include <algorithm>

typedef unsigned long int uli;
typedef long int li;
using namespace std;

vector<int> compute_res(unordered_map<int,int>& M) {
	vector<int> res;
	unordered_map<int,int>::iterator it;
	for(it = M.begin(); it != M.end(); it++) {
		if((it->second & 1)) {
			res.push_back(it->first);
		}
	}
	sort(res.begin(),res.end());
	return res;
}

int main(int argc, char *argv[])
{
	int T, N, val, limit;
	vector<int> res;
	cin >> T;
	for(int i=1; i<=T; i++) {
		cin >> N;
		limit = 2*N*N - N;
		unordered_map<int,int> M;
		for(int j=1; j<=limit; j++) {
			cin >> val;
			if (M.find(val)==M.end()) {
				M[val] = 1;
			} else {
				M[val] = M[val] + 1;
 			}
		}
		res = compute_res(M);
		cout << "Case #" << i << ":";
		for(int j=0; j<N; j++) {
			cout << " " << res[j];
		}
		cout << endl;	
	}
    return 0;
}
