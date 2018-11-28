#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char ss[101];
char ts[101];
int sc[101][101] = {0};
int n;

int minus(int a, int b){
	if(a >= b)return a-b;
	else return b-a;
}

int main(){
	int t, i, j, l, k, count, ps, ps0, p;
	char tc;
	freopen("A-small-attempt0(1).in", "r", stdin);
	freopen("test.txt", "w", stdout);
	scanf("%d", &t);
	for(i=0; i<t; i++){
		int flag = 1;
		scanf("%d", &n);
		scanf("%s", ts);
		l = strlen(ts);
		tc = ts[0]; count = 1;ps0=0;
		for(k=1; k<l; k++){
			if(ts[k] != tc){
				ss[ps0] = tc;
				sc[0][ps0++] = count;
				count = 1;
				tc = ts[k]; 
			}else{
				count++;
			}
		}
		ss[ps0] = tc;
		sc[0][ps0++] = count;


		for(j=1; j<n; j++){
			scanf("%s", ts);
			l = strlen(ts);
			tc = ts[0]; count = 1;ps=0;
			for(k=1; k<l && flag; k++){
				if(ts[k] != tc){
					if(ss[ps] != tc)flag = 0;
					sc[j][ps++] = count;
					count = 1;
					tc = ts[k]; 
				}else{
					count++;
				}
			}
			if(ss[ps] != tc)flag = 0;
			sc[j][ps++] = count;
		}
		
//		printf("%s\n",ss);

/*		for(j=0; j<n; j++){
			for(k=0; k<ps; k++){
				printf("%d ",sc[j][k]);
			}
			printf("\n");
		}*/
		printf("Case #%d: ",i+1);
		if(ps != ps0)flag = 0;
		if(!flag)printf("Fegla Won\n");
		else{
			int min = 500000, sum = 0;
			for(j=0; j<n; j++){
				sum = 0;
				for(k=0; k<n; k++){
					if(j == k)continue;
					for(p=0; p<ps0; p++){
						sum += minus(sc[j][p],sc[k][p]);
					}
				}
				if(sum < min)min = sum;
			}
			sum = 0;
			for(k=0; k<n; k++){
				for(p=0; p<ps0; p++){
					sum += minus(1,sc[k][p]);
				}
			}
			if(sum < min)min = sum;
			printf("%d\n",min);
		}
	}	
	return 0;
}
