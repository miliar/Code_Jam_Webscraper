#include <cstdio>
#include <vector>
#include <map>
using namespace std;

int r1,r2,T[5][5];
map <int,int> candidate;

void input(){
	candidate.clear();

	scanf("%d",&r1);
	for(int i=1;i<=4;i++) for(int j=1;j<=4;j++) scanf("%d",&T[i][j]);
	for(int j=1;j<=4;j++) candidate[T[r1][j]]++;
	scanf("%d",&r2);
	for(int i=1;i<=4;i++) for(int j=1;j<=4;j++) scanf("%d",&T[i][j]);
	for(int j=1;j<=4;j++) candidate[T[r2][j]]++;
}

void solve(){
	vector<int> ans;
	for(map<int,int>::iterator it=candidate.begin();it!=candidate.end();it++){
		if(it->second == 2){
			ans.push_back(it->first);
			continue;
		}
	}
	if(ans.size() > 1) printf("Bad magician!\n");
	else if(ans.size() == 1) printf("%d\n",ans[0]);
	else if(ans.size() == 0) printf("Volunteer cheated!\n");
}

int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);

	int T; scanf("%d",&T);
	for(int _i=1;_i<=T;_i++){
		printf("Case #%d: ",_i);
		input();
		solve();
	}
	return 0;
}