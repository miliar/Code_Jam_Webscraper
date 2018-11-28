#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <assert.h>
#include <algorithm>
#include <math.h>
#include <ctime>
#include <functional>

#include <Windows.h>

using namespace std;

vector<int> pn(1010); 

int ans = 0; 

int findmax(vector<int> pnn) {
	for (int i = 1000; i > 0; i--)
		if (pnn[i] != 0)
			return i;
}

void f(int minutes, vector<int> &pnn) {
	int p = findmax(pnn);
	int n = pnn[p]; 
	if (p + minutes < ans) {
		ans = p + minutes;
	}
	if (minutes >= ans) return;

	vector<int> pb = pnn;
	pb[p] = 0; 

	for (int divide = 2; divide <= p; divide++) {
		int i1 = p / divide;
		int i2 = i1 + 1; 
		int n2 = (p - i1 * divide); 
		int n1 = divide - n2;

		
		pb[i1] += n1;
		pb[i2] += n2; 

		f(minutes + n * (divide - 1), pb); 

		pb[i1] -= n1;
		pb[i2] -= n2;
	}
}

int main(int argc, char* argv[]) {
	ifstream inf(argv[1]);

	int TC = 0;
	inf >> TC;
	for (int tc = 1; tc <= TC; tc++) {
		int d; 
		inf >> d; 
		pn.clear();
		pn.resize(1010, 0);

		for (int i = 0; i < d; i++) {
			int num = 0; 
			inf >> num;
			pn[num]++;
		}
		
		ans = 0x7fffffff;
		
		f(0, pn);

		cout << "Case #" << tc << ": " << ans << endl;
		


	}

	return 0;
}