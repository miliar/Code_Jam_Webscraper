#include <cstdio>
#include <iostream>
using namespace std;

FILE * fin, *fout;

long long T, P, Q, minGen;
long double Check;

int gcd(int a, int b){
	if (b == 0) return a;
	else return gcd(b, a%b);
}

int main(){
	int i, p, d, p2 = 1;

	//fopen_s(&fin, "test.in", "r");
	//fopen_s(&fout, "test.out", "w");

	scanf("%d", &T); // fscanf_s(fin, "%d", &T);// 
	for (i = 1; i <= T; i++){
		scanf("%d/%d", &P, &Q); // fscanf_s(fin, "%d/%d", &P, &Q); // 

		d = gcd(P, Q);
		P /= d; Q /= d;

		if (P > Q){
			minGen = 41;
		}
		else if (P == Q){
			minGen = 1;
		}
		else{
			p2 = 1;
			for (p = 1; p < 41; p++){
				p2 *= 2;
				if ((P * p2) >= (2 * Q)){
					p--; p2 /= 2;
					break;
				}
			}

			minGen = p;

			while (Q>1) {
				if (Q % 2) minGen = 41, Q = 0;
				else Q /= 2;
			}
		}

		if (minGen > 40)
			printf("Case #%d: impossible\n", i); // fprintf(fout, "Case #%d: impossible\n", i); 
		else printf("Case #%d: %d\n", i, minGen); // fprintf(fout, "Case #%d: %d\n", i, minGen); 
	}

	return 0;
}