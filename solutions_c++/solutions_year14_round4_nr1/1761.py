#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main(){
	int T, X, N, cases;
	vector<int> data;
	FILE *in = fopen("A-large.in", "r");
	FILE *out = fopen("output.txt", "w");
	fscanf(in, "%d", &T);
	cases = T;
	while (cases--){
		fscanf(in, "%d %d", &N, &X);
		data.resize(N);
		int i;
		for (i = 0; i < N; i++)
			fscanf(in, "%d", &data[i]);
		sort(data.begin(), data.end());
		int used = 0;
		int start = 0, end = N - 1, maxFromStart = -1;
		int flag = 0, stored = 0;
		while (stored < N && maxFromStart < end - 1){
			start = maxFromStart + 1;
			if (data[start] + data[end] <= X){
				maxFromStart = start++;
			}
			else{
				while (--start >= 0){
					if (data[start] + data[end] <= X && data[start] != 0){
						data[start] = data[end--] = 0;
						stored += 2;
						used++;
						break;
					}
				}
				if (start < 0){
					data[end--] = 0;
					stored++;
					used++;
				}
			}
		}
		start = 0;
		while (stored < N){
			while (end >= 0 && data[end] == 0){
				end--;
			}
			used++;
			stored++;
			data[end--] = 0;
			while (start < end && data[start] == 0){
				start++;
			}
			if (start <= end) stored++;
			data[start] = 0;
		}
		fprintf(out, "Case #%d: %d\n", T - cases, used);
	}
	fcloseall();
	return 0;
}