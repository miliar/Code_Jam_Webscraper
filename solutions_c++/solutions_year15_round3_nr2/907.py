#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <iomanip>
#include <string>
#include <cstring>
using namespace std;

int countstr(char * s, const char * sub) {
	char * tmp = s;
	int count = 0;
	while(tmp = strstr(tmp, sub))
	{
		count++;
		tmp++;
	}
	return count;
}

void iterate(char * test, int len, int cum_prob, int &mx, map<char, int> & counts, int s, const char* target, int &prob_sum) {
	for (map<char, int> :: iterator it = counts.begin(); it != counts.end(); it++) {
		test[len] = it->first;
		int new_prob = cum_prob * it->second;
		if (len == s-1) {
			int count = countstr(test, target);
			//printf("%s %s %d\n", test, target, count);
			prob_sum += new_prob * count;
			mx = max(mx, count);
			//cout << "changing mx " << count << " " << mx << endl;
		}
		else {
			iterate(test, len+1, new_prob, mx, counts, s, target, prob_sum);
		}
	}
}

double answer(int k, int l, int s, string board, string target) {
	map<char, int> counts;
	for (int i = 0; i < board.size(); i++) counts[board[i]]++;
	const char * b = board.c_str();
	const char * t = target.c_str();
	char test[s];
	int mx = 0, prob_sum = 0;;
	iterate(test, 0, 1, mx, counts, s, t, prob_sum);
	double prob = prob_sum;
	for (int i = 0; i < s; i++) mx *= k;
	//cout << "mx " << mx << endl;
	prob = mx - prob;
	for (int i = 0; i < s; i++) prob/=k;
	return prob;
}

int main()
{
	cout << setprecision(7);
    int t;
	cin >> t;
	for (int _t = 1; _t <= t; _t++) {
		int k, l, s;
		cin >> k >> l >> s;
		string board, target;
		cin >> board >> target;
		cout << "Case #" << _t << ": " << answer(k, l, s, board, target) << endl;
	}
    return 0;
}
