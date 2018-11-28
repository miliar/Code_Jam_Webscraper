#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int T;

void solve(){
	string ans;
	freopen("omino.in", "r", stdin);
	freopen("omino.out", "w", stdout);
	fscanf(stdin, "%d", &T);
	for (int trial = 0, x, r, c; trial < T; trial++){
		bool win = false;
		fscanf(stdin, "%d%d%d", &x, &r, &c);
		if (x == 1){
			win = true;
		}
		else if (x==2 && (r*c)%2 == 0){
			win = true;
		}
		else if (x ==3 && (r*c)%3 == 0){
			if (!(r*c == 3)){
				win = true;
			}
		}
		else if (x ==4 && (r*c)%4 == 0){
			if (!(r*c == 4 || r*c == 8)){
				win = true;
			}
		}
		if (win) {
			fprintf(stdout, "Case #%d: %s\n", trial+1, "GABRIEL");
		}
		else {
			fprintf(stdout, "Case #%d: %s\n", trial+1, "RICHARD");
		}
	}
}

int main(){
	solve();
	return 0;
}