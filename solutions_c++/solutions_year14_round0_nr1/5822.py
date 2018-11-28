#include <stdio.h>
int main()
{
	FILE *in =fopen ("input.txt","r");
	FILE *out =fopen ("output.txt","w");
	int T;
	int L1,L2;
	int A[5][5],B[5][5];
	fscanf(in,"%d",&T);
	for(int t=1;t<=T;t++){
		fscanf(in,"%d",&L1);
		for(int i=1;i<5;i++){
			for(int j=1;j<5;j++){
				fscanf(in,"%d",&A[i][j]);
			}
		}
		
		fscanf(in,"%d",&L2);
		for(int i=1;i<5;i++){
			for(int j=1;j<5;j++){
				fscanf(in,"%d",&B[i][j]);
			}
		}
		int cnt=0;
		int ans=0;
		for(int i=1;i<5;i++){
			for(int j=1;j<5;j++){
				if(A[L1][i] == B[L2][j]){
					cnt++;
					ans = A[L1][i];
				}
			}
		}
		if(cnt == 1){
			fprintf(out,"Case #%d: %d\n",t,ans);
		} else if(cnt == 0){
			fprintf(out,"Case #%d: Volunteer cheated!\n",t);
		} else {
			fprintf(out,"Case #%d: Bad magician!\n",t,ans);
		}
	}
	return 0;
}
