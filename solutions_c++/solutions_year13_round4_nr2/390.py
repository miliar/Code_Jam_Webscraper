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
long long N, P;


int main()
{
    fstream fin("B-large.in",ifstream::in);
    fstream fout("B-large.out",ofstream::out);
    fin >> T;
	for(int tc=1;tc<=T;tc++)
    {
		fin >> N >> P;
		long long ret1 = 0, ret2 = 0;
		long long cst = 1, told = 1;
		if (P==1) ret1 = 0;
		else
		{
			rep(i,N)
			{
				cst += (1ll << N-i-1);
				/*if (i==N-1)
				{
					ret1 = (1ll << N) - 1;
					break;
				}*/
				if (P<cst)
				{
					ret1 = (1ll << (i+1)) - 2;
					break;
				}
				if (i==N-1)
				{
					ret1 = (1ll << N) - 1;
					break;
				}
			}
		}
		cst = 1;
		long long cst2 = 0;
		if (P==(1ll << N)) ret2 = (1ll <<N) - 1;
		else
		{
			rep(i,N)
			{
				//cst = 1ll << (i+1);
				cst += (1ll << N-i-1);
				cst2 = (1ll << N) - cst + 1;
				if (P>=cst2)
				{
					ret2 = (1ll << N) - (1ll << (i+1));//(1ll << (i+1)) - 2;
					break;
				}
				if (i==N-1)
				{
					ret2 = 0;
					break;
				}
			}
		}
		fout << "Case #" << tc << ": " << ret1 << " " << ret2 << "\n";
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC << "\n";
    //system("PAUSE");
    return 0;
}
