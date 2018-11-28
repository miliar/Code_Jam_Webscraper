#include <stdio.h>

int compute(int row, int col){
	
	int Matrix[5][5]={{0,0,0,0,0},
					 {0,1,2,3,4},
					 {0,2,-1,4,-3},
					 {0,3,-4,-1,2},
					 {0,4,3,-2,-1}};

	return Matrix[row][col];
}

int trans(char a){
	if(a == '1')
		return 1;
	if(a == 'i')
		return 2;
	if(a == 'j')
		return 3;
	if(a == 'k')
		return 4;
}

void printPart(char *array,int i, int j){
	for(int k=i;k<=j;++k)
		printf("%c",array[k]);
	printf("\n");
}

int main(){
	int T;
	int g = 1;
	scanf("%d",&T);
	while(T--){
		int L, X,possible = 0;
		scanf("%d", &L);
		scanf("%d", &X);
		
		char array[L+1];
		scanf("%s",array);
		
		int num = L*X;
		int ipres = 0;
		int jpres = 0;
		int kpres = 0;
		int i,j,k;
		int minus = 0;
		int temp;
		
		if(num < 3){
			printf("Case #%d: %s",g,"NO");
			if(T!=0)
			printf("\n");
			g++;
			continue;
		}

		char array2[num];
		for(i = 0, j=0 ; i<num ; ++i){
			
				array2[i] = array[j];
				j++;
				if(j==(L)) j=0;
		}
		
		int res = 1;
		minus = 0;
		
		for(i = 0 ; i<num ; ++i){
			res = compute(res,trans(array2[i]));
			temp = res;
			if((minus%2==0?temp:-1*temp) == 2){
				ipres = 1;
				break;
			}

			if(res<0){
				minus++;
				res *=-1;
			}
			
		}
		if(i>=(num-1)){
			printf("Case #%d: %s",g,"NO");
			//if(T!=0)
			printf("\n");
			g++;
			continue;
		}

		//printPart(array2,0,i);
		res = 1;
		minus = 0;
		for(j = i+1 ; j<num ; ++j){
			res = compute(res,trans(array2[j]));
			temp = res;
			if((minus%2==0?temp:-1*temp) == 3){
				jpres = 1;
				break;
			}
			if(res<0){
				minus++;
				res *=-1;
			}
		}
		
		if(j>=(num-1)){
			printf("Case #%d: %s",g,"NO");
			if(T!=0)
			printf("\n");
			g++;
			continue;
		}
		//printPart(array2,i+1,j);
		res = 1;
		minus = 0;

		for(k = j+1 ; k<num ; ++k){
			res = compute(res,trans(array2[k]));
			temp = res;
			
			if(res<0){
				minus++;
				res *=-1;
			}
		}
		if((minus%2==0?res:-1*res)== 4){
				kpres = 1;
			}
		/*if(k>(num-1)){
			printf("Case #%d: %s",g,"NO");
			if(T!=0)
			printf("\n");
			g++;
			continue;
		}
		if(k<(num-1)){
			printf("Case #%d: %s",g,"NO");
			if(T!=0)
			printf("\n");
			g++;
			continue;
		}
		if(k == (num-1))
			kpres = 1;
		else
			kpres = 0;
			*/
		//printPart(array2,j+1,k);
		if(ipres==1 && jpres==1 && kpres==1)
			possible = 1;
		else
			possible = 0;

		printf("Case #%d: %s", g,possible?"YES":"NO");
		if(T!=0)
			printf("\n");
		g++;
	}

return 0;			
}