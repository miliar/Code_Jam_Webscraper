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

string solve(vector <vector <int> > lawn) {
	int n=lawn.size(), m=lawn[0].size();
	vector <vector <int> > lawn2(n, vector <int> (m, 100));

	for(int i=0; i<n; i++) {
		int maxl=0;
		for(int j=0; j<m; j++) maxl=max(maxl, lawn[i][j]);
		for(int j=0; j<m; j++) lawn2[i][j]=min(lawn2[i][j], maxl);
	}

	for(int i=0; i<m; i++) {
		int maxl=0;
		for(int j=0; j<n; j++) maxl=max(maxl, lawn[j][i]);
		for(int j=0; j<n; j++) lawn2[j][i]=min(lawn2[j][i], maxl);
	}

	for(int i=0; i<n; i++) for(int j=0; j<m; j++) {
		if(lawn[i][j]!=lawn2[i][j]) return "NO";
	}
	
	return "YES";
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
		int N, M;
		ifs >> N >> M;
		vector <vector <int> > lawn(N, vector <int>(M));
		for(int i=0; i<N; i++) for(int j=0; j<M; j++) ifs >> lawn[i][j];
		string res=solve(lawn);
		ofs << "Case #" << testnum << ": ";
		ofs << res << endl;
	}
}

//Powered by NTL-5.5.2 (http://www.shoup.net/ntl/)