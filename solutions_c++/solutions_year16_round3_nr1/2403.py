#include <iostream>
#include <stdio.h>

using namespace std;


int sum_a(int *a, int n)
{
	int tot = 0;
	for (int i = 0; i < n; i++)
		tot += a[i];
	return tot;
}

int find_index(int *a, int n, int index)
{
	int no = 0, ind = 0, temp;
	switch (index) {
		case 1:
		for(int i = 0; i < n; i++) {
			if (a[i] > no) {
				no = a[i];
				ind = i;
			}
		}
		return ind;
		case 2:
		for(int i = 0; i < n; i++) {
			if (a[i] > no) {
				no = a[i];
				ind = i;
			}
		}
		temp = a[ind];
		a[ind] = 0;
		for(int i = 0; i < n; i++) {
			if (a[i] > no) {
				no = a[i];
				ind = i;
			}
		}
		a[ind] = temp;
		return ind;
	}
}


void dump(int *a, int n)
{
	for (int i = 0; i < n; i++)
		printf("%d", a[i]);
	printf("\n\n");
}

int main()
{
	freopen("1.in", "rt", stdin);
	freopen("1.out", "wt", stdout);
	int t, n;
	int i, j, k;
	cin >> t;
	int a[26];
	int sm = 0, index = 0;
	for (i = 0; i < t; i++) {
		cin >> n;
		for (j = 0; j < n; j++) {
			cin >> a[j];
			//cout << a[j];
		}
		//cout << endl;
		cout << "Case #" << i + 1 << ":";
		while (1) {
			sm = sum_a(a, n);
			if (sm == 0) {
				cout << endl;
				break;
			}
			//cout  << sm << endl;
			index = find_index(a, n, 1);
			if (sm == 3) {
				a[index] -= 1;
				cout << " " << char(index + 65);
				continue;
			}
			if ((a[index] - 1) > ((sm - 2)/2)) {
				a[index] -= 2;
				cout << " " << char(index + 65) << char(index + 65);
			} else {
				a[index]--;
				cout << " " << char(index + 65);
				index = find_index(a, n, 2);
				a[index]--;
				cout << char(index + 65);
			}
		}
	}
	return 0;
}
