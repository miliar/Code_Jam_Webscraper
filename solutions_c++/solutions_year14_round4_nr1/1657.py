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

int NDisks(IntVec& vSize, int capacity) {
    /*
    // DEBUG
    cout << "Called NDisks capacity=" << capacity << " vSize= ";
    PrintVec(vSize);
    */

    int n = vSize.size();
    if (n <= 1)
	return n;
    int c = capacity - vSize[n-1];
    vSize.resize(n-1);
    if (c < vSize[0]) {
	return NDisks(vSize, capacity) + 1;
    }
    else {
	int i;
	for (i=0; i<n-1; i++)
	    if (c < vSize[i])
		break;
	i--;
	if (!(c >= vSize[i] && (c < vSize[i+1] || i==n-2))) {
	    PrintVec("vSize=", vSize);
	    cout << "i=" << i << " n=" << n << " c=" << c << '\n';
	    assert(0);
	}
	vSize.erase(vSize.begin()+i);
	return NDisks(vSize, capacity) + 1;
    }
}

int main() {
    // cout << setprecision(10);
    int nTasks;
    cin >> nTasks;
    for (int iTask=1; iTask<=nTasks; iTask++) {
	int nFiles, capacity;
	cin >> nFiles >> capacity;
	IntVec vSize(nFiles);
	forall (i, nFiles) cin >> vSize[i];
	sort(vSize.begin(), vSize.end());
	cout << "Case #" << iTask << ": " << NDisks(vSize, capacity) << endl;
    }
}
