#include<iostream>
using namespace std;

int t, res, fcomb[4][4], scomb[4][4], frow, srow, nboth;
bool fappear[17], sappear[17];

int main() {
	cin >> t;

	for(int TCASE = 0; TCASE < t; TCASE++) {
		for(int i=0;i<17;i++)
			fappear[i] = false, sappear[i] = false;
		
		cin >> frow;
		for(int i=0;i<4;i++)
			for(int j=0; j<4; j++)
				cin >> fcomb[i][j];
		
		cin >> srow;
		for(int i=0;i<4;i++)
			for(int j=0; j<4; j++)
				cin >> scomb[i][j];
		
		
		for(int i=0;i<4;i++)
			fappear[fcomb[frow-1][i]] = true, sappear[scomb[srow-1][i]] = true;
		
		nboth = 0;
		for(int i=0;i<17;i++) {
			fappear[i] = (fappear[i] && sappear[i]);
			if(fappear[i])
				nboth++, res = i;
		}
		
		cout << "Case #" << TCASE+1 << ": ";
		if(nboth == 0)
			cout << "Volunteer cheated!";
		else if(nboth > 1)
			cout << "Bad magician!";
		else
			cout << res;
		cout << '\n';
	}
	
	return 0;
}
