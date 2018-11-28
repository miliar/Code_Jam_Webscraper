#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
using namespace std;

string solve(int X, int R, int C) {
	if ((R*C%X) != 0)
		return "RICHARD";
	if (X==3 && (R==1 || C==1))
		return "RICHARD";
	if (X==4 && R*C<12)
		return "RICHARD";
	return "GABRIEL";
}

int main() {
	freopen("D-small-attempt0.in", "rt", stdin); freopen("D-small.out", "wt", stdout);
	//freopen("D-large.in", "rt", stdin); freopen("D-large.out", "wt", stdout);
	//freopen("test.in","rt",stdin); freopen("test.out","wt",stdout);

	int N,X,R,C;
	cin>>N;
	for (int i=0; i<N; i++) {
		cin>>X>>R>>C;
		cout << "Case #" << i+1 << ": " << solve(X,R,C) << endl;
	}
}
