#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int a[100][100];
int lawn[100][100];
int N,M;
int row[100];
int col[100];

void reset(){
	for(int i=0; i<100; i++) {
		for(int j=0; j<100; j++) {
			a[i][j] = 0;
			lawn[i][j] = 0;
		}
	}
}


int main(){
	int tests;
	cin >> tests;
	int n = tests;
	loop:
	if(n==0) return 0;
	n--;
		reset();

		cin >> N >> M;

		//input matrix
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				int m;
				cin >> m;
				a[i][j] = m;
			}
		}

		//make lawn matrix
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				lawn[i][j] = 100;
			}
		}

		//find max for rows
		for(int i=0; i<N; i++) {
			int mx =-1;
			for(int j=0; j<M; j++) {
				mx = max(a[i][j], mx);
			}
			row[i] = mx;
		}

		//find max for col
		for(int i=0; i<M; i++) {
			int mx = -1;
			for(int j=0; j<N; j++) {
				mx = max(mx, a[j][i]);
			}
			col[i] = mx;
		}

		//cut rows
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				lawn[i][j] = min(col[j],min(row[i],lawn[i][j]));
			}
		}

		//check if matrices equql
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				if(lawn[i][j]!=a[i][j]) {
					cout << "Case #" << tests-n << ": NO" << endl;
					goto loop;
				}
			}
		}

		cout << "Case #" << tests-n << ": YES" << endl;
		goto loop;

	return 0;
}