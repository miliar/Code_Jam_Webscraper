/* Dan Mitton

*/
#define _CRT_SECURE_NO_DEPRECATE
#define toDigit(c) (c-'0')
#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <fstream>

using namespace std;
typedef long long ll;
typedef long double ld;


int cases; int n;
int main()
{
	//freopen("testA.txt", "rt", stdin);
	
	//freopen("out1.txt", "wt", stdout);
	//cin >> n;
	//cout << n;
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp = fopen(infile, "r"); //*ofp = freopen(outfile, "wt", stdout);
	ofstream outFile;
	outFile.open(outfile);
//	cout << infile;
	fscanf(fp, "%d", &cases);

	for (int i = 0; i < cases; i++) {
		int number;
		fscanf(fp, "%d", &number);

		if (number == 0) {
			outFile << ("Case #" + to_string(i + 1) + ": INSOMNIA\n");
			continue;
		}
		bool foundAll = false;
		int count = 1;
		int value = 0;
		vector<bool> numBools;
		for (int m = 0; m < 10; m++) {
			numBools.push_back(false);
		}

		while (!foundAll) {
			value = number * count;
			
			string s = to_string(value);

			for (int k = 0; k < s.size(); k++) {
				numBools.at(toDigit(s.at(k))) = true;
			}

			bool allTrue = true;
			for (int j = 0; j < numBools.size(); j++) {
				if (!numBools.at(j))
				{
					allTrue = false;
					break;
				}
			}
			if (allTrue) {
				foundAll = true;
			}
			count++;
		}

		outFile << ("Case #" + to_string(i+1) + ": " + to_string(value) + "\n");

	}



//	std::cout << n;
//	std::cout << "hi";

//	std::cout << "Press ENTER to continue...";
	//std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
//	system("pause");

	return 0;
}
