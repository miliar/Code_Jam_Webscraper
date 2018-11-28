//be naame khodaa

#include <iostream>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <string>
#include <cstdio>
#include <algorithm>
#include <set>
#include <cassert>
#include <iomanip>
#include <cstring>
typedef long long ll;

using namespace std;
typedef pair <int, int> pii;

pii p[15], r[15], s[15];
int prank[6] = {0, 0, 1, 2, 2, 1};
int rrank[6] = {1, 2, 2, 1, 0, 0};
int srank[6] = {2, 1, 0, 0, 1, 2};

pii operator + (pii A, pii B)
{
	return {A.first + B.first, A.second + B.second};
}

void rOut(int n);
void sOut(int n);

void pOut(int n){
	if (n == 0) {cout << 'P'; return;}
	int rem = (n+5)%6;
	if (rrank[rem] < prank[rem]){
		rOut(n-1);
		pOut(n-1);
	}
	else{
		pOut(n-1);
		rOut(n-1);
	}
}

void rOut(int n){
	if (n == 0) {cout << 'R'; return;}
	int rem = (n+5)%6;
	if (rrank[rem] < srank[rem]){
		rOut(n-1);
		sOut(n-1);
	}
	else{
		sOut(n-1);
		rOut(n-1);
	}
}

void sOut(int n){
	if (n == 0) {cout << 'S'; return;}
	int rem = (n+5)%6;
	if (prank[rem] < srank[rem]){
		pOut(n-1);
		sOut(n-1);
	}
	else{
		sOut(n-1);
		pOut(n-1);
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	p[0] = {1, 0}, r[0] = {0, 1}, s[0] = {0, 0};
	for (int i = 1; i <= 12; i++){
		p[i] = p[i-1] + r[i-1];
		r[i] = r[i-1] + s[i-1];
		s[i] = p[i-1] + s[i-1];
		assert(p[i] != r[i]);
		assert(p[i] != s[i]);
		assert(r[i] != s[i]);
	}
	int t;
	cin >> t;
	for (int it = 1; it <= t; it++){
		int n, R, P, S;
		cin >> n >> R >> P >> S;
		cout << "Case #" << it << ": ";
		if (make_pair(P, R) == p[n])
			pOut(n);
		else if (make_pair(P, R) == r[n])
			rOut(n);
		else if (make_pair(P, R) == s[n])
			sOut(n);
		else
			cout << "IMPOSSIBLE";
		cout << '\n';
	}
	return 0;
}
