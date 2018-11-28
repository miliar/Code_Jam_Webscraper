// Round 1B
// Problem A Large

#include <stdio.h>
#include <algorithm>

int main(){
	int T,t,A,N, i,j, a[100], m,n,r;
	FILE *fi = fopen("al.in","r"),
		*fo = fopen("al.out","w");
	fscanf(fi,"%d\n",&T);
	for(t = 1; t <= T; t++){
		fprintf(fo,"Case #%d: ",t);
		fscanf(fi,"%d %d\n",&A,&N);
		for(i = 0; i < N; i++)
			fscanf(fi,"%d",a+i);
		std::sort(a, a+N);
		r = 0, m = 1000000000;
		for(i = 0; i < N; i++){
			if(N-i+r < m)
				m = N-i+r;
			if(A > a[i]){
				A += a[i];
				//printf("- i=%d A+=%d=%d\n",i,a[i],A);
			}else{
				n = A + A-1;
				//printf("-- i=%d a[i]=%d n=%d\n",i,a[i],n);
				if(n > a[i]){
					A = n + a[i];
					r++;
				}else{
					j = 1;
					while(n <= a[i]){
						j++;
						if(j > N-i){
							r += N-i;
							i = N;
							break;
						}
						n += n-1;
					}
					if(i < N){
						A = n + a[i];
						r += j;
					}
				}
				//printf("--- i=%d A=%d r=%d\n",i,A,r);
			}
		}
		fprintf(fo,"%d\n",r<m?r:m);
	}
	fclose(fi); fclose(fo);
	return 0;
}
