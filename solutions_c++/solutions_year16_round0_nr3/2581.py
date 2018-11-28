#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <vector>
#include <string>
#include <cassert>
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;

void printDg(ostream& cout, const vector<bool>& a, const vector<int>& divs){
	for(int i=a.size()-1; i>=0; i--) cout<<(a[i]?1:0);
	for(int i=2; i<=10; i++) cout<<' '<<divs[i];
	cout<<endl;
}

vector< vector<long long> > bases;
vector< long long > primes;

long long toNum(const vector<bool>& dg, int base){
	long long rez = 0;
	for(int i=0; i<dg.size(); i++){
		rez+=bases[base][i]*dg[i];
	}
	return rez;
}

int checkSys(const vector<bool>& dg, int base){
	long long a = toNum(dg, base);
	for(int i=0; i<primes.size(); i++){
		if(a%primes[i]==0){
			return primes[i];
		}
	}
	return -1;
}

bool check(const vector<bool>& dg, vector<int>& divs){
	for(int base=10; base>=2; base--){
		int divv = checkSys(dg, base);
		if(divv==-1){
			return false;
		}
		divs[base] = divv;
	}
	return true;
}

void genBases(int n){
	bases.resize(11);
	for(int i=2; i<=10; i++){
		bases[i].resize(n);
		bases[i][0] = 1;
		for(int j=1; j<n; j++) bases[i][j] = bases[i][j-1]*i;
	}
}

void genPrimes(int maxN){
	vector<int> f(maxN, true);
	for(int i=2; i<maxN; i++){
		if(f[i]){
			primes.push_back(i);
			if(i*1LL*i<maxN){
				for(int j=i*i; j<maxN; j+=i){
					f[j] = false;
				}
			}
		}
	}
}

int main(){
	srand(123);
	genBases(16);
	genPrimes(10001);
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int ntests;
	cin>>ntests;
	for(int testnum=0; testnum<ntests; testnum++){
		int n, J;
		cin>>n>>J;
		cout<<"Case #"<<testnum+1<<":"<<endl;
		vector<bool> dg(n);
		set< vector<bool> > used;
		vector<int> divs(11,0);
		int ok = 0;
		while(ok<50){
			dg[0] = dg[n-1] = 1;
			for(int i=1; i<n-1; i++) dg[i] = rand()%2;
			if(used.find(dg)==used.end() && check(dg, divs)){
				ok++;
				used.insert(dg);
				printDg(cout, dg, divs);
			}
		}
	}
	return 0;
}
