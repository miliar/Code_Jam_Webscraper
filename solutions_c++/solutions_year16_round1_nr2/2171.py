#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <vector>
#include <deque>

#define INF 2000000000

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int TC;


int main(){
	scanf("%d", &TC);
	for(int Tn = 1; Tn <= TC; Tn++){
		printf("Case #%d: ", Tn);
		int N;
		scanf("%d", &N);
		vi l;
		int used[3000];
		int heights = 0;
		memset(used, 0, sizeof(used));
		for(int i = 0; i < N * 2 -1; i++){
			for(int j = 0; j < N; j++){
				int a;
				scanf("%d", &a);
				if(used[a] == 0){
					l.push_back(a);
					heights++;
				}
				used[a] = used[a] + 1;
			}
		}
		sort(l.begin(), l.end());

		for(int i = 0; i < heights; i++){
			if(used[l[i]] % 2 == 1) printf("%d ", l[i]);
		}

		printf("\n");
	}
}