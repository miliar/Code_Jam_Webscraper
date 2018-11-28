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

vector<int> a;

int main()
{
	int tcase = 0;
	ifstream fin("../A-large.in");
	ofstream fout("z.out");
	fin >> tcase;
	for (int tind = 1; tind <= tcase; tind++)
	{
		int i,j;
		//istringstream strin();
        int n, x;
        fin >> n >> x;
        a.clear();
        for (i = 0; i < n; i++) {
            fin >> j;
            a.push_back(j);
        }
        sort(a.begin(), a.end());
        i = 0; j = n - 1;
		int ans = 0;
		while (j >= i) {
            if (a[j] + a[i] <= x) {
                ans++;
                j--;
                i++;
            } else {
                ans++;
                j--;
            }
		}
		fout << "Case #" << tind << ": " << ans << endl;
	}
	return 0;
}
