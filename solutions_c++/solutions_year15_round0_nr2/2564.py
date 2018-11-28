#include<cstdio>
using namespace std;

int res;

void BF(int *P, int cur, int max){
    if(cur+max < res)	res = cur+max;
    if(max < 4)	return;
    if(P[max]+cur >= res)   return;
    int sav = P[max];
    P[max] = 0;
    for(int i=1; i<=max/2; ++i){
	P[max-i] += sav;
	P[i] += sav;
	int nmax;
	for(int j=max-1; j>0; --j){
	    if(P[j] > 0){
		nmax = j;
		break;
	    }
	}
	BF(P, cur+sav, nmax);
	P[max-i] -= sav;
	P[i] -= sav;
    }
    P[max] = sav;
    return;
}

int main(){
    int T, D, pi;
    int P[10];
    scanf(" %d ", &T);
    for(int t=1; t<=T; ++t){
	for(int i=0; i<10; ++i)	P[i] = 0;

	scanf(" %d ", &D);
	res = 0;
	for(int i=0; i<D; ++i){
	    scanf(" %d ", &pi);
	    ++P[pi];
	    if(pi > res)    res = pi;
	}

	BF(P, 0, res);

	printf("Case #%d: %d\n", t, res);
    }
    return 0;
}
