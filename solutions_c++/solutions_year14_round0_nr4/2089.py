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
int N;

int playWar(vector<double> Naomi, vector<double> Ken) {
	int ret = 0;
	sort(Naomi.begin(), Naomi.end());
	sort(Ken.begin(), Ken.end());
	vector<int> usedN(Naomi.size(), 0);
	vector<int> usedK(Ken.size(), 0);
	for(int i=0;i<Naomi.size();++i) {
		usedN[i] = 1;
		bool fl = 0;
		for(int j=0;j<Ken.size();++j) {
			if (usedK[j]==0 && Ken[j]>Naomi[i]) {
				usedK[j] = 1;
				fl = 1;
				break;
			}
		}
		if (!fl) {
			int ind = 0;
			while (usedK[ind]) ind++;
			usedK[ind] = 1;
			ret++;
		}
	}
	return ret;
}

int playDeceitfulWar(vector<double> Naomi, vector<double> Ken) {
	int ret = 0;
	sort(Naomi.begin(), Naomi.end());
	sort(Ken.begin(), Ken.end());
	vector<int> usedN(Naomi.size(), 0);
	vector<int> usedK(Ken.size(), 0);
	int nmin = 0, nmax = Naomi.size()-1;
	int kmin = 0, kmax = Ken.size()-1;
	for(int i=0;i<Naomi.size();++i) {
		//double kminv = -1.;
		for(int i=0;i<Ken.size();++i)
			if (usedK[i]==0) { kmin = i; break; }
		bool fl = 0;
		int nind = -1;
		for(int i=0;i<Naomi.size();++i)
			if (usedN[i]==0 && Naomi[i]>Ken[kmin]) { nind = i; break; }
		if (nind!=-1) {
			usedK[kmin] = 1;
			usedN[nind] = 1;
			ret++;
		}
		else {
			for(int i=0;i<Naomi.size();++i)
				if (usedN[i]==0) { nind = i; break; }
			for(int i=Ken.size()-1;i>=0;--i)
				if (usedK[i]==0) { kmin = i; break; }
			usedK[kmin] = 1;
			usedN[nind] = 1;
		}
	}
	return ret;
}

int main()
{
    fstream fin("D-large.in",ifstream::in);
    fstream fout("D-large.out",ofstream::out);
    fin >> T;
	for(int tc=1;tc<=T;tc++)
    {
        fin >> N;
		cout << tc << " " << N << "\n";
		vector<double> blN(N), blK(N);
		rep(i,N) fin >> blN[i];
		rep(i,N) fin >> blK[i];
		fout << "Case #" << tc << ": " << playDeceitfulWar(blN, blK) << " " << playWar(blN, blK) << "\n";
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC << "\n";
    system("PAUSE");
    return 0;
}
