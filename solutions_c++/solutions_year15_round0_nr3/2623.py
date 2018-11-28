#include <bits/stdc++.h>
using namespace std;

int t;
int l, x;
char cad[10002];
int num[10002];
int acum[10002];

int main (){

	freopen ("C-small-attempt0.in", "r", stdin);
	freopen ("sol.out", "w", stdout);
	scanf ("%d", &t);
	int cont = 0;
	while (t--){
		cont++;
		scanf ("%d%d", &l, &x);
		for (int i = 1; i <= l; i++)
			scanf (" %c", &cad[i]);
		for (int i = 1; i <= l; i++){
			if (cad[i] == 'i') num[i] = 2;
			if (cad[i] == 'j') num[i] = 3;
			if (cad[i] == 'k') num[i] = 4;
		}
		for (int i = 1; i <= l; i++){
			for (int k = i + l; k <= (l * x); k += l)
				num[k] = num[i];
		}
		acum[1] = num[1];
		for (int i = 2; i <= (l * x); i++){
			if (acum[i - 1] == 1){
				if (num[i] == 2) acum[i] = 2;
				if (num[i] == 3) acum[i] = 3;
				if (num[i] == 4) acum[i] = 4;
			}
			if (acum[i - 1] == 2){
				if (num[i] == 2) acum[i] = 5;
				if (num[i] == 3) acum[i] = 4;
				if (num[i] == 4) acum[i] = 7;
			}
			if (acum[i - 1] == 3){
				if (num[i] == 2) acum[i] = 8;
				if (num[i] == 3) acum[i] = 5;
				if (num[i] == 4) acum[i] = 2;
			}
			if (acum[i - 1] == 4){
				if (num[i] == 2) acum[i] = 3;
				if (num[i] == 3) acum[i] = 6;
				if (num[i] == 4) acum[i] = 5;
			}
			if (acum[i - 1] == 5){
				if (num[i] == 2) acum[i] = 6;
				if (num[i] == 3) acum[i] = 7;
				if (num[i] == 4) acum[i] = 8;
			}
			if (acum[i - 1] == 6){
				if (num[i] == 2) acum[i] = 1;
				if (num[i] == 3) acum[i] = 8;
				if (num[i] == 4) acum[i] = 3;
			}
			if (acum[i - 1] == 7){
				if (num[i] == 2) acum[i] = 4;
				if (num[i] == 3) acum[i] = 1;
				if (num[i] == 4) acum[i] = 6;
			}
			if (acum[i - 1] == 8){
				if (num[i] == 2) acum[i] = 7;
				if (num[i] == 3) acum[i] = 2;
				if (num[i] == 4) acum[i] = 1;
			}
		}
		int ban = 0;
		for (int i = 1; i < (l * x); i++){
			for (int j = i + 1; j < (l * x); j++){
				if (acum[i] == 2 && acum[j] == 4 && acum[l * x] == 5)
					ban = 1;
			}
		}
		if (ban)
			printf ("Case #%d: YES\n", cont);
		else
			printf ("Case #%d: NO\n", cont);
	}
	return 0;
}