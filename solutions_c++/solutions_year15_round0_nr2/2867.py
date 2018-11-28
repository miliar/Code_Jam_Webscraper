#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

int T;

int main(){

	FILE *fin = fopen("input.txt", "r");
	FILE *fout = fopen("output.txt", "w");
	fscanf(fin,"%d", &T);
	for (int tc = 1; tc <= T; tc++){

		int answer = 99999;
		int D;
		int max_num = 0;
		vector<int> myV;
		fscanf(fin,"%d", &D);
		for (int i = 0; i < D; i++){
			int num;
			fscanf(fin,"%d", &num);
			myV.push_back(num);
			max_num = max(max_num, num);
		}
		for (int cnt = 1; cnt <= max_num; cnt++){
			int sum_ = 0;
			for (int i = 0; i < myV.size(); i++){

				if (myV[i] % cnt != 0)
					sum_ += myV[i] / cnt;
				else
					sum_ += myV[i] / cnt - 1;
			}
			answer = min(cnt + sum_, answer);
		}
		fprintf(fout, "Case #%d: %d\n", tc, answer);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}