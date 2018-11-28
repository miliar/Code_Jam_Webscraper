#include <stdio.h>
#include <algorithm>
#include <queue>

using namespace std;

int N;
int P[30];

priority_queue<pair<int, int> > q;

int main(void){

	int testcase;
	scanf("%d", &testcase);

	for(int t_itr = 1; t_itr <= testcase; t_itr++){
		scanf("%d", &N);

		int total_cnt = 0;
		for(int i=0; i<N; i++){
			scanf("%d", &P[i]);
			//printf("%d ", P[i]);
			total_cnt += P[i];
			q.push(make_pair(P[i], i));
		}
		//printf("\n");

		printf("Case #%d: ", t_itr);

		while(!q.empty()){
			for(int i=0; i<2 && !q.empty(); i++){
				total_cnt -= 1;
				int cnt = q.top().first;
				int ch = q.top().second;
				printf("%c", ch+'A');
				q.pop();
				if(cnt != 1){
					q.push(make_pair(cnt-1, ch));
				}
				if(!q.empty() && q.top().first*2 <= total_cnt){
					break;
				}
			}
			printf(" ");
		}
		

		printf("\n");
		

	}
	return 0;
}