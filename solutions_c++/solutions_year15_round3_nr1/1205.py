#include<iostream>
using namespace std;
int T, R, C, W;
FILE *fp1, *fp2;
int main(){
	fp1 = fopen("A-large.in", "r");
	fp2 = fopen("A-large.txt", "w");
	//cin >> T;
	fscanf(fp1, "%d", &T);

	for(int i =0; i<T; i++){
		fscanf(fp1, "%d %d %d", &R, &C, &W);
		//cin >> R >> C >> W;
		int start = W - 1; int curR = 0; int curC = 0;
		int res = 0;
		int checkNum = C / W;
		res += (R - 1) * checkNum;
		if (C % W == 0)
			res += checkNum + W - 1;
		else
			res += checkNum + W;
		fprintf(fp2, "Case #%d: %d\n", i + 1, res);
		//cout << "Case #" << i+1 << ": " << res << endl;
	}
}