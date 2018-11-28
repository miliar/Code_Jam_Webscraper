#include <bits/stdc++.h>
#define pb push_back
using namespace std;
vector<int> L[30];
int n;
int app[2510];
map<pair<int,int>, int> M;
int main(){
	int t;
	scanf("%d", &t);
	vector<int> ans;
	for(int c=1; c<=t; c++){
		memset(app, 0, sizeof(app));
		scanf("%d", &n);
		for(int i=0; i<2*n-1; i++){
			for(int j=0; j<n; j++){
				int x;
				scanf("%d", &x);
				app[x]++;
			}
		}
		for(int i=0; i<=2500; i++) if(app[i] & 1) ans.push_back(i);
		printf("Case #%d: ", c);
		for(int i=0; i<n; i++) printf("%s%d", (i==0) ? ("") : (" "), ans[i]);
		printf("\n");
		ans.clear(); M.clear();
	}
	return 0;
}