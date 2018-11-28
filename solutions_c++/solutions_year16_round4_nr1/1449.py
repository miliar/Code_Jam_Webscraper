#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cassert>
#include <cstdlib>
#include <cstdio>

using namespace std;

#define forall(i,n) for(int i=0; i<(int)(n); i++)

typedef vector<int> IntVec;
typedef long long ll;
typedef unsigned long long ull;

template<class T, class T1, class T2> inline bool Within(T x, T1 xMin, T2 xMax)
    {return (x >= xMin && x <= xMax);}
template<class T, class T1> inline bool Within(T x, T1 xMax)
    {return (x >= 0 && x < xMax);}

template<class T> void PrintVec(const vector<T>& v, const char* s=NULL) {
    if (s)
	cout << s << ' ';
    forall (i, v.size())
	cout << v[i] << ' ';
    cout << endl;
}

template<class T> void PrintVec(const char* s, const vector<T>& v) {
    PrintVec(v, s);
}


bool Comb(string& s, int P, int R, int S) {
    int len = P+R+S;
    if (len == 1) {
	if (P == 1)
	    s.resize(1, 'P');
	else if (R == 1)
	    s.resize(1, 'R');
	else if (S == 1)
	    s.resize(1, 'S');
	else {
	    cout << "bad prs\n";
	    exit(0);
	}
	return true;
    }
    if (abs(P-R)>1 || abs(P-S)>1 || abs(R-S)>1)
	return false;
    int P1 = (P+R-S)/2, R1=(R+S-P)/2, S1=(P+S-R)/2;
    swap(R1,S1);
    string s1;
    bool rc = Comb(s1, P1, R1, S1);
    assert(rc);
    s.resize(len);
    forall (i, len/2) {
	const char c = s1[i];
	if (c == 'P') { s[2*i] = 'P'; s[2*i+1]='R'; }
	else if (c == 'R') { s[2*i] = 'P'; s[2*i+1]='S'; }
	else if (c == 'S') { s[2*i] = 'R'; s[2*i+1]='S'; }
	else {cout << "bad character " << c << endl; exit(0);}
    }
    return true;
}

int main() {
    // cout << setprecision(10);
    int nTasks;
    cin >> nTasks;
    for (int iTask=1; iTask<=nTasks; iTask++) {
	int N, P, R, S;
	cin >> N >> R >> P >> S;
	const int len = (1 << N);
	assert(P + R + S == len);
	cout << "Case #" << iTask << ": "; // DEBUG
	string s;
	s.resize(len);
	bool rc = Comb(s, P, R, S);
	// cout << P << ' ' << R << ' ' << S << ' '; // DEBUG
	if (rc)
	    cout << s << '\n';
	else
	    cout << "IMPOSSIBLE\n";
    }
}
