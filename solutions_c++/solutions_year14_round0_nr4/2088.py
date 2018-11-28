#include <iostream>

using namespace std;
int compare (const void * a, const void * b)
{
  if ( *(float*)a >  *(float*)b ) return -1;
  else if ( *(float*)a == *(float*)b ) return 0;
  else return 1;
}
int main(int argc, char *argv[]) {
	FILE *fptr = fopen("D-large.in", "r");
	FILE *ffptr = fopen("D-large.out", "w");
	int T, N, bestNaomi, bestKen,count,left;
	
	fscanf(fptr,"%d", &T);
	for (int k = 0; k < T; k++) {
		fscanf(fptr,"%d", &N);
		float Naomi[N], Ken[N];	
		for (int i = 0; i < N; i++) {
			fscanf(fptr, "%f", &Naomi[i]);
		}
		for (int i = 0; i < N; i++) {
			fscanf(fptr, "%f", &Ken[i]);
		}
		float minKen = 2, maxKen = -1;
		qsort (Ken, N, sizeof(float), compare);
		qsort (Naomi, N, sizeof(float), compare);
//		for (int i = 0; i < N; i++) {
//					cout << Naomi[i]<<" ";
//				}
//		cout << endl;
//		for (int i = 0; i < N; i++) {
//			cout << Ken[i]<<" ";
//		}
//		cout << endl;
		bestNaomi = 0;
		count = 0;
		left=0;
	
		while (count < N) {
			if(Naomi[left] > Ken[count]){
				left++;
				bestNaomi++;
			}
			count ++;
		}
		
		count = 0;
		left=0;
		bestKen = 0;
	
		while (count < N) {
			if(Ken[left] < Naomi[count]){
//				cout << Ken[left]<<"<"<<Naomi[count]<<endl;
				bestKen++;
			}
			else{
				left++;
			}
			count ++;
		}
//		cout << bestNaomi <<" " <<bestKen << endl;
		fprintf(ffptr, "Case #%d: %d %d\n", k+1, bestNaomi, bestKen);	
	}
}