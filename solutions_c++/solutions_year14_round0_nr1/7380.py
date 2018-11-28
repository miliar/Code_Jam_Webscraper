#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int arr1[4][4];
	int arr2[4][4];

	int t;
	cin >> t;

	int i, j;
	int ans1, ans2;
	
	int t_ctr = 1;
	
	while ( t-- ) {
		
		cin >> ans1;
		for ( i =0; i < 4; i++ ) {
			for ( j = 0; j < 4; j++ ) {
				cin >> arr1[i][j];
			}
		}
		
		cin >> ans2;
			
		for ( i =0; i < 4; i++ ) {
			for ( j = 0; j < 4; j++ ) {
				cin >> arr2[i][j];
			}
		}


		int sol;
		int ctr = 0;
		for ( i = 0; i < 4; i++ ) {
			for ( j = 0; j < 4; j++ ) {
				if ( arr1[ans1 - 1][i] == arr2[ans2 - 1][j] ) {
					ctr++;
					sol = arr1[ans1 - 1][i];
				}
			}
		}

		if ( ctr == 0 ) {
			cout << "Case #"<< t_ctr << ": Volunteer cheated!" << endl;
		} else if ( ctr == 1 ) {
			cout << "Case #"<< t_ctr << ": " << sol << endl;

		} else if ( ctr > 1 ) {
			cout << "Case #"<< t_ctr << ": Bad magician!" << endl;
		}

		t_ctr++;
		
	}
	
	return 0;

}
