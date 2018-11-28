#include <iostream>
#include <cstdio>

using namespace std;

int T;
int K, C, S;

void input(){
	scanf ("%d%d%d", &K, &C, &S);
}

void solve(){
	// solving logic
}

void output(int t){
	printf ("Case #%d: ", t);
	if (K > S){
		printf ("IMPOSSIBLE\n");
		return;
	}
	for (int i = 1; i <= K; ++i){
		printf ("%d ", i);
	}
	printf ("\n");
}

int main(){
	freopen ("d.in", "r", stdin);
	freopen ("out.txt", "w", stdout);
	scanf ("%d", &T);
	for (int i = 1; i <= T; ++i){
		input();
		solve();
		output(i);
	}
	return 0;
}