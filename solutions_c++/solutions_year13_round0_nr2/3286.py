#include <cstdio>
#include <algorithm>

struct s_mp{
	int r, c, id;
	bool operator < (const s_mp &b) const{
		return (id < b.id);
	}
};

inline int max(int a, int b){ return a > b ? a : b; }

int main(){
	int N, M;
	int rws[100], cls[100];
	s_mp *map = new s_mp[100 * 100];
	for(int T, t = (scanf("%d", &T), 1); t <= T; t++){
		scanf("%d %d", &N, &M);
		for(int i = 0, ct = 0; i < N; i++){
			for(int j = 0; j < M; j++){
				map[ct].r = i;
				map[ct].c = j;
				scanf("%d", &(map[ct++].id));
			}
		}
		std::sort(map, map + N * M);
		for(int i = 0; i < N; i++){ rws[i] = 0; }
		for(int j = 0; j < M; j++){ cls[j] = 0; }
		bool isOK = true;
		for(int i = N * M - 1; isOK && i >= 0; i--){
			if(rws[map[i].r] > map[i].id && cls[map[i].c] > map[i].id){
				isOK = false;
			}else{
				rws[map[i].r] = max(rws[map[i].r], map[i].id);
				cls[map[i].c] = max(cls[map[i].c], map[i].id);
			}
		}
		printf("Case #%d: %s\n", t, isOK ? "YES" : "NO");
	}
	delete [] map;
	return 0;
}
