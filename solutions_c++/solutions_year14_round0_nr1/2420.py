#include <iostream>
#include <cstdlib>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <math.h>
#include <stack>
#include <queue>
#include <list>
#include <limits.h>
#include <time.h>
#include <iterator>

#pragma comment(linker, "/STACK:167772160")

using namespace std;

int main(){
	ifstream cin("A-small-attempt0 (1).in");
	ofstream cout ("out.txt");
	int T;
	cin >> T;
	for(int t=0; t<T; t++) {
		int n;		
		int cnt[17] = {};
		cin >> n;
		for(int i=1; i<=4; i++)
			for(int j=1; j<=4; j++) {
				int p;
				cin >> p;
				if(i == n) cnt[p]++;
			}
		cin >> n;
		for(int i=1; i<=4; i++)
			for(int j=1; j<=4; j++) {
				int p;
				cin >> p;
				if(i == n) cnt[p]++;
			}
		int k = 0, ans;
		for(int i=1; i<17; i++)
			if(cnt[i] == 2) k++, ans = i;
		cout << "Case #" << t+1 << ": " ;
		if(!k) cout << "Volunteer cheated!\n"; else
			if(k == 1) cout << ans << endl; else
				cout << "Bad magician!\n";
	}
    return 0;
}