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
#define MOD 1000000007
#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;

int T;
int M,N;
vector<string> lines;
vector<int> grps;
unsigned long long maxret, subs;
unsigned long long curmax = 0;
unsigned long long curways = 0;
unsigned long long factorial = 0;

vector< vector<int> > same;

int getSameSub(string & A, string & B) {
	int ret = 1;
	int st = 0;
	while (st<A.size() && st<B.size() && A[st]==B[st]) { ret++; st++; }
	return ret;
}
void go(int ind) {
	if (ind<M) {
		rep(i,N) {
			grps[ind] = i;
			go(ind + 1);
		}
	}
	else {
		maxret = subs = 0;
		vector<int> cntgrp(N, 0);
		rep(i,M) {
			cntgrp[grps[i]]++;
			maxret += lines[i].size() + 1;
		}
		rep(i,N) if (cntgrp[i]==0) return;
		vector< vector<int> > subbed(M);
		rep(i,M) {
			subbed[i].resize(lines[i].size()+1);
			rep(j,subbed[i].size()) subbed[i][j] = 0;
		}
		for(int i=0;i<M-1;++i)
			for(int j=i+1;j<M;++j)
				if (grps[i]==grps[j]) {
					if (subbed[j][0]==0) { subs++; subbed[j][0] = 1; }
					for(int k=1;k<subbed[j].size();++k)
						if (subbed[j][k]==0 && lines[i].substr(0,k)==lines[j].substr(0,k)) { subs++; subbed[j][k] = 1; }
				}
		if (maxret-subs>curmax) {
			curmax = maxret - subs;
			curways = 1;//factorial;
		}
		else if (maxret-subs==curmax) {
			curways += 1;//factorial;
		}
	}
}

int main()
{
    fstream fin("D-small-attempt0.in",ifstream::in);
    fstream fout("D-small-attempt0.out",ofstream::out);
    fin >> T;
	for(int tc=1;tc<=T;tc++)
    {
		fin >> M >> N;
		lines.resize(M);
		grps.resize(M);
		rep(i,M) fin >> lines[i];
		same.resize(M);
		factorial = 1;
		curmax = 0;
		curways = 0;
		for(int i=0;i<N;++i) 
			factorial = (factorial * (i+1))%MOD;
		rep(i,M) {
			same[i].resize(M);
			rep(j,M) same[i][j] = getSameSub(lines[i], lines[j]);
		}
		go(0);
		fout << "Case #" << tc << ": " << curmax << " " << curways << "\n";
		cout << "Case #" << tc << ": " << curmax << " " << curways << "\n";
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC << "\n";
    system("PAUSE");
    return 0;
}
