#include<iostream>
#include<vector>
using namespace std;
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("ouput.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++){
		int total = 0;
		printf("Case #%d: ", i + 1);
		vector<int> vec;
		int N;
		scanf("%d", &N);
		for (int j = 0; j < N; j++){
			int temp;
			scanf("%d", &temp);
			total += temp;
			vec.push_back(temp);
		}
		while (total >= 4){
			for (int j = 0; j < 2; j++){
				int f = 0;
				for (int k = 1; k < vec.size(); k++){
					if (vec[k] > vec[f]){
						f = k;
					}
				}
				printf("%c", 'A' + f);
				total--;
				vec[f]--;
			}
			printf(" ");
		}

		if (total == 3){
			int f = 0;
			for (int k = 1; k < vec.size(); k++){
				if (vec[k] > vec[f]){
					f = k;
				}
			}
			printf("%c ", 'A' + f);
			total--;
			vec[f]--;
		}
		int re[2], j = 0;
		for (int k = 0; k < vec.size()&&j<2; k++){
			if (vec[k] > 0){
				re[j] = k;
				j++;
			}
		}
		printf("%c%c\n", 'A' + re[0],'A'+re[1]);
	}
}