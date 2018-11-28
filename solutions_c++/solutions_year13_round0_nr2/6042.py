//============================================================================
// Name        : Problem B Lawnmower.cpp
// Author      : Dhrubo Abdullah Khan
// Version     : 1
// Copyright   : Free to share
// Description : Adhoc
//============================================================================

#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

#define FORS(i,s,e) for(int i = int(s); i < int(e); i++)
#define FOR(i,e) FORS(i,0,e)
#define MAX 100

typedef vector<int> vi;
typedef vector<vi> vvi;

int main() {
	int T;
	cin >> T;

	int c = 0;

	FOR(k,T){
		c++;

		int N,M;
		cin >> N >> M;
		vvi l(N,vi(M,100));
		vvi lFinal(N,vi(M,100));

		vi rMax(N,-1);
		vi rMaxId(N,0);
		vi rMin(N,MAX+1);
		vi rMinId(N,0);

		FOR(i,N){
			FOR(j,M){
				cin >> lFinal[i][j];
				if(lFinal[i][j] >= rMax[i]){
					rMax[i] = lFinal[i][j];
					rMaxId[i] = j;
				}
				if(lFinal[i][j] <= rMin[i]){
					rMin[i] = lFinal[i][j];
					rMinId[i] = j;
				}
			}
		}

		vi cMax(M,-1);
		vi cMaxId(M,0);
		vi cMin(M,MAX + 1);
		vi cMinId(M,0);

		FOR(j,M){
			FOR(i,N){
				if(lFinal[i][j] > cMax[j]){
					cMax[j] = lFinal[i][j];
					cMaxId[j] = i;
				}
				if(lFinal[i][j] <= rMin[j]){
					cMin[j] = lFinal[i][j];
					cMinId[j] = i;
				}
			}
		}


		//entering along all the columns
		FOR(j,M){
			FOR(i,N){
				l[i][j] = cMax[j];
			}
		}

//		//entering along all the rows
		FOR(i,N){
			FOR(j,M){
				if(rMax[i] > rMin[i])
					break;
				l[i][j] = rMax[i];
			}
		}

//		FOR(i,N){
//			FOR(j,M){
//				cout << lFinal[i][j] << " ";
//			}
//			cout << endl;
//		}
//		cout << endl;
//
//		FOR(i,N){
//			FOR(j,M){
//				cout << l[i][j] << " ";
//			}
//			cout << endl;
//		}
//		cout << endl;


		//check all rows with min max
		bool No = false;
		FOR(i,N){
			FOR(j,M){
				if(lFinal[i][j] != l[i][j]){
					cout << "Case #" << c << ": NO";
					No = true;
					break;
				}
			}
			if(No){
				break;
			}
		}

		if(!No){
			cout << "Case #" << c << ": YES";
		}
		if(c != T)
			cout << endl;

		rMax.clear();
		rMin.clear();
		cMax.clear();
		cMin.clear();
		rMaxId.clear();
		rMinId.clear();
		cMaxId.clear();
		cMinId.clear();
	}

	return 0;
}
