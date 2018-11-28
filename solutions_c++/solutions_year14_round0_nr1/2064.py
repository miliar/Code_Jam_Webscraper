#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;
vector<int> a[4], b[4];
int f,s,x;
void solve(int test){
	printf("Case #%d: ", test+1);
	scanf("%d",&f);
	f--;
	for(int i=0; i<4; i++){
		a[i].clear();
		for(int j=0; j<4; j++){
			scanf("%d",&x);
			a[i].push_back(x);
		}
	}
	scanf("%d",&s);
	s--;
	for(int i=0; i<4; i++){
		b[i].clear();
		for(int j=0; j<4; j++){
			scanf("%d",&x);
			b[i].push_back(x);
		}
	}
	int res=-1;
	for(int i=0; i<4; i++){
		for(int j=0; j<4; j++){
			if(a[f][i] == b[s][j]){
				if(res==-1) res= a[f][i];
				else res = 0;
			}
		}
	}
	if(res==-1){
		printf("Volunteer cheated!\n");
	}else if(res==0){
		printf("Bad magician!\n");
	}else{
		printf("%d\n",res);
	}
}
int ntest;
int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&ntest);		
	for(int t=0; t<ntest; t++){
		
		solve(t);
	}
	return 0;
}
