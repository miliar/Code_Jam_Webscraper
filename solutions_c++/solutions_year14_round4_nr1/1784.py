#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <cstdio>
using namespace std;

const string inp = "a.in", oup = "a.out";

int main()
{
	ifstream inf(inp.c_str());
	ofstream ouf(oup.c_str());
	
	int T;
	inf >> T;
	
	int a[10000];
	bool v[10000];
	
	for (int time = 0; time < T; ++time) {
		ouf << "Case #" << time + 1 << ": ";

		int N, X;
		inf >> N >> X;

		for (int i = 0; i < N; ++i) {
			inf >> a[i];
			v[i] = false;
		}
		
		sort(a, a + N);
		
		int count = 0;
		for (int i = 0; i < N; ++i)
			if (!v[i]) {
				for (int j = N - 1; j > i; --j)
					if (!v[j] && a[i] + a[j] <= X) {
						v[j] = true;
						break;
					}
				++count;
			}

		ouf << count << endl;
 	}
	return 0;
}