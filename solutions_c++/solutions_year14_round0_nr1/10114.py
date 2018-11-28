#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <set>
#include <fstream>
#include <utility>
#include <string>
#include <sstream>
#include <cstring>
#include <cmath>
#define INF (int)1e9
#define EPS 1e-9
#define forall(i,a,b) for(int i=a;i<b;i++)
#define pb push_back
#define mp make_pair
#define sz(a) ((int)(a.size()))


using namespace std;

int main() {

	ofstream myfile;
  	myfile.open ("output.txt");
  	
  	ifstream infile ("A-small-attempt1.in");
  	if (infile.is_open()) {
  		
 	int t = 1, n;
	infile >> n;
	while(t <= n) {

		int first, second, ans;
		set<int> row1;
		vector<int> row2;
		
		infile >> first;
		forall(i, 1, 5) {
			forall(j, 1, 5) {
				int x;
				infile >> x;
				if(i == first) row1.insert(x); 
			}
		}
		
		infile >> second;
		forall(i, 1, 5) {
			forall(j, 1, 5) {
				int x;
				infile >> x;
				if(i == second) row2.pb(x); 
			}
		}		
		
		int c = 0;
		forall(i, 0, row2.size()) {
			if(row1.count(row2[i])) {
				ans = row2[i];
				c++;
			}
		}
		
		if(c == 0) myfile << "Case #" << t << ": Volunteer cheated!" << endl;
		else if (c == 1) myfile << "Case #" << t << ": " << ans << endl;
		else myfile << "Case #" << t << ": Bad magician!" << endl;
		
		t++;
	}
	infile.close();
	myfile.close();
}
}
