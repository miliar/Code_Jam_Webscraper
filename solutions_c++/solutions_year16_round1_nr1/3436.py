#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include<map>
using namespace std;

int main() {
	//FILE *fin = freopen("B-small-attempt0.in", "r", stdin);
	FILE *fin = freopen("A-large.in", "r", stdin);
	assert(fin != NULL);
	//FILE *fout = freopen("B-small-attempt0.out", "w", stdout);
	FILE *fout = freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string s;
		cin >> s;
		string result="";
		if (s.size()>0)
			result += s[0];
		for (int i = 1; i < s.size(); i++)
		{
			if (s[i] <= result[i - 1]||s[i]<result[0]) result += s[i];
			else result = s[i] + result;
		}

		cout << "Case #" << t<<": ";
		for (int i = 0; i < result.size();i++)
		{
			cout << result[i];
		}
		cout << endl;


	}
	exit(0);
}