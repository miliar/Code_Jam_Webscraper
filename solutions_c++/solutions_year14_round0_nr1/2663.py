#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int t;
	scanf("%d", &t);
	for (int k = 1; k <= t; k++) {
		int n, m;
		int a[4][4], b[4][4];
		scanf("%d", &n);
		for (int i = 0; i < 4; i++) 
			for (int j = 0; j < 4; j++)
				scanf("%d", &a[i][j]);
		scanf("%d", &m);
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				scanf("%d", &b[i][j]);

		int frqa[17] = {}, frqb[17] = {};
		for (int i = 0; i < 4; i++)
			frqa[a[n - 1][i]]++;
		for (int i = 0; i < 4; i++)
			frqb[b[m - 1][i]]++;
		int flag = 0, element = 0;
		for (int i = 1; i < 17; i++) {
			if (frqa[i] == 1 && frqb[i] == 1) {
				if (flag == 0)
					flag = 1;
				else 
					flag = 2;
				element = i;
			}
		}

		cout << "Case #" << k << ": " ;
		if (flag == 0)
			cout << "Volunteer cheated!";
		else if (flag == 1)
			cout << element;
		else if (flag == 2)
			cout << "Bad magician!";
		cout << endl;
	}
}

