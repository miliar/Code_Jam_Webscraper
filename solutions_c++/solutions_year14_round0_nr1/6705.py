//#define _CRT_SECURE_NO_WARNINGS
using namespace std;

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <fstream>
#include <ctime>
#include <cstdlib>
#include <cstdio>
#include <iomanip>
#include <sstream>

#include <map>
#include <list>
#include <set>
#include <climits>
#include <queue>
#include <array>

//#include <cstring>
//#include <conio.h>
//#include "Large Numbers.h"
//#include "Primes.h"

typedef unsigned long long int ull;

#define SORT(Array)						sort(Array.begin(), Array.end())									// sorting an STL containers
#define REVERSE(Array)					reverse(Array.begin(), Array.end())									// reversing an STL containers
#define FOR(variable, condition)		for(int variable = 0; variable < condition; ++variable)				// loop from 0 to 'condition'
#define rep(variable, start, condition)	for(int variable = strart, valiable < condition, ++variable)		// loop from 'start' to 'condition'
#define FORA(variable, Array)			for(auto &member : Array)											// loop trough all the elements of an array
#define FORIN(Array)					for(auto &member : Array) { cin >> member; }						// loop, getting user input for all the elements of a 1D array
#define VIN(name, len)					vector<double> name(len); FORIN(name);								// declares a vector and get's user input for it's values
#define FOROUT(Array)					for(auto member : Array) { cout << member << " "; } cout << endl;	// loop, outputting all elements of a 1D array

int main() {
	//ifstream cin; cin.open("C:\\Users\\Lubo\\SkyDrive\\Programming\\C++\\Default Projects\\Competitive Programming (VS13)\\Files\\input.txt");
	ios_base::sync_with_stdio(false);
	//ofstream cout; cout.open("C:\\Users\\Lubo\\SkyDrive\\Programming\\C++\\Default Projects\\Competitive Programming (VS13)\\Files\\output.txt");

	int cases = 0, num = 1;
	cin >> cases;

	while (cases--) {
		int answer1, answer2, res = 0, ans;
		cin >> answer1;
		vector<vector<int>> cards1(4, vector<int>(4)), cards2(4, vector<int>(4));

		FOR(i, 4) {
			FOR(j, 4) {
				cin >> cards1[i][j];
			}
		}

		cin >> answer2;

		FOR(i, 4) {
			FOR(j, 4) {
				cin >> cards2[i][j];
			}
		}

		FOR(i, 4) {
			FOR(j, 4) {
				if (cards2[answer2 - 1][j] == cards1[answer1 - 1][i]) {
					res++;

					if (res > 1) {
						i = 4;
						break;
					}

					ans = cards1[answer1 - 1][i];
				}
			}
		}

		cout << "Case #" << num << ": ";

		if (res == 1) {
			cout << ans << "\n";
		} else if (res > 1) {
			cout << "Bad magician!\n";
		} else if (!res) {
			cout << "Volunteer cheated!\n";
		}

		num++;
	}

	return 0;
}