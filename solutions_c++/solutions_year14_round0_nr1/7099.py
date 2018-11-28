#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <cstring>
#include <stack>
#include <queue>

using namespace std;

typedef long long int lli;

int main()
{
	int t, t1 = 1;
	int p, q;
	int a[5][5];
	int b[5][5];
	
	scanf("%d", &t);
	
	while (t--) {
		vector<int> v1;
		vector<int> v2;
		vector<int> v3;
		
		scanf("%d", &p);
		
		for (int i = 1; i <= 4; i++) {
			for (int j = 1; j <= 4; j++) {
				scanf("%d", &a[i][j]);
			}
		}
		scanf("%d", &q);
		
		for (int i = 1; i <= 4; i++) {
			for (int j = 1; j <= 4; j++) {
				scanf("%d", &b[i][j]);
			}
		}
		
		for (int i = 1; i <= 4; i++) {
			v1.push_back(a[p][i]);
		}
		
		for (int i = 1; i <= 4; i++) {
			v2.push_back(b[q][i]);
		}
		
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (v1[i] == v2[j]) {
					v3.push_back(v1[i]);
				}
			}
		}
				
		if (v3.size() == 1) {
			cout << "Case #" << t1 << ": " << v3[0] << endl;
		}
		else if (v3.size() == 0) {
			cout << "Case #" << t1 << ": "  << "Volunteer cheated!" << endl;
		}
		else {
			cout << "Case #" << t1 << ": "  << "Bad magician!" << endl;
		}
		t1++;
	}
	
	return 0;
}
