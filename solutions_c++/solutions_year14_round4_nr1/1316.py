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

int N, X;
vector<int> S;

int main()
{
    fstream fin("A-large.in",ifstream::in);
    fstream fout("A-large.out",ofstream::out);
    fin >> T;
	for(int tc=1;tc<=T;tc++)
    {
		fin >> N >> X;
		S.resize(N);
		rep(i,N) fin >> S[i]; 
		{
			sort(S.begin(), S.end());
			vector<int> used(N, 0);
			rep(i,N) used[i] = 0;
			bool fl = 1;
			int ret = 0;
			int mai = N - 1;
			while (1) {
				//int mai = N;
				/*for(int i=N-1;i>=0;i--)
					if (used[i]==0) { mai = i; break; }*/
				while (mai>=0 && used[mai]) mai--;
				if (mai<0) break;
				used[mai] = 1;
				//int mai2 = N;
				for(int i=mai-1;i>=0;i--)
					if (used[i]==0 && (S[i] + S[mai]<=X)) { used[i] = 1; break; }
				ret++;
			}
			cout << "Case #" << tc << ": " << ret << "\n";
			fout << "Case #" << tc << ": " << ret << "\n";
		}
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC << "\n";
    system("PAUSE");
    return 0;
}
