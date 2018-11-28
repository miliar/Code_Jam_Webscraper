#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

#define forall(i,n) for(int i=0; i<(int)(n); i++)

template<class T, class T1, class T2> inline bool Within(T x, T1 xMin, T2 xMax)
    {return (x >= xMin && x <= xMax);}


int main() {
    int nTasks;
    cin >> nTasks;
    for (int iTask=1; iTask<=nTasks; iTask++) {
	vector<bool> ok(17, true);
	for (int a=1; a<=2; a++) {
	    int row;
	    cin >> row;
	    assert(Within(row, 1, 4));
	    for (int i=1; i<=4; i++) {
		for (int j=1; j<=4; j++) {
		    int val;
		    cin >> val;
		    assert(Within(val, 1, 16));
		    if (i != row)
			ok.at(val) = false;
		}
	    }
	}
	int nTrue=0, sum=0;
	for (int i=1; i<=16; i++)
	    if (ok.at(i)) {
		nTrue++;
		sum += i;
	    }
	cout << "Case #" << iTask << ": ";
	switch(nTrue) {
	    case 0: cout << "Volunteer cheated!\n"; break;
	    case 1: cout << sum << '\n'; break;
	    default: cout << "Bad magician!\n"; break;
	}
    }
}
