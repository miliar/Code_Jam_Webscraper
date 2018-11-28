#include <cstdio>
#include <iostream>
#include <cstdlib>

using namespace std;

int count(const int &N, const int &i, int *index, int &index_count){
	if (N == 0) {
		return 0;
	}
	int tmp = N * i;
	while(tmp / 10 != 0 && index_count < 10) {
		int k = tmp % 10;
		//printf("%d", k);
		if (index[k] == 0) {
			index_count++;
			index[k] = 1;
		}
		tmp /= 10;
	}
	if (tmp != 0){
		//printf("%d", tmp);
		if (index[tmp] == 0) {
			index_count++;
			index[tmp] = 1;
		}
	}
	//printf("\n");
	if (index_count < 10){
		return count(N, i+1, index, index_count);
	} else {
		return N * i;
	}
}
void init(int *index, const int &n) {
	for(int i = 0; i < n; i++){
		index[i] = 0;
	}
}
int main(int argc, char const *argv[])
{
	int T, N;
	scanf("%d", &T);
	for(int i = 0; i < T; i++) {
		scanf("%d", &N);
		int index_count = 0, result;
		int *index = new int[10];
		init(index, 10);
		if ((result = count(N, 1, index, index_count))){
			printf("Case #%d: %d\n", i+1, result);
		} else {
			printf("Case #%d: INSOMNIA\n", i+1);
		}
		delete [] index;
	}
	return 0;
}