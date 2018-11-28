#include <cstdio>
#include <string>
using namespace std;
void input(int A[4][4]){
	for(int i = 0; i < 4; ++i)
		for(int j = 0; j < 4; ++j)
			scanf("%3d", &A[i][j]);
}
void output(int A[4][4]){
	for(int i = 0; i < 4; ++i){
		for(int j = 0; j < 4; ++j)
			scanf("%3d ", &A[i][j]);
		printf("\n");
	}
}

int main(){
	string sample_i {"sample"};
	string small_i {"A-small-attempt1"};
	string large_i {"A-large-practice"};
	freopen((small_i+".in").c_str(), "r", stdin);
	freopen((small_i+".out").c_str(), "w", stdout);
	int N, arrang1[4][4], arrang2[4][4], c1, c2, result[4][4], count, indexi = 0, indexj = 0;
	scanf("%6d", &N);
	for(int x = 0; x < N; ++x){
		count = 0;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				result[i][j]=0;
		scanf("%3d", &c1);
		input(arrang1);
		scanf("%3d", &c2);
		input(arrang2);
		c1--;c2--;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; ++j){
				if(arrang1[c1][i] == arrang2[c2][j]){
					indexi = arrang1[c1][i]/4;
					indexj = arrang1[c1][i]%4-1;
					if(!indexj){
						indexi--;
						indexj=4;
					}
					result[indexi][indexj]++;
				}
			}
		}
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; ++j)
				count += result[i][j];
		if(count > 1)
			printf("Case #%d: Bad magician!\n", x+1);
		else if(count < 1)
			printf("Case #%d: Volunteer cheated!\n", x+1);
		else
			for(int i = 0; i < 4; i++)
				for(int j = 0; j < 4; ++j)
					if(result[i][j])
						printf("Case #%d: %d\n", x+1, i*4+j+1);
	}
	return 0;
}
