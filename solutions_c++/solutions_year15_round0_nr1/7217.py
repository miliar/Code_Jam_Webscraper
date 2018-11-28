//Problem: Google Code Jam 2015 Qualification Round A
//Name: Standing Ovation
//Author: Bruce K. B. Tong
//Tag: Greedy

#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

//#define SMALL
#define LARGE

int solve(int Smax, char S[]) {
	int ans = 0, sum = 0;
	for (int i = 0; i < Smax+1; i++) {
		if (sum < i) {
			ans += i-sum;
			sum = i;
		}
		sum += S[i]-'0';
	}
	return ans;
}

int main() {
	freopen("A-sample.in", "rt", stdin);
	#ifdef SMALL
		freopen("A-small-attempt0.in", "rt", stdin);
		freopen("A-small-attempt0.out", "wt", stdout);
	#endif
	#ifdef LARGE
		freopen("A-large.in", "rt", stdin);
		freopen("A-large.out", "wt", stdout);
	#endif
	
	int T;		//1 <= T <= 100
	int Smax;	//0 <= Smax <= 6 (or 1,000)
	char S[1000+1];
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cin >> Smax;
		cin.ignore();
		for (int j = 0; j < Smax+1; j++)
			cin >> S[j];
		cout << "Case #" << i << ": ";
		cout << solve(Smax, S);
		cout << endl;
	}
	return 0;
}