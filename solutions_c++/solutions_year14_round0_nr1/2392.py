#include <iostream>
#include <algorithm>
using namespace std;

const int N = 4;
int ar1[4][4], ar2[4][4];
int num[16];

inline int solve()
{
	int a1, a2;
	cin >> a1;
	--a1;
	for(int i=0; i<4; ++i)
		for(int j=0; j<4; ++j) {
			cin >> ar1[i][j];
			--ar1[i][j];
		}
	cin >> a2;
	--a2;
	for(int i=0; i<4; ++i)
		for(int j=0; j<4; ++j) {
			cin >> ar2[i][j];
			--ar2[i][j];
		}

	fill_n(num, 16, 0);
	for(int j=0; j<4; ++j) {
		num[ar1[a1][j]]++;
		num[ar2[a2][j]]++;
	}

	int ret = -1;
	for(int i=0; i<16; ++i)
		if(num[i]==2)
			if(ret==-1)
				ret = i;
			else
				return -2;
	return ret;
}

int main()
{
	int nt;
	cin >> nt;
	for(int i=1; i<=nt; ++i) {
		int x = solve();
		cout << "Case #" << i << ": ";
		if(x==-2)
			cout << "Bad magician!" << endl;
		else if(x==-1)
			cout << "Volunteer cheated!" << endl;
		else
			cout << x+1 << endl;
	}

	return 0;
}
