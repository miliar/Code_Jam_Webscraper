#include <iostream>

using namespace std;

int T, num1, num2;
int d1[4][4], d2[4][4];

int main()
{
    cin >> T;
    for (int k=1; k<=T; ++k) {
	cin >> num1;
	for (int i=0; i<4; ++i)
	    for (int j=0; j<4; ++j)
		cin >> d1[i][j];
	cin >> num2;
	for (int i=0; i<4; ++i)
	    for (int j=0; j<4; ++j)
		cin >> d2[i][j];

	num1--;
	num2--;
	int cnt = 0;
	int num;
	for (int i=0; i<4; ++i)
	    for (int j=0; j<4; ++j) {
		if (d1[num1][i] == d2[num2][j]) {
		    num = d1[num1][i]; cnt++;
		}
	    }

	if (cnt == 1)
	    cout << "Case #" << k << ": " << num << endl;
	if (cnt > 1)
	    cout << "Case #" << k << ": Bad magician!" << endl;
	if (cnt == 0)
	    cout << "Case #" << k << ": Volunteer cheated!" << endl;
	    
    }
    
    return 0;
}
