// A.cpp: определяет точку входа для консольного приложения.
//
#include "stdafx.h"
#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream cin("A-small-attempt0.in");
	ofstream cout("outA.txt");
	int T,t = 0;
	vector<vector<int>> a(4, { 0, 0, 0, 0 }), b(4, { 0, 0, 0, 0 });
	cin >> T;
	while (t != T){
		++t;
		cout << "Case #" << t << ": ";
		int k1, k2;
		cin >> k1;
		k1--;
		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			cin >> a[i][j];
		cin >> k2;
		k2--;
		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			cin >> b[i][j];
		int k = 0;
		int ans = 0;
		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
		if (a[k1][i] == b[k2][j]) {
			k++;
			ans = i;
		}
		if (k == 0) cout << "Volunteer cheated!";
		else if (k == 1) cout << a[k1][ans];
		else cout << "Bad magician!";
		cout << endl;
	}
	return 0;
}

