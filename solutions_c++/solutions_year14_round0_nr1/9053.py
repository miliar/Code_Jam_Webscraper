#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int main(){
	int tc, tcn;
	scanf("%d", &tcn);
	for(tc=0; tc<tcn; ++tc){
		printf("Case #%d: ", tc+1);
		set<int> s[2];
		for(int i=0; i<2; ++i){
			int x;
			scanf("%d", &x);
			x--;
			for(int j=0; j<16; ++j){
				int y;
				scanf("%d", &y);
				if(j/4 == x)
					s[i].insert(y);
			}
		}
		vector<int> r(4);
		vector<int>::iterator it = set_intersection(s[0].begin(), s[0].end(), s[1].begin(), s[1].end(), r.begin());
		if(it - r.begin() == 1){
			printf("%d\n", *r.begin());
		} else if (it - r.begin()){
			puts("Bad magician!");
		} else {
			puts("Volunteer cheated!");
		}
	}
}
