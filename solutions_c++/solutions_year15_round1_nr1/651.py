#include <cstdio>
#include <algorithm>
using namespace std;
const int NMax=1100;
int N,A[NMax];
int Ceil(int a,int b) {
	if(a%b==0) return a/b;
	return a/b+1;
}
int main()
{
	FILE *fin=fopen("input.txt","r"),*fout=fopen("output.txt","w");
	int T;
	fscanf(fin,"%d",&T);
	for(int I=1;I<=T;I++) {
		fscanf(fin,"%d",&N);
		int ret1=0,ret2=0,t=0;
		for(int i=1;i<=N;i++) {
			fscanf(fin,"%d",A+i);
			if(i>1&&A[i]<A[i-1]) {
				ret1+=A[i-1]-A[i];
				t=max(t,A[i-1]-A[i]);
			}
		}
	//	printf("%d\n",t);
		//getchar();getchar();	
		for(int i=1;i<=N;i++) {
			if(i>1) {
				if(A[i]<A[i-1]) {
					if(t>A[i-1]) ret2+=A[i-1];
					else ret2+=t;
				}else {
					if(t>A[i-1]) ret2+=A[i-1];
					else ret2+=t;
				}
 			}
		}
		fprintf(fout,"Case #%d: %d %d\n",I,ret1,ret2);
	}
	fclose(fin);fclose(fout);
	return 0;
}
