#include <iostream>
#include <cstdio>

using namespace std;

bool inf;
int T, N, f, w;
int curN[1001];

bool check(){
	int target = (1 << 10) - 1;
	for (int i = 0; i <= f; ++i){
		int temp = curN[i];
		while (temp){
			w = w | (1 << (temp % 10));
			temp /= 10;
		}
	}
	if (w == target){
		return true;
	}
	return false;
}

void add(){
	int r = 1e9;
	int s = N;
	for (f = 0; s; ++f){
		int ts = (curN[f] + s) / r;
		curN[f] = (curN[f] + s) % r;
		s = ts;
	}
}

void input(){
	scanf ("%d", &N);
	curN[0] = N;
	f = 0;
	w = 0;
	inf = false;
}

void solve(){
	for (int i = 0 ; !check(); ++i){
		add ();
		if (i > 10000){
			inf = true;
			break;
		}
	}
}

void output(int t){
	printf ("Case #%d: ", t);
	if (inf){
		printf ("INSOMNIA\n");
		return;
	}
	for (int i = f - 1; i >= 0; --i){
		printf ("%d", curN[i]);
	}
	printf ("\n");
}

int main(){
	freopen ("a.in", "r", stdin);
	freopen ("out.txt", "w", stdout);
	scanf ("%d", &T);
	for (int i = 1; i <= T; ++i){
		input();
		solve();
		output(i);
	}
	return 0;
}