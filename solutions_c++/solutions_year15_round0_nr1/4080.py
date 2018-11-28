#include <bits/stdc++.h>
using namespace std;

int t;
int n;
char cad[1010];
int total, faltan;

int main (){

	freopen ("A-large.in", "r", stdin);
	freopen ("solA.out", "w", stdout);
	scanf ("%d", &t);
	int cont = 0;
	while (t--){
		cont++;
		scanf ("%d", &n);
		for (int i = 0; i < (n + 1); i++)
			scanf (" %c", &cad[i]);
		total = 0;
		faltan = 0;
		for (int i = 0; i < (n + 1); i++){
			if (total < i){
				faltan += (i - total);
				total += (i - total);
			}
			total += (cad[i] - '0');
		}
		printf ("Case #%d: %d\n", cont, faltan);
	}
	return 0;
}