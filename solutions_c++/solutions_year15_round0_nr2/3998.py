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

int pn[1010]; 

int ans = 0; 

void f(vector<int> &v, int minutes) {
	if (minutes >= ans) return;

	sort(v.begin(), v.end()); 

	if (minutes + v.back() < ans)
		ans = minutes + v.back();
	
	int t = v.back();
	if (t == 1) return;

	for (int i = 1; i <= (t / 2); i++) {
		vector<int> bv = v; 
		bv.back() = (t - i); 
		/*
		for (int j = 0; j < (bv.size() - 1); j++) {
			if (bv[j] + i >= t) continue;

			bv[j] += i;
			f(bv, minutes + 1); 
			bv[j] -= i; 
		}
		*/
		
		bv.push_back(i); 
		f(bv, minutes + 1); 
	}
}

int main(int argc, char* argv[]) {
	ifstream inf(argv[1]);

	int TC = 0;
	inf >> TC;
	for (int tc = 1; tc <= TC; tc++) {
		/*
		int d; 
		inf >> d; 
		vector<int> dinners(d); 
		memset(pn, 0, sizeof(pn));

		for (int i = 0; i < d; i++) {
			inf >> dinners[i];
			pn[dinners[i]]++;
		}

		sort(dinners.begin(), dinners.end());
		
		int ans = dinners.back();
		
		int change = 0; 
		for (int i = 1000; i > 0; i--) {
			if (pn[i] > 0) {
				int mp = 1;
				if (i > 1) {
					change += pn[i];
					int p1 = i / 2;
					int p2 = i - p1;
					pn[p1] += pn[i];
					pn[p2] += pn[i];

					for (int j = i - 1; j > 0; j--) {
						if (pn[j] > 0) {
							mp = j;
							break;
						}
					}
				}
				if (change + mp < ans)
					ans = change + mp;
			}
		}
		*/
		ans = 0x7fffffff;
		int d;
		inf >> d;
		vector<int> dinners(d);

		for (int i = 0; i < d; i++) {
			inf >> dinners[i];
		}

		f(dinners, 0); 

		cout << "Case #" << tc << ": " << ans << endl;
		


	}

	return 0;
}