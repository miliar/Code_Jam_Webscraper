#include<cstdio>
#include<set>

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

int main(){
	int T;
	scanf("%d", &T);
	for (int t = 0; t<T; ++t){
		int a,b;
		set<int> c;
		scanf("%d", &a); a--;
		for (int i = 0; i<4; ++i) {
			for (int j = 0; j<4; ++j) {
				int x;
				scanf("%d", &x);
				if (i == a) c.insert(x);
			}
		}
		scanf("%d", &b); b--;
		int poc = 0, co;
		for (int i = 0; i<4; ++i) {
			for (int j = 0; j<4; ++j) {
				int x;
				scanf("%d", &x);
				if (i == b) {
					if (c.count(x) > 0) {
						poc++;
						co = x;
					}
				}
			}
		}
		printf("Case #%d: ",t+1);
		if (poc == 0) {
			printf("Volunteer cheated!\n");
		} else if (poc == 1) {
			printf("%d\n",co);
		} else {
			printf("Bad magician!\n");
		}
	}
	return 0;
}
