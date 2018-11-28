#define _CRT_SECURE_NO_WARNINGS
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
	//freopen("C:\\Users\\Lubo\\SkyDrive\\Programming\\C++\\Default Projects\\Competitive Programming (VS13)\\Files\\output.txt", "w", stdout);
	//freopen("C:\\Users\\Lubo\\SkyDrive\\Programming\\C++\\Default Projects\\Competitive Programming (VS13)\\Files\\input.txt", "r", stdin);
	ios_base::sync_with_stdio(false);

	int cases = 0, num = 1;
	cin >> cases;

	while (cases--) {
		double C, F, X, result = 0, perS = 2, curC = 0;
		cin >> C >> F >> X;

		while (C / perS + X / (perS + F) < X / perS) {
			result += C / perS;
			perS += F;
		}

		result += X / perS;

		cout << "Case #" << num << ": " << setprecision(6) << fixed << result << "\n";

		num++;
	}

	return 0;
}