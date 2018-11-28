#include <cstdio>
#include <iostream>
#include <map>
#include <sstream>

using namespace std;
int t, n;

int main(){
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int w,h,i, j;
	//cin >> t;
	scanf("%d", &t);

	for(w = 1; w <= t; w++){
		scanf("%d", &n);
		map<int, int> mapa;
		for(i = 0; i < 2 * n - 1; i++){
			for(j = 0; j < n; j++){
				scanf("%d", &h);
				mapa[h]++;
			}
		}
		printf("Case #%d:", w);
		for(map<int, int>::iterator it = mapa.begin(); it != mapa.end(); it++){
			if(it->second % 2 == 1){
				printf(" %d", it->first);
			}
		}
		printf("\n");
	}

	return 0;
}