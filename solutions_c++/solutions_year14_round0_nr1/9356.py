#include<iostream>
#include<algorithm>
using namespace std;

void main(){
	int N;
	int aOne, aTwo;
	int gridOne[4][4], gridTwo[4][4];
	int x = 1;
	FILE *fpRead, *fpWrite;
	fopen_s(&fpRead, "A-small-attempt2.in", "r");
	fopen_s(&fpWrite, "output.txt", "w");
	fscanf_s(fpRead, "%d", &N);
	while (x <= N){
		int cnt = 0;
		int ans;
		fscanf_s(fpRead, "%d", &aOne);
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				fscanf_s(fpRead, "%d", &gridOne[i][j]);
			}
		}
		fscanf_s(fpRead, "%d", &aTwo);
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				fscanf_s(fpRead, "%d", &gridTwo[i][j]);
			}
		}
		int tempOne[4], tempTwo[4];
		for (int i = 0; i < 4; i++){
			tempOne[i] = gridOne[aOne - 1][i];
			tempTwo[i] = gridTwo[aTwo - 1][i];
		}
		sort(tempOne, tempOne + 4);
		sort(tempTwo, tempTwo + 4);
		int im = 0, j = 0;
		while (im < 4 && j < 4){
			if (tempOne[im] == tempTwo[j]){
				cnt++;
				ans = tempOne[im];
				if (cnt > 1)
					break;
				im++;
				j++;
			}
			else if (tempOne[im] < tempTwo[j]){
				im++;
			}
			else{
				j++;
			}
		}
		if (cnt == 1){
			fprintf_s(fpWrite, "Case #%d: %d\n", x, ans);
		}
		else if (cnt < 1){
			fprintf_s(fpWrite, "Case #%d: Volunteer cheated!\n", x);
		}
		else{
			fprintf_s(fpWrite, "Case #%d: Bad magician!\n", x);
		}
		x++;
	}
}