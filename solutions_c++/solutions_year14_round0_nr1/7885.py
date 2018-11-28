#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>

using namespace std;

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int TC;
	scanf("%d", &TC);
	for(int tc=1; tc<=TC; tc++) {
		int a;
		scanf("%d", &a);
		vector<int> f;
		for(int i=0; i<4; i++) for(int j=0; j<4; j++){
			int t;
			scanf("%d", &t);
			if( i+1 == a ) f.push_back(t);
		}
		int b;
		scanf("%d", &b);
		vector<int> s;
		for(int i=0; i<4; i++) for(int j=0; j<4; j++) {
			int t;
			scanf("%d", &t);
			if( i+1 == b ) s.push_back(t);
		}
		vector<int> ans;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				if( f[i] == s[j] ) 
					ans.push_back(s[j]);
		if( ans.size() == 0 ) {
			printf("Case #%d: Volunteer cheated!\n", tc);
		}
		else if( ans.size() == 1 ) {
			printf("Case #%d: %d\n", tc, ans[0]); 
		}
		else {
			printf("Case #%d: Bad magician!\n", tc);
		}
					
		
	}
	return 0;
}