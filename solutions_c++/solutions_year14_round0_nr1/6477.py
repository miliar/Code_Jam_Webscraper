#include <iostream>
#include <set>

using namespace std;

int
main()
{
    int T;

    cin >> T;

    for (int i = 1; i <= T; ++i) {
	int a[4][4], b[4][4];
	int m, n;

	cin >> m;
	--m;

	for (int j = 0; j < 4; ++j) {
	    for (int k = 0; k < 4; ++k)
		cin >> a[j][k];
	}

	cin >> n;
	--n;
	
	for (int j = 0; j < 4; ++j) {
	    for (int k = 0; k < 4; ++k)
		cin >> b[j][k];
	}

	int hit = 0;
	int ans = -1;

	for (int j = 0; j < 4; ++j) {
	    for (int k = 0; k < 4; ++k) {
		if (a[m][j] == b[n][k]) {
		    ++hit;
		    ans = a[m][j];
		}
	    }
	}

	cout << "Case #" << i << ": ";

	if (hit == 0)
	    cout << "Volunteer cheated!" << endl;
	else if (hit == 1)
	    cout << ans << endl;
	else
	    cout << "Bad magician!" << endl;
    }

    return 0;
}
