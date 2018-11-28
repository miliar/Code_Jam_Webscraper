#include <iostream>
#include <stdio.h>
#include <queue>
#include <algorithm>
#include <vector>
using namespace std;
int tc, n, r, p, s, counter;
char arr[10000];
queue<char> q;
vector<char> prev;
vector<char> cur;
vector<string> sorter;
vector<string> sorter2;

char winner(char a, char b){
	if (a == 'P' && b == 'R') return a;
	if (a == 'R' && b == 'P') return b;
	if (a == 'S' && b == 'P') return a;
	if (a == 'P' && b == 'S') return b;
	if (a == 'R' && b == 'S') return a;
	if (a == 'S' && b == 'R') return b;
}

void cl(){
	while (!q.empty()){
		q.pop();
	}
}
//r p s
bool check(int a, int b, int c){
	if (a == 0 && b == 0 && c == 0) return true;
	if (a == 1 && b == 1 && c == 0){
		cur.push_back('R');
		cur.push_back('P');
		return true;
	}
	if (a == 1 && b == 0 && c == 1){
		cur.push_back('R');
		cur.push_back('S');
		return true;
	}
	if (a == 0 && b == 1 && c == 1){
		cur.push_back('S');
		cur.push_back('P');
		return true;
	}
	int aprime = a + b - c;
	if (aprime % 2 == 1) return false;
	aprime /= 2;
	bool cc = check(c - b + aprime, aprime, b - aprime);
	if (!cc) return cc;
	for (vector<char>::iterator it = cur.begin(); it != cur.end(); it++){
		if (*it == 'R'){
			prev.push_back('R');
			prev.push_back('S');
		} else if (*it == 'P'){
			prev.push_back('R');
			prev.push_back('P');
		} else {
			prev.push_back('S');
			prev.push_back('P');
		}
	}
	cur.clear();
	for (vector<char>::iterator it = prev.begin(); it != prev.end(); it++){
		cur.push_back(*it);
	}
	prev.clear();
	return cc;
}

void sortt(){
	sorter2.clear();
	while (sorter.size() > 1){
		string a = *sorter.rbegin();
		sorter.pop_back();
		string b = *sorter.rbegin();
		sorter.pop_back();
		if (a < b){
			sorter2.push_back(a + b);
		} else {
			sorter2.push_back(b + a);
		}
	}
	for (vector<string>::iterator it = sorter2.begin(); it != sorter2.end(); it++){
		sorter.push_back(*it);
	}
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("a-large.out", "w", stdout);
	scanf("%d", &tc);
	for (int i = 0; i < tc; i++){
		sorter.clear();
		sorter2.clear();
		cur.clear();
		prev.clear();
		scanf("%d%d%d%d", &n, &r, &p, &s);
		if (check(r, p, s)){
			for (vector<char>::iterator it = cur.begin(); it != cur.end(); it++){
				string a = "";
				a = a + *it;
				sorter.push_back(a);
			}
			while (sorter.size() > 1){
				sortt();
			}
			cout << "Case #" << i + 1 << ": " + *sorter.begin() << endl;
		} else {
			printf("Case #%d: IMPOSSIBLE\n", i + 1);
		}
	}
}
