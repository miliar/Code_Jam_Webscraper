#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <math.h>
#include <string.h>
#include <vector>
#include <stack>
#include <queue>

using namespace std;

int main(){
	FILE *ifp, *ofp;

	ifp = fopen("A-large.in", "r");
	ofp = fopen("output.txt", "w");

	int t;

	fscanf(ifp, "%d", &t);

	for (int i = 1; i <= t; i++){
		int N;
		priority_queue <pair <int, int> > que;

		fscanf(ifp, "%d", &N);
		
		for (int j = 1; j <= N; j++){
			int tmp;
			fscanf(ifp, "%d", &tmp);
			que.push(make_pair(tmp, j));
		}
		fprintf(ofp, "Case #%d: ", i);

		while (que.size()!=0){
			if (que.size() == 2 && que.top().first==1){
				pair <int, int> tmp[2];
				for (int k = 0; k < 2; k++){
					tmp[k] = que.top();
					que.pop();
				}
				fprintf(ofp, "%c%c\n", 'A' + tmp[0].second - 1, 'A' + tmp[1].second - 1);
			}
			else{
				if (que.size() == 2){
					pair <int, int> tmp = que.top();
					que.pop();
					if (tmp.first == que.top().first){
						pair <int, int> tmp2 = que.top();
						que.pop();
						tmp.first--;
						tmp2.first--;
						fprintf(ofp, "%c%c ", 'A' + tmp.second - 1, 'A' + tmp2.second - 1);
						if (tmp.second != 0){
							que.push(tmp);
							que.push(tmp2);
						}
						continue;
					}
					fprintf(ofp, "%c ", 'A' + tmp.second - 1);

					tmp.first--;
					if (tmp.first != 0){
						que.push(tmp);
					}
					continue;
				}
				pair <int, int> tmp = que.top();
				que.pop();

				fprintf(ofp, "%c ", 'A' + tmp.second - 1);

				tmp.first--;
				if (tmp.first != 0){
					que.push(tmp);
				}
			}
		}
	}

	fclose(ifp);
	fclose(ofp);

	return 0;
}