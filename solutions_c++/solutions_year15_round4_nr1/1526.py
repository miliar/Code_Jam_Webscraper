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
typedef vector<IntVec> IntVV;
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

bool OK(const IntVV& maze, unsigned const R, unsigned const C, int i, int j, int dir) {
    int row=i, col=j;
    while (true) {
	switch (dir) {
	    case 1 : col++; break;
	    case 2 : row++; break;
	    case 3 : col--; break;
	    case 4 : row--; break;
	    default: cerr << "bad dir=" << dir << endl; exit(0);
	}
	if (col >= (int)C || col < 0 || row >= (int)R || row < 0)
	    return false;
	else if (maze[row][col] != 0)
	    return true;
    }
}

int Change(const IntVV& maze, unsigned const R, unsigned const C, int i, int j) {
    int dir = maze[i][j];
    if (dir == 0)
	return 0;
    if (OK(maze, R, C, i, j, dir))
	return 0;
    for (int dir2=1; dir2<=4; dir2++)
	if (OK(maze, R, C, i, j, dir2))
	    return 1;
    return -1;
}

int MinChanges(const IntVV& maze, unsigned const R, unsigned const C) {
    int sum=0;
    forall (i, R)
	forall (j, C) {
	    int c = Change(maze, R, C, i, j);
	    if (c >= 0)
		sum += c;
	    else
		return c;
	}
    return sum;
}

int main() {
    // cout << setprecision(10);
    int nTasks;
    cin >> nTasks;
    for (int iTask=1; iTask<=nTasks; iTask++) {
	unsigned R, C;
	cin >> R >> C;
	IntVV maze(R); 
	forall (i, R) {
	    string s;
	    cin >> s;
	    assert(s.size()==C);
	    maze[i].resize(C);
	    forall (j, C) {
		switch(s[j]) {
		    case '.' : maze[i][j]=0; break;
		    case '>' : maze[i][j]=1; break;
		    case 'v' : maze[i][j]=2; break;
		    case '<' : maze[i][j]=3; break;
		    case '^' : maze[i][j]=4; break;
		    default :
			cerr << "Bad char " << s[j] << " i=" << i << " j=" << j << endl; 
			exit(0);
		}
	    }
	}
	int n = MinChanges(maze, R, C);
	cout << "Case #" << iTask << ": ";
	if (n >= 0)
	    cout << n << '\n';
	else
	    cout << "IMPOSSIBLE\n";
    }
}
