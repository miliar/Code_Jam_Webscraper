#include <cstdio>
#include <algorithm>

using namespace std;
const int MAX = 100020;

int n, x, data[MAX];

void input(){
	scanf("%d%d", &n, &x);

	int i;
	for(i = 0; i<n; i++)
		scanf("%d", &data[i]);

	sort(data, data+n);
}

void solve(){
	int s = 0, e = n-1, res = 0;
	while(s < e){
		if(data[s]+data[e] <= x){
			s++;
			e--;
			res++;
		} else {
			e--;
			res++;
		}
	}
	if(s == e) res++;

	printf("%d\n", res);
}

int main(){
	freopen("output.txt", "w", stdout);

	int numCase, t;
	scanf("%d", &numCase);
	for(t = 1; t<= numCase; t++){
		printf("Case #%d: ", t);

		input();
		solve();
	}

	return 0;
}