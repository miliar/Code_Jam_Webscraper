#include <stdio.h>
#include <algorithm>
#include <vector>
#include <iterator>

using namespace std;

int board1[4][4];
int board2[4][4];
vector<int> first;
vector<int> second;

void solve(int ans1, int ans2, int t){
	sort(first.begin(),first.end());
	sort(second.begin(),second.end());
	
	vector<int> intersection;
	set_intersection(first.begin(),first.end(),second.begin(),second.end(),
		back_inserter(intersection));
		
	if(intersection.size() == 0)
		printf("Case #%d: Volunteer cheated!\n",t);
	else if(intersection.size() > 1)
		printf("Case #%d: Bad magician!\n",t);
	else	
		printf("Case #%d: %d\n", t, intersection[0]);
}

int main(){
	int t,ans1,ans2;
	scanf("%d",&t);
	for(int i=1;i<=t;++i){
		scanf("%d",&ans1);
		for(int j=0;j<4;++j){
			for(int k=0;k<4;++k){
				scanf("%d",&board1[j][k]);
				if(j == ans1-1)
					first.push_back(board1[j][k]);
			}
		}
		scanf("%d",&ans2);
		for(int j=0;j<4;++j){
			for(int k=0;k<4;++k){
				scanf("%d",&board2[j][k]);
				if(j == ans2-1)
					second.push_back(board2[j][k]);
			}
		}
		solve(ans1,ans2,i);
		first.clear();
		second.clear();
	}
	
	return 0;
}