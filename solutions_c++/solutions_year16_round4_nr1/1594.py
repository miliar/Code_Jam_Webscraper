#include <bits/stdc++.h>
using namespace std;

#define fo(x,y,z) for(int x=y;x<z;x++)

int tc;

int main(){
	scanf("%d", &tc);
	fo(x,1,tc+1){
		printf("Case #%d: ", x);
		int n, r, p, s;
		scanf("%d %d %d %d", &n, &r, &p, &s);

		if(n == 1 && r == 1 && s == 1){
			printf("RS\n");
			continue;
		}

		vector<string> ans;
		fo(y,0,3){
			string cur[2];
			if(y == 0) cur[1] = "PR";
			else if(y == 1){
				if(n < 3) cur[1] = "PS";
				else cur[1] = "SP";
			}	
			else cur[1] = "SR";

			fo(i,0,n-1){
				int nx = (i+1)&1;
				cur[i&1] = "";

				fo(j,0,cur[nx].size()){
					if(cur[nx][j] == 'R'&& i == n-2){
						cur[i&1].append("RS");
					}
					else{
						if(cur[nx][j] == 'P') cur[i&1].append("PR");
						else if(cur[nx][j] == 'S'){
							if(i < n-3) cur[i&1].append("SP");
							else cur[i&1].append("PS");
						}
						else cur[i&1].append("SR");
					}
				}
			}
			int cr, cp, cs;
			cr = cp = cs = 0;
			fo(i,0,cur[n&1].size()){
				if(cur[n&1][i] == 'P') cp++;
				else if(cur[n&1][i] == 'S') cs++;
				else cr++;
			}
			if(cr == r && cp == p && cs == s) ans.push_back(cur[n&1]);
		}

		if(ans.size() == 0){
		   	printf("IMPOSSIBLE\n");
			continue;
		}
		sort(ans.begin(), ans.end());
		printf("%s\n", ans[0].c_str());
	}

	return 0;
}
