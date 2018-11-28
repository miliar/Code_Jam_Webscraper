#include <iostream>
#include <stdio.h>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <string.h>
#include <functional>
#include <iomanip>
#include <fstream>

using namespace std;

int main(){
	ifstream fin("input.in");
	ofstream fout("output.out");
	int T; fin >> T;
	for (int Z = 0; Z < T; Z++)
	{
		int D; fin >> D;
		vector<int> p(D);
		int mx = 0;
		for (int i = 0; i < D; i++)
		{
			fin >> p[i];
			mx = max(mx, p[i]);
		}
		int ans = mx;
		for (int i = 1; i <= mx; i++)
		{
			int sp = 0;
			int mm = 0;
			for (int j = 0; j < D; j++)
			{
				if (p[j] > i){
					int pl = p[j] / i;
					if (p[j] % i != 0)
						pl++;
					pl--;
					sp += pl;
				}
				mm = max(mm, p[j]);
			}
			ans = min(ans, min(sp + i, mm));
		}
		fout << "Case #" << Z + 1 << ": " << ans << endl;
	}
	return 0;
}