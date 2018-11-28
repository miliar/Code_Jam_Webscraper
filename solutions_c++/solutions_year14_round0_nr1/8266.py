#include <cstdio>
#include <set>
#include <algorithm>
#include <vector>

using namespace std;

void Solve()
{
	int r;
	set<int> s1, s2;
	scanf("%d", &r);
	for(int i = 1; i<=4; ++i){
		for(int j = 1; j<=4; ++j){
			int k;
			scanf("%d", &k);
			if(i == r){
				s1.insert(k);
			}
		}
	}
	scanf("%d", &r);
	for(int i = 1; i<=4; ++i){
		for(int j = 1; j<=4; ++j){
			int k;
			scanf("%d", &k);
			if(i == r){
				s2.insert(k);
			}
		}
	}
	vector<int> s3(10);
	vector<int>::iterator ret = set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), s3.begin());
	if(ret-s3.begin() == 0){
		printf("Volunteer cheated!\n");
	}else if(ret-s3.begin() > 1){
		printf("Bad magician!\n");
	}else{
		printf("%d\n", s3[0]);
	}
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("small.out", "w", stdout);
	int nCase;
	scanf("%d", &nCase);
	for(int i = 1; i<=nCase; ++i){
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}
