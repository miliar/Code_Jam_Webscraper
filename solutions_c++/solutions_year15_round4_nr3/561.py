#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <set>
using namespace std;
const int MAXN = 200+5;
int T, N;
char line[1<<12];

bitset<2005> s[2], s0, s1;
bitset<2005> sentance[20];
int tot;
int insert(string str){
    if(mp.find(str)==mp.end()){
        mp[str]=tot++;
    }
    return mp[str];
}

void dfs(int x) {
	if (x == N) {
		return;
	}
	vis[x] = false;
	dfs(x+1);
	vis[x] = true;
	dfs(x+1);
}
int main() {
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		scanf("%d", &N);
		gets(line);
		for (int i = 1; i <= N; i++) {
			gets(line);
			cout<<string(line)<<endl;
			stringstream sin(string(line));
		}
		dfs(3);

        int ans=1000000;
        for(int i=0; i<(1<<n); i++){
            s0=s[0]; s1=s[1];
            for(int j=0; j<n; j++){
                if(i>>j&1){
                    s0|=sentance[j];
                }
                else{
                    s1|=sentance[j];
                }
            }
            int ret=(s0&s1).count();
            ans=min(ans,ret);
        }

		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}