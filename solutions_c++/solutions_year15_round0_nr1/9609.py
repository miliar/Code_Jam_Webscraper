#include <bits/stdc++.h>

#define DB(a)       cerr << #a << ": " << (a) << endl;

using namespace std;

int main() 
{
	int T;
	cin >> T;
	int t = 1;
	while(t<=T) {
		cout << "Case #" << t++ << ": ";
		string s;
		int n;
		cin >> n >> s;
		int count = s[0]-'0';
		int add = 0;
		if(count == 0) add++, count++;
		for(int i=1; i<n+1; i++) {
			if(count<i) add += i-count, count += i-count;
			count += s[i]-'0';
		}
		cout << add << endl;
	}
}
