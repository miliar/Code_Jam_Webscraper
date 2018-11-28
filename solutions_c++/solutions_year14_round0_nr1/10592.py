#include <iostream>
#include <conio.h>
#include <math.h>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <conio.h>

#define PI acos(-1.0)
#define EPS 0.0001
#define For(i, a, b) for( int i = (a); i < (b); i++ )

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

int t, tmp;
int arr_f[4], arr_s[4];

int main() {
	cin >> t;

	for (int  c = 0; c < t; c++) {
		int first;
		cin >> first;
		--first;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (i <= first)
					cin >> arr_f[j];
				else 
					cin >> tmp;
			}
		}
		int second;
		cin >> second;
		--second;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (i <= second)
					cin >> arr_s[j];
				else 
					cin >> tmp;
			}
		}
	int count = 0, val = 0;	
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (arr_f[i] == arr_s[j]) {
				count++;
				val = arr_f[i];
			}
		}
	}
	cout << "Case #" << c+1 << ": ";
	if (count == 1) {
		cout << val << endl;
	}

	else if (count > 1) {
		cout << "Bad magician!" << endl;
	}

	else {
		cout << "Volunteer cheated!" << endl;
	}
	}


	//_getch();
	return 0;
}