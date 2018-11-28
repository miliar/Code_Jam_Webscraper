
#include <iostream>
#include <cctype>
#include <string>
#include <vector>
using namespace std;

#define FOR(x,s,n) for(typeof(s) x=(s);x<(n);x++)
#define REP(x,n) for(typeof(n) x=0;x<(n);x++)
#define P(x,N,M) 
//REP(i,N){cout << endl; REP(j,M){cout << x[(i*M)+j] << " ";}cout << endl;}
int main()
{
	int C;
	cin >> C;
	REP(testcase,C) {


		int M,N;
		
		cin >> N >> M;
		int x[N*M];
		REP(i,N) {
			REP(j,M) {
				cin >> x[(i*M)+j];
			}
		}

		bool possible=true;

		REP(i,N){
			REP(j,M) {
				if(x[(i*M)+j]>100 
				||x[(i*M)+j]<1) {
					possible=false;
					goto next;
				}
			}
		}

		if(N==1 || M==1) goto next;


		
		FOR(h,1,101) {
		REP(i,N) {

			bool e=true;
REP(j,M) {
				int v=x[(i*M)+j];
				if(v==0) {
					continue;
				}
				if(v!=h) {
					e=false;
					break;
				}
			}

			if(e) {
				REP(j,M) {
					int v=x[(i*M)+j];
					if(v==h) {
						x[(i*M)+j]=0;
					}

				}
			}
			//cout << "Firest end " ;
			P(x,N,M);
		}
		REP(j,M) {

			bool e=true;
			REP(i,N) {
				int v=x[(i*M)+j];
				if(v==0) {
					continue;
				}
				if(v!=h) {
					e=false;
					break;
				}
			}

			if(e) {
				REP(i,N) {
					int v=x[(i*M)+j];
					if(v==h) {
						x[(i*M)+j]=0;
					}

				}
			}
		}
		//cout << "Firest end2 " ;
			P(x,N,M);
			
			
		}

		REP(i,N) {
			REP(j,M) {
				if(x[(i*M)+j]!=0) {
					possible=false;
					goto next;
				}
			}
		}




next:
		if(possible) {
			cout << "Case #" << testcase+1 << ": YES" << endl;
		} else {
			cout << "Case #" << testcase+1 << ": NO" << endl;
		}

	}
	return 0;
}
