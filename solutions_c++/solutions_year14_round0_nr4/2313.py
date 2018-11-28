#include <stdio.h>
#include <algorithm>

int main(){
	int T;

	FILE *fi = fopen("D-large.in", "r");
	FILE *fo = fopen("output.txt", "w");
	fscanf(fi,"%d", &T);

	for (int i = 1; i <= T; i++){
		double naomi[1001] = { 0, }, ken[1001] = { 0, };
		int n;
		fscanf(fi,"%d", &n);
		for (int j = 0; j < n; j++)
			fscanf(fi,"%lf", &naomi[j]);
		for (int j = 0; j < n; j++)
			fscanf(fi,"%lf", &ken[j]);
		std::sort(naomi, naomi + n);
		std::sort(ken, ken + n);
		int pnta = 0, pntb = 0;
		int chn[1001] = { 0, }, chk[1001] = { 0, };

		for (int j = 0; j < n; j++){
			
			for (int k = 0; k < n; k++){
				if (chk[k] == 0 && naomi[j]>ken[k]){
					pnta++;
					chn[j]++;
					chk[k]++;
					break;
				}
				else if (chk[k]==0&&naomi[j] < ken[k]){
					chn[j]++;
					for (int l = n - 1; l >= 0; l--){
						if (chk[l] == 0)
						{
						chk[l]++;
						break;
						}
					}
					break;
				}
			}
		}



			int chnn[1001] = { 0, }, chkk[1001] = { 0, };
			for (int j = n - 1; j >= 0; j--){
				
				for (int k = 0; k < n; k++){
					int t;
					for (int l = n - 1; l >= 0; l--){
						if (chkk[l] == 0)
						{
							t = l;
							break;
						}
					}
					if (chkk[k] == 0 && naomi[j]<ken[k]){
						chkk[k]++;
						chnn[j]++;
						break;
					}
					else if (naomi[j] > ken[k] && k == t){
						for (int l = 0; l < n; l++){
							if (chkk[l] == 0){
								chkk[l]++;
								break;
							}
						}
						chnn[j]++;
						pntb++;
						break;
					}
				}
			}
			fprintf(fo,"Case #%d: %d %d\n", i, pnta, pntb);
		}

	return 0;
}
