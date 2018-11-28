#include <stdio.h>
#include <string.h>

int main(){
	int i,j,t,n,n_case,last_seen,d,m,count;
	bool seen[11];
	scanf("%d",&t);
	for (i=0;i<t;i++){
		memset(seen, false, sizeof(seen));
		count = 0;
		scanf("%d",&n);
		n_case = n;
		for (j = 2; j <= 1000000; j++){
			//printf("%d, ",seen[j]);
			last_seen = n_case;
			do{
				d = n_case/10;
				m = n_case%10;
				if (!seen[m]){
					seen[m] = true;
					count++;
				}
				//printf("d: %d, m: %d\n",d,m );
				n_case = d;
			}while(d!=0);
			//printf("n: %d, j:%d, count: %d\n", n_case,j,count);
			if (count==10){
				break;
			}
			n_case = n*j;
		}
		if (count==10){
			printf("Case #%d: %d\n",i+1, last_seen);
		}else{
			printf("Case #%d: INSOMNIA\n",i+1);
		}
	}
	return 0;
}