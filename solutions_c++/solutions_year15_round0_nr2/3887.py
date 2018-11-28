// main.cpp

#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <bitset>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <vector>
#include <numeric>
#include <complex>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <utility>

#define i64 long long
#define ui64 unsigned long long

using namespace std;

#define READ_IN_FILE 1

#ifdef ONLINE_JUDGE
#define READ_IN_FILE 0
#endif

//vector<int> vi;
vector<string> si;

double solve()
{
	return 0;
}

int main()
{
	if (READ_IN_FILE) freopen("in.in", "r", stdin);
	
	int T;
	scanf("%d\n", &T);
	if (!T) {
		cerr << "Check input!" << endl;
		exit(0);
	}
	vector<int> vi0;
	
	for (int t = 1; t <= T; t++) {
		vi0.clear();
		int D = 0;
		scanf("%d", &D);
		if (D == 0) break;
		
		for (int di = 0; di < D; di++) {
			int p;
			scanf("%d ", &p);
			vi0.push_back(p);
		}
		
		int eneed = -1;
		for (int sec = 0; sec <= 1; sec++) {
			vector<int> vi(vi0);
			int need = -1, large = 0, di = 0;
			if ((*max_element(vi.begin(), vi.end())) < 9) sec++;
			
			while (1) {
				int maxIndex = (int)(max_element(vi.begin(), vi.end()) - vi.begin());
				int max = vi[maxIndex];
				if (need == -1) need = max;
				if (max % 2 == 0) {
					max = max / 2;
					vi.push_back(max);
				} else if (max == 9) {
					if (!sec) {
						max = 6;
						vi.push_back(3);
					} else {
						max = max / 2;
						vi.push_back(max);
						max++;
					}
				} else {
					max = max / 2;
					vi.push_back(max);
					max++;
				}
				di++;
				vi[maxIndex] = max;
				max = *max_element(vi.begin(), vi.end());
				max += di;
				if (max > need) {
					large++;
					if (large > 100) break;
				} else {
					need = max;
				}
			}
			if (eneed == -1) eneed = need;
			if (need < eneed) eneed = need;
		}
		
		printf("Case #%d: %d\n", t, eneed);
	}
	
	if (READ_IN_FILE) fclose(stdin);
	return 0;
}
