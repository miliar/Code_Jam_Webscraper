#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int T, row, count, hit;
	int A[4][4];
	int cand[4];
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		count = 0;
		cin >> row;
		for (int k = 0; k < 4; ++k)	for (int j = 0; j < 4; ++j) cin >> A[k][j];
		for (int k = 0; k < 4; ++k)
		{
			cand[k] = A[row-1][k];
		}
		cin >> row;
		for (int k = 0; k < 4; ++k)	for (int j = 0; j < 4; ++j) cin >> A[k][j];
		for (int k = 0; k < 4; ++k)
		{
			for (int l = 0; l < 4; ++l)
			{
				if(cand[l] == A[row-1][k]){
					count++;
					hit = cand[l];
				}
			}
		}
		cout << "Case #" << i+1 << ": ";
		if(count==0) cout << "Volunteer cheated!\n";
		else if(count==1) cout << hit << endl;
		else cout << "Bad magician!\n";

	}
	return 0;
}