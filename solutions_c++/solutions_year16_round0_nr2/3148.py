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
string pancakes;

int solve(int end, char sign) {
	if (end<0) return 0;
	int ind = end;
	while (ind>=0 && pancakes[ind]==sign) ind--;
	if (ind<0) return 0;
	if (ind<end) return solve(ind, sign);
	while (ind>=0 && pancakes[ind]!=sign) ind--;
	if (ind<0) return 1;
	return 2 + solve(ind, sign);
}

int main()
{
    fstream fin("B-large.in",ifstream::in);
    fstream fout("B-large.out",ofstream::out);
    fin >> T;
	for(int tc=1;tc<=T;tc++)
    {
		fin >> pancakes;
		fout << "Case #" << tc << ": " << solve(pancakes.size()-1, '+') << "\n";
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC << "\n";
    //system("PAUSE");
    return 0;
}
