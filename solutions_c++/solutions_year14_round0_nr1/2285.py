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

int main()
{
    fstream fin("A-small-attempt0.in",ifstream::in);
    fstream fout("A-small-attempt0.out",ofstream::out);
    fin >> T;
	for(int tc=1;tc<=T;tc++)
    {
        int arr[16];
		rep(i,16) arr[i] = 0;
		int rnum = 0, crow = 0;
		int tmp = 0;
		rep(k,2) {
			fin >> rnum;
			crow = 0;
			rep(i,4) {
				crow++;
				rep(j,4)
					{ 
						fin >> tmp;
						if (crow==rnum) arr[tmp-1]++;
					}
			}
		}
		int lcrd = -1, tcnt = 0;
		rep(i,16) if (arr[i]==2) { lcrd = i+1; tcnt++; }
		if (tcnt==1) fout << "Case #" << tc << ": " << lcrd << "\n";
		else if (tcnt>1) fout << "Case #" << tc << ": " << "Bad magician!" << "\n";
		else fout << "Case #" << tc << ": " << "Volunteer cheated!" << "\n";
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC << "\n";
    system("PAUSE");
    return 0;
}
