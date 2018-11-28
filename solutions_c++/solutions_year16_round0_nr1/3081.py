#include <cstdio>
#include <iostream>
#include <fstream>
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
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;

int T;

long long solve(long long N) {
	if (N==0) return -1;
	long long ret = N;
	int digi[10];
	for(int i=0;i<10;++i) digi[i] = 0;
	int digcount = 0;
	while(1) {
		long long tmp = ret;
		while (tmp>0) {
			int tmpi = tmp%10;
			if (digi[tmpi]==0) {
				digcount++;
				digi[tmpi] = 1;
			}
			tmp /= 10;
		}
		if (digcount==10) break;
		ret += N;
	}
	return ret;
}

int main()
{
    fstream fin("A-large.in",ifstream::in);
    fstream fout("A-large.out",ofstream::out);
    fin >> T;
	for(int tc=1;tc<=T;tc++)
    {
        long long N;
		fin >> N;
		long long ret = solve(N);
		if (ret<0) fout << "Case #" << tc << ": " << "INSOMNIA" << "\n";
		else fout << "Case #" << tc << ": " << ret << "\n";
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC << "\n";
    //system("PAUSE");
    return 0;
}
