#include <stdio.h>
#include <iostream>
#include <string.h>
#include <vector>

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
		string ans;
		DRIII(X,R,C); 
		if(X==1){
			ans = "GABRIEL";
		}else{ 
			if(R>C){
				int aux = R;
				R = C;
				C=aux;
			}
			if(X==2){
				if(R==1 && C==1)				
					ans = "RICHARD";
				else if(R==1 && C==3)
					ans = "RICHARD";
				else if(R==3 && C==3)
					ans = "RICHARD";
				else
					ans = "GABRIEL";
			}else if(X==3){
				if(R==2 && C==3)
					ans = "GABRIEL";
				else if(R==3 && C==3)
					ans = "GABRIEL";
				else if(R==3 && C==4)
					ans = "GABRIEL";
				else 
					ans = "RICHARD";
			}else if(X==4){
				if(R == 3 && C ==4)
					ans = "GABRIEL";
				else if(R==4 && C==4)
					ans = "GABRIEL";
				else
					ans = "RICHARD";
			}
		}

		printf("Case #%d: ",case_n++);
		cout<<ans<<endl;			
	}
	return 0;
}
