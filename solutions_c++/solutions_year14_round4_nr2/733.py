#include <cstdio>
#include <algorithm>

using namespace std;
const int MAX = 1020, INF = 1234567890;

int n, data[MAX];

void input(){
	scanf("%d", &n);
	
	int i;
	for(i = 0; i<n; i++)
		scanf("%d", &data[i]);
}

void solve(){
	int s = 0, e = n-1, i, res = 0;
	while(s <= e){
		int minVal = INF, minPos = -1;

		for(i = s; i<=e; i++){
			if(data[i] < minVal){
				minVal = data[i];
				minPos = i;
			}
		}

		if(minPos-s <= e-minPos){
			for(i = minPos; i>s; i--){
				swap(data[i], data[i-1]);
				res++;
			}
			s++;
		} else {
			for(i = minPos; i<e; i++){
				swap(data[i], data[i+1]);
				res++;
			}
			e--;
		}
	}

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