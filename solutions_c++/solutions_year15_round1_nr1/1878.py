#include <stdio.h>
#include <iostream>
#include <string.h>
#include <vector>
#include <cmath>

#define PVI(X) for(int x=0;x<X.size();x++){printf("%d ",X[x]);}printf("\n");
#define SZ(X) ((int)(X).size())
#define ALL(X) (X).begin(), (X).end()
#define REP(I, N) for (int I = 0; I < (N); ++I)
#define REPP(I, A, B) for (int I = (A); I < (B); ++I)
#define RI(X) scanf("%d", &(X))
#define RII(X, Y) scanf("%d%d", &(X), &(Y))
#define RIII(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define DRI(X) int (X); scanf("%d", &X)
#define DRII(X, Y) int X, Y; scanf("%d%d", &X, &Y)
#define DRIII(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)
#define RS(X) scanf("%s", (X))
#define CASET int ___T, case_n = 1; scanf("%d ", &___T); while (___T-- > 0)
#define CASENZ int ___T, case_n = 1; scanf("%d ", &___T); while (___T != 0)
#define MP make_pair
#define PB push_back
#define MS0(X) memset((X), 0, sizeof((X)))
#define MS1(X) memset((X), -1, sizeof((X)))
#define LEN(X) strlen(X)
#define F first
#define S second
using namespace std;

int main(){	
	CASET{
		int ans1,ans2;
		ans1 = ans2 = 0;
		DRI(qnt);
		vector <int> values;
		REP(i,qnt){
			DRI(v);
			values.PB(v);
		}
		int maior_dif = 0;
		REPP(i,1,qnt){
			if(values[i-1]-values[i]>0){
				ans1+=values[i-1]-values[i];
				maior_dif = max(maior_dif,(values[i-1]-values[i]));
			}			
		}
		REP(i,qnt){
			if(i!=(values.size()-1)){
				if(values[i]>=maior_dif)
					ans2+=maior_dif;
				else
					ans2+=values[i];
			}
		}
		// cout<<maior_dif<<endl;
		printf("Case #%d: %d %d\n",case_n++,ans1,ans2);
	}
	return 0;
}
