//Code Jam problem "Revenge of the Pancakes" Qualification Round 2016
//https://code.google.com/codejam/contest/6254486/dashboard
//-Thomas Steinke codejam@thomas-steinke.net 2016-04-08

#include <queue>
#include <iostream>
#include <string>
#include <cassert>
using namespace std;

int strtoint(string s, int size) {
	int x = 0;
	for (int i = 0; i < size; i++) {
		x*=2;
		if (s[i] == '-') x++;
		else assert(s[i] == '+');
	}
	return x;
}
string inttostr(int x, int size) {
	string s = "";
	for (int i = 0; i < size; i++) {
		if (x % 2 == 0) 
			s = "+" + s;
		else
			s = "-" + s;
		x = x/2;
	}
	return s;
}

string flip(string s, int len, int size) {
	string t = "";
	for (int i = 0; i < len; i++) t = t + (s[len-1-i] == '+' ? '-' : '+');
	for (int i = len; i < size; i++) t = t + s[i];
	return t; 
}

int* lookup_table(int size) {
	int* table = new int[1 << size];
	for (int i = 1; i < (1 << size); i++) table[i]=-1;
	table[0]=0;
	queue<int> q;
	q.push(0);
	while (!q.empty()) {
		int x = q.front(); q.pop();
		int d = table[x];
		string s = inttostr(x,size);
		for (int i = 0; i <= size; i++) {
			string t = flip(s,i,size);
			int y = strtoint(t,size);
			if (table[y]<0) {
				table[y]=d+1;
				q.push(y);
			}
		}
	}
	return table;
}

void tests() {
	int size = 3;
	for (int x = 0; x < (1 << size); x++) {
		string s = inttostr(x,size);
		int y = strtoint(s,size);
		cout << x << " -> " << s << " -> " << y << endl;
	}
	string ss[] = {"+++","---","-++","--+","++-"};
	for (int j = 0; j < 5; j++) {
		string s = ss[j];
		cout << endl;
		for (int i = 0; i <= (int) s.length(); i++) {
			cout << "flip(\"" << s <<"\"," << i << "," << s.length() << ")=" << flip(s,i,s.length()) << endl;
		}
	}
	cout << endl;
}

int main() {
	int maxsize=10;
	int * tables[maxsize];
	for (int size = 1; size <= maxsize; size++) 
		tables[size] = lookup_table(size);
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		string s; cin >> s;
		int x = strtoint(s,s.length());
		int ans = tables[s.length()][x];
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
