#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
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

string SFromB(int len, int bin) {
    string s(len, '-');
    forall (i, len)
    if (bin & (1 << (len - 1 - i)))
	s[i] = '+';
    else
	s[i] = '-';
    return s;
}

IntVec Best(int len, int nFlips) {
    int pow2 = (1 << len);
    IntVec v(pow2, -1);
    v[pow2-1] = 0;

    if (len < nFlips) {
	return v;
    }

    const int templ = (1 << nFlips) - 1;

    IntVec v0;
    v0.push_back(pow2-1);
    int nSteps = 0;
    while (!v0.empty()) {
	/*
	// DEBUG
	cout << "nSteps=" << nSteps << " nFlips=" << nFlips << " v0=";
	// PrintVec(v0);
	forall (i, v0.size())
	    cout << ' ' << SFromB(len, v0[i]);
	cout << '\n';
	*/

	++nSteps;
	IntVec vNext;
	forall (i, v0.size())
	    forall (j, len-nFlips+1) {
		const int bin = v0[i] ^ (templ << j);
		if (v[bin] == -1) {
		    vNext.push_back(bin);
		    v[bin] = nSteps;
		}
	    }
	v0 = vNext;
    }
    return v;
}

int MinSteps(const string& s, int nFlips) {
    const int len = s.size();
    vector<bool> d(len+1);
    forall (i, len)
	d[i] = (s[i] != s[i-1]);
    d[0] = (s[0] == '-');
    d[len] = (s[len-1] == '-');
    int nSteps = 0;
    for (int i=0; i<=len-nFlips; i++) {
	if (d[i]) {
	    ++nSteps;
	    d[i] = true;
	    d[i+nFlips] = !d[i+nFlips];
	}
    }
    for (int i=len-nFlips+1; i<=len; i++)
	if (d[i])
	    return -1;
    return nSteps;
}


int main() {
    // cout << setprecision(10);
    int nTasks;
    cin >> nTasks;
    for (int iTask=1; iTask<=nTasks; iTask++) {
	string s;
	int nFlips;
	cin >> s >> nFlips;
	/*
	const int len = s.length();
	int bin = 0;
	forall (i, len)
	    if (s[len-1-i] == '+')
		bin += (1 << i);
	IntVec vSteps = Best(len, nFlips);
	int nSteps = vSteps[bin];
	*/
	int nSteps = MinSteps(s, nFlips);
	cout << "Case #" << iTask << ": ";
	// cout << '"' << s << "\" " << nFlips << ' ' << bin << ' '; // DEBUG
	if (nSteps >= 0)
	    cout << nSteps << '\n';
	else
	    cout << "IMPOSSIBLE\n";
    }
}
