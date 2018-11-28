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

vector <ll> cand;

ll mkpalin1(int n) {
	int i=n;
	ll ret=n;
	while(i) {
		ret*=10;
		ret+=i%10;
		i/=10;
	}
	return ret;
}

ll mkpalin2(int n) {
	int i=n/10;
	ll ret=n;
	while(i) {
		ret*=10;
		ret+=i%10;
		i/=10;
	}
	return ret;
}

bool palin(ll n) {
	vector <int> v;
	while(n) {
		v.push_back(n%10);
		n/=10;
	}
	vector <int> v2=v;
	reverse(v2.begin(), v2.end());
	if(v==v2) return true;
	else return false;
}

void pre_calc() {
	for(int i=1; i<=999; i++) {
		ll j=mkpalin1(i);
		j=j*j;
		if(palin(j)) cand.push_back(j);
		j=mkpalin2(i);
		j=j*j;
		if(palin(j)) cand.push_back(j);
	}
	sort(cand.begin(), cand.end());
	cout << cand.size() << endl;
}

ll solve(ll A, ll B) {
	ll res=0;

	for(int i=0; i<(int)cand.size(); i++) {
		if(cand[i]>=A && cand[i]<=B) res++;
	}
	
	return res;
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

	pre_calc();
	int testcase;
	ifs >> testcase; ifs.ignore();
	for(int testnum=1; testnum<=testcase; testnum++) {
		ll A, B;
		ifs >> A >> B;
		ll res=solve(A, B);
		ofs << "Case #" << testnum << ": ";
		ofs << res << endl;
	}
}

//Powered by NTL-5.5.2 (http://www.shoup.net/ntl/)