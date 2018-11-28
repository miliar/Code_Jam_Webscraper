#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <list>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <numeric>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <iterator>
#include <complex>
#include <stack>
#include <queue>
#include <ctime>
#include <cassert>
//#include <NTL/ZZ.h>
using namespace std;
//using namespace NTL;
static const double EPS = 1e-8;
typedef long long ll;
typedef unsigned long long ull;
typedef complex <double> pt;
typedef complex <ll> pti;

int ok[1<<20];

int rec(int mask, int ckeys[201], vector <int> &lock, vector <vector <int> > &keys2) {
	int res=0;
	int n=lock.size();
	if(mask==(1<<n)-1) return true;

	for(int i=0; i<n; i++) {
		if(mask&(1<<i)) continue;
		if(ckeys[lock[i]]==0) continue;
		int nmask=(mask|(1<<i));
		if(ok[nmask]>=0) {
			res|=ok[nmask];
		} else {
			ckeys[lock[i]]--;
			for(int j=0; j<(int)keys2[i].size(); j++) ckeys[keys2[i][j]]++;
			res|=rec(nmask, ckeys, lock, keys2);
			ckeys[lock[i]]++;
			for(int j=0; j<(int)keys2[i].size(); j++) ckeys[keys2[i][j]]--;
		}
	}
	if(res) ok[mask]=1;
	else ok[mask]=0;
	return res;
}

string solve(vector <int> &keys, vector <int> &lock, vector <vector <int> > &keys2) {
	string res;
	int n=lock.size();

	int ckeys[201];
	memset(ckeys, 0, sizeof(ckeys));
	for(int i=0; i<(int)keys.size(); i++) ckeys[keys[i]]++;

	for(int i=0; i<(1<<20); i++) ok[i]=-1;
	if(rec(0, ckeys, lock, keys2)==0) return "IMPOSSIBLE";

	int mask=0;
	for(int i=0; i<n; i++) {
		for(int j=0; j<n; j++) {
			if(mask&(1<<j)) continue;
			if(ckeys[lock[j]]==0) continue;
			if(ok[mask|(1<<j)]==0) continue;
			stringstream ss;
			ss << j+1;
			res+=ss.str()+" ";
			mask|=(1<<j);
			ckeys[lock[j]]--;
			for(int k=0; k<(int)keys2[j].size(); k++) ckeys[keys2[j][k]]++;
			break;
		}
	}
	
	return res.substr(0, res.size()-1);
}

int main() {
	int practice=0;
	string prb[12];
	const string difficulty[2][2]={{"-small-attempt.in", "-large.in"}, {"-small-practice.in", "-large-practice.in"}};
	const string extension="";
	//const string extension=".txt";

	char key;
	while(1) {
		for(int i=0; i<12; i++) {
			prb[i].assign(1, 'A'+i/2);
			prb[i]+=difficulty[practice][i%2];
			prb[i]+=extension;
			cout << (char)(i%2?('A'+i/2):('a'+i/2)) << ". " << prb[i] << endl;
		}
		cout << "p. " << (practice?"change to practice mode.":"change to match mode.") << endl;

		do {
			cout << "Choose the input file." << endl;
			cin >> key;
		} while(!('a'<=key && key<'a'+6) && !('A'<=key && key<'A'+6) && key!='p');
		if(key!='p') break;
		practice^=1;
		system("cls");
	}

	int index, cap;
	if(key>='a') { index=(key-'a')*2; cap=0; }
	else { index=(key-'A')*2+1; cap=1; }
	string filename=prb[index];

	if(!cap && !practice) {
		do {
			cout << "Choose number of attempt times." << endl;
			cin >> key;
		} while(key<'0' || '9'<key);
		filename.insert(15, 1, key);
	}

	cout << "Filename is " << filename << endl;
	ifstream ifs(filename.c_str());

	ofstream ofs("output.txt");

	int testcase;
	ifs >> testcase; ifs.ignore();
	for(int testnum=1; testnum<=testcase; testnum++) {
		int K, N;
		ifs >> K >> N;
		vector <int> keys(K);
		for(int i=0; i<K; i++) ifs >> keys[i];
		vector <int> lock(N);
		vector <vector <int> > keys2(N);
		for(int i=0; i<N; i++) {
			int k;
			ifs >> lock[i] >> k;
			keys2[i].resize(k);
			for(int j=0; j<k; j++) ifs >> keys2[i][j];
		}
		string res=solve(keys, lock, keys2);
		ofs << "Case #" << testnum << ": ";
		ofs << res << endl;
	}
}

//Powered by NTL-5.5.2 (http://www.shoup.net/ntl/)