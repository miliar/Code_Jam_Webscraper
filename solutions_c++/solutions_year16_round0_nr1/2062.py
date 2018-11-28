#include <iostream>
#include <fstream>
#include <string>

#define REP(i, a, b)		for(i = (int)a; i<=(int)b ; i++)
#define FOR(i, N)			REP(i, 0, N-1)

using namespace std;

int main(){
	ifstream cin("A.in");
	ofstream cout("A-Large.out");

	int t, T;
	cin >> T;
	REP(t, 1, T) {
		int i, j;

		bool done[10];
		FOR(i, 10) done[i] = false;

		int N, n=0;
		cin >> N;
		if (N == 0){
			cout << "Case #" << t << ": INSOMNIA" << endl;
			continue;
		}

		j = 0;
		while (n != 10) {
			j++;
			int M = N * j;
			while (M){
				int k = M % 10;
				M /= 10;
				if (done[k]) continue;
				done[k] = true;
				n++;
			}
		}
		cout << "Case #" << t << ": " << N*j << endl;
	}
	return 0;
}