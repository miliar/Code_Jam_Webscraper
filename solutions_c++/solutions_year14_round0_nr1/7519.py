#include<stdio.h>
#include<stdlib.h>

int mainfunc(FILE *fi,FILE *fo){
	int ans1, ans2, map1[10][10], map2[10][10];
	fscanf(fi,"%d", &ans1);
	for (int i = 0; i < 4; i++){
		for (int j = 0; j < 4; j++){
			fscanf(fi,"%d", &map1[i][j]);
		}
	}
	fscanf(fi,"%d", &ans2);
	for (int i = 0; i < 4; i++){
		for (int j = 0; j < 4; j++){
			fscanf(fi,"%d", &map2[i][j]);
		}
	}
	ans1--;
	ans2--;
	int more = 0,ret;
	for (int i = 0; i < 4; i++){
		for (int j = 0; j < 4; j++){
			if (map1[ans1][i] == map2[ans2][j]){
				ret = map1[ans1][i];
				more++;
			}
			if (more>1)return 0;
		}
	}
	if (more == 0)return -1;
	return ret;
}

int main(void){
	int T,ans;
	FILE *fi = fopen("A-small-attempt2.in", "r");
	FILE *fo = fopen("A-small-attempt2.out", "w");
	fscanf(fi,"%d", &T);
	for (int i = 0; i < T; i++){
		ans=mainfunc(fi,fo);
		fprintf(fo,"Case #%d: ", i + 1);
		if (ans == 0)fprintf(fo,"Bad magician!\n");
		else if (ans == -1)fprintf(fo,"Volunteer cheated!\n");
		else fprintf(fo,"%d\n", ans);
	}
}