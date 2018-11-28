#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <math.h>
#include <limits>
#include <queue>
#include <string.h>

using namespace std;

typedef long long ll;
#define MOD 1000000007

int poss[17];

void getPossible(istream& inStream, int row) {
	int val;
	for (int count = 1; count < 17; count++) {
		inStream >> val;
		if ((row * 4 - 3) <= count && count <= (row * 4)) {
			poss[val]++;
		}
	}
}

void func(istream& inStream,ofstream& outStream) {
	int t, first, second;
	inStream >> t;
	for (int test = 0; test < t; test++) {

		memset(poss, 0, 17 * sizeof(int));

		inStream >> first;
		getPossible(inStream, first);
		inStream >> second;
		getPossible(inStream, second);

		int count_2 = 0;
		int value = 0;
		for (int i = 1; i < 17; i++) {
			if (poss[i] == 2) {
				count_2++;
				value = i;
			}
		}
		outStream << "Case #" << (test + 1) << ": ";
		switch (count_2) {
		case 0:
			outStream << "Volunteer cheated!";
			break;
		case 1:
			outStream << value;
			break;
		default:
			outStream << "Bad magician!";
			break;
		}
		outStream << endl;
	}
}

int main() {
	ifstream fileInStream("A-small-attempt2.in");
//	ifstream fileInStream("input.txt");
	istream& inStream = (fileInStream == false) ? cin : fileInStream;
	ofstream outStream("output.txt");
	func(inStream,outStream);
	return 0;
}
