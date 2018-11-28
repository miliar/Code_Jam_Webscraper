#include <cstdio>
#include <algorithm>
using namespace std;

#define Long long long
const int MAXN = 101;
Long X;
int T , N;
Long h[MAXN];

FILE *fin = fopen("A-large.in" , "r");
FILE *fout= fopen("A-large.out" , "w");

int main(){
	fscanf(fin , "%d" , &T);
	for(int t = 1 ; t <= T ; t++){
		fscanf(fin , "%lld %d" , &X , &N);
		for(int n = 0 ; n < N ; n++)
			fscanf(fin , "%lld" , &h[n]);
		sort(h , h + N);
		Long added = 0;
		Long res = 1;
		for(int p = 1 ; p <= 60 ; p++)
			res *= (Long)(2);
		if(X == 1)
			res = N;
		else {
			for(int n = 0 ; n < N ; n++){
				res = min(res , (Long)(added + N - n));
				while(X <= h[n]){
					X += X - 1;
					added++;
				}
				X += h[n];
			}
			res = min(res , added);
		}
		fprintf(fout , "Case #%d: %lld\n" , t , res);
	}
	return 0;
}