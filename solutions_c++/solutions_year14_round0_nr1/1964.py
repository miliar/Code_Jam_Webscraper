#include <iostream>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int tt = 1; tt <= t; tt++){
		int result = 0;
		int card;
		int n, m;
		cin >> n;
		int a[5][5], b[5][5];
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				cin >> a[i][j];
			}
		}

		cin >> m;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++)
			{
				cin >> b[i][j];
			}
		}

		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				if (a[n -1][i] == b[m - 1][j]){
					result++;
					card = a[n-1][i];
					break;
				}
			}
		}

		cout << "Case #" << tt << ": ";
		if (result == 0){
			cout << "Volunteer cheated!" << endl;
		}
		else if (result == 1){
			cout << card << endl;
		}
		else{
			cout << "Bad magician!" << endl;
		}
	}
	return 0;
}