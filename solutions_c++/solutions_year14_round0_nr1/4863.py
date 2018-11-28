#include <iostream>
using namespace std;

#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define REP(I,N) for(int I=0;I<(N);I++)

int main(){
	int T;
	cin >> T;

	REP(i,T){
		int A,c;
		int pos[20];
		FOR(j,1,16) pos[j] = 0;

		cin >> A;

		REP(x,4)
			REP(y,4){
				cin >> c;
				if(x+1==A) pos[c]++;
			}

		cin >> A;

		REP(x,4)
			REP(y,4){
				cin >> c;
				if(x+1==A) pos[c]++;
			}

		int guess;
		int cou = 0;

		FOR(j,1,16){
			cou += (pos[j]==2);
			if(pos[j]==2) guess = j;
		}

		cout << "Case #" << (i+1) << ": ";

		if(cou==0) cout << "Volunteer cheated!\n";
		else
			if(cou>1) cout << "Bad magician!\n";
			else
				cout << guess << endl;
	}	

	return 0;
}
