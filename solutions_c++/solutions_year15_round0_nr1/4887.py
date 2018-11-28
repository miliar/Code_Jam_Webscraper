#include <iostream>
#include <stdio.h>

using namespace std;

void print_S(int S[], int n){
	for(int i = 0; i < n; ++i){
		if(i != 0)
			cout << ", ";
		cout << S[i];
	}
	cout << endl;
}

int main(){
	int T;
	scanf("%d\n", &T);
	for(int c = 1; c <= T; ++c){
		int Smax;
		scanf("%d ", &Smax);
		int S[Smax + 1];
		for(int i = 0; i < Smax + 1; ++i){
			char c;
			scanf("%c", &c);
			S[i] = c - '0';
		}
		int t = 0, p = S[0];
		for(int i = 1; i < Smax + 1; ++i){
			if(S[i] != 0){
				if(p < i){
					t += i - p;
					p += t;
				}
			}
			p += S[i];
		}
		scanf("\n");
		cout << "Case #" << c << ": " << t << endl;
	}
	return 0;
}
