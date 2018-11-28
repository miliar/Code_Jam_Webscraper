#include <iostream>
using namespace std;

int main() 
{
	int n, firRow, secRow;
	int a[4], b[4];
	cin >> n;
	int tmp = n, tmp1, tmp2, tmp3, tmp4;
	while (n--) {
		cin >> firRow;
		for (int i = 1; i < 5; ++i)
			if (firRow != i) cin >> tmp1 >> tmp2 >> tmp3 >> tmp4;
			else cin >> a[0] >> a[1] >> a[2] >> a[3];
		cin >> secRow;
		for (int i = 1; i < 5; ++i)
			if (secRow != i) cin >> tmp1 >> tmp2 >> tmp3 >> tmp4;
			else cin >> b[0] >> b[1] >> b[2] >> b[3];
		int k = 0, res = 0;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				if (a[i] == b[j]) {
					++k;
					res = a[i];
				}
		cout << "Case #" << (tmp - n) << ": ";
		if (k == 1) cout << res;
		else if (k > 1) cout << "Bad magician!";
		else cout << "Volunteer cheated!";
		cout << endl;
	}
}