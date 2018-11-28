//============================================================================
// Name        : codejam.cpp
// Author      : Abhidnya
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================


#include <iostream>
#include <stdio.h>

using namespace std;


int sumofp(int *p, int n)
{
	int tot = 0;
	for (int i = 0; i < n; i++)
		tot += p[i];
	return tot;
}

int findindex(int *p, int n, int index)
{
	int no = 0, ind = 0, temp;
	switch (index) {
		case 1:
		for(int i = 0; i < n; i++) {
			if (p[i] > no) {
				no = p[i];
				ind = i;
			}
		}
		return ind;
		case 2:
		for(int i = 0; i < n; i++) {
			if (p[i] > no) {
				no = p[i];
				ind = i;
			}
		}
		temp = p[ind];
		p[ind] = 0;
		for(int i = 0; i < n; i++) {
			if (p[i] > no) {
				no = p[i];
				ind = i;
			}
		}
		p[ind] = temp;
		return ind;
	}
}


void pri(int *p, int n)
{
	for (int i = 0; i < n; i++)
		printf("%d", p[i]);
	printf("\n\n");
}

int main()
{
	freopen("b.in", "rt", stdin);
	freopen("b.out", "wt", stdout);
	int no, n;
	int i, j, k;
	cin >> no;
	int p[26];
	int sum = 0, index = 0;
	for (i = 0; i < no; i++) {
		cin >> n;
		for (j = 0; j < n; j++) {
			cin >> p[j];
		}
		//cout << endl;
		cout << "Case #" << i + 1 << ":";
		while (1) {
			sum = sumofp(p, n);
			if (sum == 0) {
				cout << endl;
				break;
			}
			//cout  << sm << endl;
			index = findindex(p, n, 1);
			if (sum == 3) {
				p[index] -= 1;
				cout << " " << char(index + 65);
				continue;
			}
			if ((p[index] - 1) > ((sum - 2)/2)) {
				p[index] -= 2;
				cout << " " << char(index + 65) << char(index + 65);
			} else {
				p[index]--;
				cout << " " << char(index + 65);
				index = findindex(p, n, 2);
				p[index]--;
				cout << char(index + 65);
			}
		}
	}
	return 0;
}
