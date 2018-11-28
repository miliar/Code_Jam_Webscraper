#include <cstdio>
#include <queue>
#include <string>
#include <utility>
#include <iostream>

using namespace std;
typedef pair<string, int> si;

string flip(string str, int num) {
	for (int i = 0; i < num; i++) {
		str[i] = str[i]=='+' ? '-' : '+';
	}
	return str;
}

bool done(string str) {
	for (char c : str)	if (c == '-') return false;
	return true;
}



int cmoves (string pcakes){
   int moves = 0;
   for(int i =0;i<pcakes.length()-1;i++) if (pcakes[i] != pcakes[i+1]) moves++;
   if(pcakes[pcakes.length()-1] == '-') moves++;
   return moves;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++){
		string cakes;
		cin >> cakes;/*
		queue<si> q;
		cout << cakes << endl;
		q.push(si(cakes, 0));
		bool found = false;
		if (done(cakes)) found = true;
		while (!found && !q.empty()) {
			string s = q.front().first;
			int k = q.front().second;
			q.pop();
		//	cout << s << k << endl;
			for (int i = 0; i <= (int)s.size(); i++) {
				string s2 = flip(s, i);
				if (done(s2)) {
					found = true;
					printf("%d\n", k+1);
					break;
				}
				q.push(si(s2, k+1));
				//cout << s2 << k;
			}
		}*/
		printf("Case #%d: %d\n", t+1, cmoves(cakes));
		
	}
}
