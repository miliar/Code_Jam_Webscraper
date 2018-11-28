// cards.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include "windows.h"
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	//Sleep(10*1000);
	int t = 0;
	cin >> t;
	for (auto i = 0; i < t; ++i) {
		int first = 0;
		cin >> first;
		int fa[4][4];
		for (auto j = 0; j < 4; ++j) for (auto k = 0; k < 4; ++k)
			cin >> fa[j][k];

		int second = 0;
		cin >> second;
		int sa[4][4];
		for (auto j = 0; j < 4; ++j) for (auto k = 0; k < 4; ++k)
			cin >> sa[j][k];

		int found = -1;
		bool out = false;
		for (int f = 0; f < 4; ++f) {
			for (int s = 0; s < 4; ++s) {
				if (fa[first-1][f] == sa[second-1][s]) {
					if (found != -1) {
						out = true;
						break;
					}
					found = fa[first-1][f];
				}
					
			}
			if (out) break;
		}
		cout << "Case #" << i+1 <<": ";
		if (out) {
			cout << "Bad magician!" << endl;
		} else if (-1 == found) {
			cout << "Volunteer cheated!" << endl;
		} else
			cout << found << endl;

	}
	return 0;
}

