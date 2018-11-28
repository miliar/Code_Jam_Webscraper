#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
using namespace std;

string solve(vector <int> P) {
	P.push_back(0);
	P.push_back(0);
	P.push_back(0);
	P.push_back(0);
	P.push_back(0);
	sort(P.begin(),P.end(),greater<int>());
	int ans = P[0];
	ans = min(ans,1+max(P[1],P[0]/2 + P[0]%2));
	ans = min(ans,2+max(max(P[2],P[1]/2 + P[1]%2),P[0]/2 + P[0]%2));
	ans = min(ans,3+max(max(P[2],P[1]/2 + P[1]%2),P[0]/3 + P[0]%3));
	ans = min(ans,2+max(P[1],P[0]/3 + P[0]%3));
	ans = min(ans,3+max(max(max(P[3],P[2]/2 + P[2]%2),P[1]/2 + P[1]%2),P[0]/2 + P[0]%2));
	ans = min(ans,4+max(max(max(max(P[4],P[3]/2 + P[3]%2),P[2]/2 + P[2]%2),P[1]/2 + P[1]%2),P[0]/2 + P[0]%2));
	return to_string(ans);
}

int main() {
	freopen("B-small-attempt3.in", "rt", stdin); freopen("B-small.out", "wt", stdout);
	//freopen("B-large.in", "rt", stdin); freopen("B-large.out", "wt", stdout);
	//freopen("test.in","rt",stdin); freopen("test.out","wt",stdout);

	int D, t, T;
	cin>>T;
	for (int i=0; i<T; i++) {
		vector <int> P;
		cin>>D;
		for (int j=0; j<D; j++) {
			cin>>t;
			P.push_back(t);
		}
		cout << "Case #" << i+1 << ": " << solve(P) << endl;
	}
}
