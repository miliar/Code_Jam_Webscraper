#include <bits/stdc++.h>
 
#define FORO(n)     for (int i = 0; i < n; i++)
#define FOROI(i, n)     for ( i = 0; i < n; i++)
#define MAX_SIZE    200
#define INF         INT_MAX 
using namespace std;

int main ()  {
	int t;
	cin >> t;
	FORO(t) {
		int soma = 0, amig = 0;
		int s, j;
		cin >> s;
		FOROI(j, s+1) {
			char c;
			cin >> c;
			if (c > '0' && j > soma) {
				amig += j - soma;
				soma += j - soma;
			}
			soma += c - '0';
			//cout << soma << endl;
		}
		cout << "Case #" << i+1 << ": " << amig << endl;
	}



}
