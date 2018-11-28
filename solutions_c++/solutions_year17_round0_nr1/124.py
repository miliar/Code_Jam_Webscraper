#include<cstdio>
#include<algorithm>
#include<string>
using namespace std;

int process(string& str, int K){
	int N = str.size();
	int ret = 0;
	for (int i = 0; i <= N - K; i++){
		if (str[i] == '-'){
			for (int j = 0; j < K; j++) str[i + j] = '-' + '+' - str[i + j];
			ret++;
		}
	}

	for (int i = 0; i < N; i++) if (str[i] == '-') return -1;
	return ret;
}

char buff[1111];

int main(){
	freopen("large.in", "r", stdin);
	freopen("large.out", "w", stdout);

	int T; scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++){
		printf("Case #%d: ", tc);
		int K; scanf("%s%d", buff, &K);
		int res = process(string(buff), K);
		if (res < 0) printf("IMPOSSIBLE\n");
		else printf("%d\n", res);
	}
}