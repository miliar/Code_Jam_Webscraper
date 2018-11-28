#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
//#include <utility>
//#include <set>
//#include <map>
//#include <queue>
#include <iomanip>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vint;
//typedef vector<string> vstr;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

int main()
{
	int tcase = 0;
	ifstream fin("../B-large.in");
	ofstream fout("z.out");
	fin >> tcase;
	for (int tind = 1; tind <= tcase; tind++)
	{
		int i,j, n;
		//istringstream strin();
		vector<int> a;
		fin >> n;
		for (i = 0; i < n; i++) {
            fin >> j;
            a.push_back(j);
		}
		int ans = 0;
		while (a.size() > 1) {
            j = a.size() - 1;
            for (i = j - 1; i >= 0; i--)
                if (a[i] < a[j]) j = i;
            int s = a.size();
            ans += min(j, s-1-j);
            for (i = j+1; i < s; i++) a[i-1] = a[i];
            a.pop_back();
		}
		fout << "Case #" << tind << ": " << ans << endl;
	}
	return 0;
}
