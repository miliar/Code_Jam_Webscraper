#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <iomanip>
#include <string>
#include <map>
using namespace std;

//#define in cin
//#define out cout
ifstream in("D-small-attempt1.in.txt");
ofstream out("D-small-out");

// D
int T, M, N;
vector<string> VS;
vector<int> server[6];
map<int, int> hm;
string str;

int getRes(int sid) {
	int sz = server[sid].size();
	if (sz == 0) return 0;
	int id = server[sid][0];
	int res = 1 + VS[id].size();
	for (int i = 1; i < sz; i++) {
		int id1 = server[sid][i];
		int t = VS[id1].size();
		int len1 = VS[id1].size();
		for (int j = 0; j < i; j++) {
			int id2 = server[sid][j];
			int len2 = VS[id2].size();
			int common = 0;
			for (int k = 0; k < min(len1, len2); k++) {
				if (VS[id1][k] == VS[id2][k]) common++;
				else break;
			}
			t = min(t, len1-common);
		}
		res += t;
	}
	return res;
}
int main()
{
	in >> T;
	for (int cnt = 1; cnt <= T; cnt++) {
		in >> M >> N;
		int bnd = 1;
		VS.clear();
		hm.clear();
		for (int i = 0; i < M; i++) {
			in >> str;
			VS.push_back(str);
			bnd *= N;
		}
		for (int tt = 0; tt <= bnd-1; tt++) {
			for (int i = 0; i < N; i++) {
				server[i].clear();
			}
			int tmp = tt;
			for (int i = 0; i < M; i++) {
				int id = (tmp % N);
				tmp /= N;
				server[id].push_back(i);
			}
			/*
			cout << "get" << endl;
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < server[i].size(); j++) {
					cout << server[i][j] << " ";
				}
				cout << endl;
			}
			cout << "over" << endl;
			*/
			int t = 0;
			for (int i = 0; i < N; i++) {
				t += getRes(i);
				//cout << t << endl;
			}
			if (hm.find(t) == hm.end()) hm[t] = 1;
			else hm[t] += 1;
		}
		int mx = 0;
		for (map<int, int>::iterator itr = hm.begin(); itr != hm.end(); itr++) {
			if (itr->first > mx) mx = itr->first;
		}
		out << "Case #" << cnt << ": " << mx << " " << hm[mx] << endl;
	}
	return 0;
}

/*
// B
int A[12], p[12], T, N;

int main()
{
	in >> T;
	for (int cnt = 1; cnt <= T; cnt++) {
	    in >> N;
	    for (int i = 0; i < N; i++) {
	        in >> A[i];
	        p[i] = i;
	    }
	   	int res = 100;	    
	    while (true) {
	        bool valid = true, up = true;
	        for (int i = 0; i < N-1; i++){
	            if (up && A[p[i]] <= A[p[i+1]]) continue;
	            else up = false;
	            if (!up && A[p[i]] < A[p[i+1]]) valid = false;
	        }
	        if (valid) {
	        	int t = 0;
		        for (int i = 0; i < N; i++){
		            for (int j = i+1; j < N; j++){
		                if (p[i] > p[j]) t++;
		            }
		        }
		        // out << res << endl;
		        res = min(res, t);
		    }
	        if (!next_permutation(p, p + N)) break;
	    }
	    out << "Case #" << cnt << ": " << res << endl;
	}
	return 0;
}
*/

/*
// A
int T, N, X;
int S[705];

int main()
{
	in >> T;
	for (int cnt = 1; cnt <= T; cnt++) {
		in >> N >> X;
		int ss;
		memset(S, 0, sizeof(S));
		for (int i = 0; i < N; i++) {
			in >> ss;
			S[ss]++;
		}
		int res = 0;
		int i = X;
		while (i >= 1) {
			if (S[i] == 0) {
				i--;
				continue;
			}
			int j = min(X-i, i);
			for ( ; j >= 1; j--) {
				if (S[j] > 0) {
					int t = min(S[j], S[i]);
					if (i == j) t = t/2;
					S[j] -= t;
					S[i] -= t;
					res += t;
					if (S[i] == 0) {
						break;
					}
				}
			}
			if (S[i]) {
				res += S[i];
				S[i] = 0;
			}
			i--;
		}
		out << "Case #" << cnt << ": " << res << endl;
	}
	return 0;
}

*/