#include <iostream>
#include <cstdlib>

#define forn(i,n) for(int i = 0; i < (int)(n); i++)
#define forn1(i,n) for(int i = 1; i <= (int)(n); i++)

using namespace std;

int main()
{
	int test;
	int a1, a2;
	int first[8][8];
	int second[8][8];
	bool can[30];
	int pos, card;

	cin >> test;

	forn(t,test){
		
		forn(i,20) can[i] = false;

		pos = 0;

		cin >> a1;
		forn(i,4){
			forn(j,4){
				cin >> first[i][j];
			}
		}
		cin >> a2;
		forn(i,4){
			forn(j,4){
				cin >> second[i][j];
			}
		}
		a1--; a2--;

		forn(i,4){
			can[ first[a1][i] ] = true;
		}
		//forn(i,17) cout << can[i] << " ";
		//cout << endl;
		forn(i,4){
			//cout << can[ second[a2][i] ] << endl;
			if(can[ second[a2][i] ]){ pos++; card = second[a2][i]; }
		}

		cout << "Case #" << (t+1) << ": ";
	
		if(pos == 0){
			cout << "Volunteer cheated!" << endl;
		}
		if(pos == 1){
			cout << card << endl;
		}
		if(pos >= 2){
			cout << "Bad magician!" << endl;
		}
	}
	return 0;
}
