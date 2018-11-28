#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cassert>
#include <cstdlib>

using namespace std;

#define forall(i,n) for(int i=0; i<(int)(n); i++)

template<class T, class T1, class T2> inline bool Within(T x, T1 xMin, T2 xMax)
    {return (x >= xMin && x <= xMax);}
template<class T, class T1> inline bool Within(T x, T1 xMax)
    {return (x >= 0 && x < xMax);}

void Print(const vector<bool>& v) {
    forall (i, v.size())
	cout << (v[i] ? '+' : '-');
    cout << endl;
}

void Print(const vector< pair<double, bool> >& v) {
    forall (i, v.size())
	cout << v[i].first << ' ' << v[i].second << '\n';
    cout << endl;
}

template<class T> void Shuffle(vector<T>& v) {
    for (int i=1; i<(int)v.size(); i++) {
	int r = rand() % (i+1);
	swap(v[i], v[r]);
    }
}

vector<bool> GenTest(int n) {
    vector<bool> v(2*n);
    int nPlus=n, nMinus=n;
    forall (i, 2*n) {
	int r = rand() % (nPlus + nMinus);
	if (r < nPlus) {
	    v[i] = true;
	    nPlus--;
	} else {
	    v[i] = false;
	    nMinus--;
	}
    }
    return v;
}

vector<bool> Exclude(const vector<bool>& v, int i1, int i2) {
    assert(v.size() >= 2);
    assert(Within(i1, v.size()));
    assert(Within(i2, v.size()));
    vector<bool> out(v.size()-2);
    int iOut=0;
    forall (iIn, v.size())
	if (iIn!=i1 && iIn!=i2)
	    out[iOut++] = v[iIn];
    return out;
}

int Better(const vector<bool>& v1, const vector<bool>& v2) {
    int i1=-1, i2=-1;
    int c=0;
    while (true) {
	i1++, i2++;
	while (i1 < (int)v1.size() && !v1[i1])
	    i1++;
	if (i1 == (int)v1.size())
	    return c;
	while (i2 < (int)v2.size() && !v2[i2])
	    i2++;
	assert(i2 != (int)v2.size());
	if (i1 < i2) {
	    if (c < 0)
		return 0;
	    c = 1;
	}
	else if (i1 > i2) {
	    if (c > 0)
		return 0;
	    c = -1;
	}
    }
}

map<vector<bool>, int> mapScores;

int War(const vector<bool>& v) {
    if (v.empty())
	return 0;

    if (v[v.size()-1]) {
	int j;
	for (j = (int)v.size()-2; j>=0; j--)
	    if (!v[j])
		break;
	assert(j >= 0);
	vector<bool> v1 = Exclude(v, j, v.size()-1);
	return War(v1);
    }
    if (v[0]) {
	int j;
	for (j = (int)v.size()-1; j>=0; j--)
	    if (!v[j])
		break;
	assert(j < (int)v.size());
	vector<bool> v1 = Exclude(v, 0, j);
	return War(v1) + 1;
    }
    int iFirst;
    for (iFirst=1; iFirst<(int)v.size(); iFirst++)
	if (v[iFirst])
	    break;
    assert(iFirst < (int)v.size());
    vector<bool> v1 = Exclude(v, 0, iFirst);
    return War(v1);
}

int DWar(const vector<bool>& v) {
    if (v.empty())
	return 0;
    bool bFound = false;
    int iWorst = -1, iWinning = -1, iWorstEnemy = -1;
    for (int i=(int)v.size()-1; i>=0; i--) {
	if (!v[i]) {
	    if (!bFound) {
		iWorstEnemy = i;
		bFound = true;
	    }
	    continue;
	}
	if (iWorst < 0)
	    iWorst = i;
	if (bFound) {
	    iWinning = i;
	    break;
	}
    }
    assert(iWorst >= 0 && iWorstEnemy >= 0);
    assert(iWinning < iWorstEnemy && iWinning <= iWorst);

    int iBestEnemy = -1;
    forall (i, v.size()) {
	if (!v[i]) {
	    iBestEnemy = i;
	    break;
	}
    }
    assert(iBestEnemy >= 0);

    int score2 = -1;
    if (iWinning >=0) {
	score2 = DWar(Exclude(v, iWorstEnemy, iWinning)) + 1;
	return score2;
    }
    int score1 = DWar(Exclude(v, iBestEnemy, iWorst));
    return score1;
}



int main() {
    // DEBUG
    /*
    const bool b10 = true;
    if (b10) {
	forall (i, 10000) {
	    vector<bool> v = GenTest(10);
	    cout << DWar(v) << ' ' << War(v) << endl;
	}
    }
    else {
	forall (i, 100) {
	    cerr << i << endl;
	    vector<bool> v = GenTest(i);
	    cout << DWar(v) << ' ' << War(v) << endl;
	}
    }
    return 0;
    */

    int nTasks;
    cin >> nTasks;
    for (int iTask=1; iTask<=nTasks; iTask++) {
	int N;
	cin >> N;
	vector<pair<double, bool> > vPairs(2*N);
	forall (i, 2*N) {
	    double w;
	    cin >> w;
	    vPairs[i] = make_pair(w, i<N);
	}
	sort(vPairs.begin(), vPairs.end());
	vector<bool> v(2*N);
	forall (i, 2*N)
	    v[i] = vPairs[i].second;
	reverse(v.begin(), v.end());
	mapScores.clear();
	cout << "Case #" << iTask << ": " << DWar(v) << ' ' << War(v) << '\n';
    }
}
