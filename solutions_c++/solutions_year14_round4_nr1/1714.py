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

int dp[10005][10005];
const int INF=1000000000;

int solve(int N, int X, vector <int> S) {
	int res=INF;

	for(int i=1; i<N+2; i++) for(int j=i-1; j<N+2; j++) dp[i][j]=INF;
	dp[1][N]=0;
	sort(S.begin(), S.end());
	for(int i=1; i<=N; i++) {
		for(int j=N; j>=i; j--) {
			if(S[i-1]+S[j-1]>X || j==i) {
				dp[i+1][j]=min(dp[i+1][j], dp[i][j]+1);
				dp[i][j-1]=min(dp[i][j-1], dp[i][j]+1);
			} else {
				dp[i+1][j-1]=min(dp[i+1][j-1], dp[i][j]+1);
			}
		}
	}
	for(int i=1; i<=N+1; i++) res=min(res, dp[i][i-1]);
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
	if(ifs.fail()) {
		cerr << "Failed to open " << filename << endl;
		return 1;
	}

	ofstream ofs("output.txt");

	int testcase;
	ifs >> testcase; ifs.ignore();
	for(int testnum=1; testnum<=testcase; testnum++) {
		int N, X;
		ifs >> N >> X;
		vector <int> S(N);
		for(int i=0; i<N; i++) ifs >> S[i];
		int res=solve(N, X, S);
		ofs << "Case #" << testnum << ": ";
		ofs << res << endl;
	}
}

//Powered by NTL-5.5.2 (http://www.shoup.net/ntl/)