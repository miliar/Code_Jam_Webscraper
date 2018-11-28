#include<cstdio>
#include<algorithm>
#include<map>
#include<vector>
using namespace std;

int T;
map<int,int> pm;

int cut(map<int,int> m){
    for(map<int,int>::iterator it = m.end(); it!=m.begin();){
	it--; int ans=it->first;
	if(it->first<3)
	    return it->first;
	//printf("Not less than 3\n");
	for(int i=it->first-1; i>=(it->first/2); i--){
	//    printf("Doing cut of size %d\n", i);
	    map<int,int> t = m;
	    t[i] += it->second;
	    t[it->first-i] += it->second;
	    t.erase(it->first);
	    ans = min(ans, it->second+cut(t));
	}
	//printf("Returning %d\n", ans);
	return ans;
    }
}
int main(){
    scanf("%d\n", &T);
    for(int i=1; i<=T; i++){
	int ans=0, D;
	pm.clear();
	scanf("%d", &D);
	for(int j=0;j<D; j++){
	    int tmp;
	    scanf("%d", &tmp);
	    pm[tmp]++;
	}

	ans = cut(pm);

	printf("Case #%d: %d\n", i, ans);
    }
}
