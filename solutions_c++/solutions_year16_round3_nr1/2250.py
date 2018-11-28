#include <stdio.h>
#include <queue>
using namespace std;
struct p{
	int index;
	int value;
};

bool operator<(p i, p j){
	return i.value < j.value;
}
int main(void){
	int T;
	int N;
	priority_queue<p> P;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int testcase = 1; testcase <= T; ++testcase){
		scanf("%d", &N);
		int sum = 0;
		for (int i = 0; i < N; i++){
			p input;
			scanf("%d", &input.value);
			input.index = i;
			P.push(input);
			sum += input.value;
		}
		printf("Case #%d: ", testcase);
		while (sum > 0){
			p t = P.top();
			printf("%c", 'A' + t.index);
			--sum;
			--t.value;
			P.pop();
			P.push(t);
			if (sum == 2){
				printf(" ");
				continue;
			}
			t = P.top();
			printf("%c", 'A' + t.index);
			--sum;
			--t.value;
			P.pop();
			P.push(t);
			printf(" ");
		}
		printf("\n");
	}
	return 0;
}