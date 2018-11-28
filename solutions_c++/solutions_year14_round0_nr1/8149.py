#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

typedef pair<int, int> ii;


int main(){
	int t; scanf("%d", &t);
	for(int cas=1;cas<=t;cas++){
		int a, b;
		vector<vector<int> > v(4, vector<int>(4));
		vector<vector<int> > v2(4, vector<int>(4));
		scanf("%d", &a);a--;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d", &v[i][j]);
			}
		}
		scanf("%d", &b);b--;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d", &v2[i][j]);
			}
		}
		set<int> s;
		for(int i=0;i<4;i++){
			s.insert(v[a][i]);
		}
		int c = -1;
		for(int i=0;i<4;i++){
			if(s.find(v2[b][i]) != s.end()){
				if(c == -1){
					c = v2[b][i];
				}else{
					c = -2;
				}
			}
		}
		if(c == -2){
			printf("Case #%d: Bad magician!\n", cas);
		}else if(c == -1){
			printf("Case #%d: Volunteer cheated!\n", cas);
		}else{
			printf("Case #%d: %d\n", cas, c);
		}
	}


}