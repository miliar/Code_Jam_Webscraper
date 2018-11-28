#include<iostream>
#include<string>
// #include<math.h>
#include<vector>
#include<algorithm>
// #include<map>
// #include<utility>
// #include<sstream>
// #include<ctype.h>
// #include<queue>

using namespace std;

int puiss (int a, int b);
int app (vector<int> tab, int x);

int main(){
	int T, row, a;

	cin >> T;
	for (int i = 0; i < T; i++) {
		vector<int> t1, t2;
		cin >> row;
		for (int j = 0; j < 16; j++) {
			cin >> a;
			if (j >= 4*(row-1) && j < 4*row ) { t1.push_back(a); }
		}
		cin >> row;
//cout << "row = " << row << "\n";
                for (int j = 0; j < 16; j++) {
                        cin >> a;
//cout << "j = " << j << "\n";
                        if (j >= 4*(row-1) && j < 4*row && app(t1,a)) {
				t2.push_back(a);
//cout << "condition ok\n";
			}
		}
//for (unsigned int i = 0; i < t1.size(); i++) { cout << t1[i] << " "; }
//cout << "\n";
//for (unsigned int i = 0; i < t2.size(); i++) { cout << t2[i] << " "; }
//cout << "\n";
		if (t2.size() > 1) {
			cout << "Case #" << i+1 << ": Bad magician!\n";
		}
		if (t2.size() == 1) {
                               cout << "Case #" << i+1 << ": " << t2[0] << "\n";
		}
		if (t2.size() == 0) {
                               cout << "Case #" << i+1 << ": Volunteer cheated!\n";
		}
	}
}


int puiss (int a, int b) {
        if (b == 0) { return 1; }
        if (b == 1) { return a; }
        int temp = puiss (a, b/2);
        if ( b%2 ) { return (temp*temp*a); }
        return (temp*temp);
}

int app (vector<int> tab, int x) {
	for (unsigned int i = 0; i < tab.size(); i++) {
		if (x == tab[i]) { return 1; }
	}
	return 0;
}
