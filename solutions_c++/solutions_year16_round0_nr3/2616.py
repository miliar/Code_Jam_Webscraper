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
int N, J;

long long findDivisor(long long num) {
	if (num<=2) return -1;
	if (num%2==0) return 2;
	for(long long a = 3; a*a <= num; a += 2) {
		if (num % a == 0) return a;
	}
	return -1;
}

int main()
{
    fstream fin("C-small-attempt0.in",ifstream::in);
    fstream fout("C-small-attempt0.out",ofstream::out);
    fin >> T;
	for(int tc=1;tc<=T;tc++)
    {
		fin >> N >> J;
		fout << "Case #" << tc << ": " << "\n";

		int cnt = 0;
		for(unsigned int d=0; d<(1<<(N-2)); d++) {
			vector<int> digi(0);

			digi.push_back(1);
			rep(i,N-2) digi.push_back((d & (1<<i))!=0);
			digi.push_back(1);
			vector<long long> divs(0), nums(0);
			for(int b=2;b<=10;++b) {
				long long tnum = 0;
				tnum += 1;
				rep(i,N-2)
					tnum = b*tnum + digi[i+1];
				tnum = b*tnum + 1;
				long long div = findDivisor(tnum);
				if (div>0) { divs.push_back(div); nums.push_back(tnum); }
				else break;
			}
			if (divs.size()==9) {
				rep(i,digi.size()) fout << digi[i] ;
				fout << " ";
				rep(i,divs.size()) fout << divs[i] << " ";
				fout << "\n";

				rep(i,digi.size()) cout << digi[i] ;
				cout << " ";
				rep(i,divs.size()) cout << nums[i] << " " << divs[i] << "  ";
				cout << "\n";

				cnt++;
				if (cnt>=J) break;
			}
		}
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC << "\n";
    //system("PAUSE");
    return 0;
}
