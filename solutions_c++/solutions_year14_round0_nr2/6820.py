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

void func(istream& inStream, ofstream& outStream) {
	int t;
	inStream >> t;
	outStream.precision(7);
	for (int test = 1; test <= t; test++) {
		double c, f, x, curR = 2.0, curTime = 0.0, completeTime = 0.0,
				finishTime = 0.0, curFinishTime;
		inStream >> c >> f >> x;
		curFinishTime = x / 2.0;
		while (true) {
			curTime += c / curR;
			curR += f;
			completeTime = x / curR;
			finishTime = curTime + completeTime;
			if (finishTime > curFinishTime) {
				break;
			}
			curFinishTime = finishTime;
		}
		outStream << "Case #" << test << ": ";
		char output[128] = "";
		sprintf(output, "%.7f", curFinishTime);
		outStream << output << endl;
	}
}

int main() {
	ifstream fileInStream("B-large.in");
//	ifstream fileInStream("input.txt");
	istream& inStream = (fileInStream == false) ? cin : fileInStream;
	ofstream outStream("output.txt");
	func(inStream, outStream);
	return 0;
}
