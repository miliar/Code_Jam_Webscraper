#include <stdio.h>
#include <stdlib.h>


int getMax (int **Lawn, int n, int m, int no, int row){
	int i,max;
	if (row==1){
		max=Lawn[no][0];
		for (i=0; i<m; i++){
			if(Lawn[no][i] > max)	
				max = Lawn[no][i];
		}
	}
	else{
		max=Lawn[0][no];
		for (i=0;i<n;i++){
			if (Lawn[i][no]>max)
				max=Lawn[i][no];	
		}	
	}
	return max;
}

int compare (int **a, int **b, int n, int m){
	int i,j,check=1;
	for (i=0;i<n;i++)
		for (j=0;j<m;j++)
			if (a[i][j] != b[i][j]){
				check =0;
				break;	
			}
			return check;
}

void print(int **a, int n, int m){
	int i,j;
	printf("\n Array:\n");
	for (i=0; i< n; i++){
		for  (j=0;j<m;j++){
			printf("%d ", a[i][j]);	
		}	
		printf("\n");
	}	
}

int LawnMower (int **Lawn, int n, int m){
	int i,j,length,val;
	int **arr;
	
	arr = (int **)malloc(sizeof(int*)*n);
	for (i=0; i < n ;i++)
		arr[i] = (int *)malloc(sizeof(int)*m);
	
	for (i=0; i<n;i++){
		for (j=0;j<m;j++){
			arr[i][j]=100;	
		}	
	}		
	
	for (i=0; i<n;i++){
		length = getMax(Lawn,n,m,i,1);	
		for (j=0;j<m;j++){
			if (length <= arr[i][j])
			arr[i][j] = length;	
		}
	}
	
	for (j=0; j <m; j++){
		length = getMax(Lawn,n,m,j,0);
		for (i=0; i<n;i++){
			if (length <= arr[i][j])
				arr[i][j] = length;	
		}	
	}
	
	//print(arr,n,m);
	val = compare(Lawn,arr,n,m);
	free(arr);
	return val;
}



int main (int argc, char *argv[]){
	int n,m,t,i,j,test=1;
	
	
	FILE *ip =fopen("B-large.in", "r");
	
	FILE *op = fopen("outputLarge.txt","w");
	
	fscanf(ip,"%d", &t);
	while (test <= t){
		printf("test: %d\n", test);
		fscanf(ip,"%d %d", &n, &m);
		
		if (test==8)
			printf("n=%d m=%d\n", n,m);
		//int Lawn[n][m];
		int **Lawn = (int **)malloc(sizeof(int*)*n);
		
		if (test==8)
		printf("check point 1\n");
		
		for (i=0; i < n ;i++)
			Lawn[i] = (int *)malloc(sizeof(int)*m);
		
		for (i=0; i<n;i++)
			for(j=0;j<m;j++)
				{
					fscanf(ip,"%d", &Lawn[i][j]);
					if (test==8)
						printf("Lawn[%d][%d] = %d\n", i,j,Lawn[i][j]);
				}
		if (n==1 || m==1){
			fprintf(op,"Case #%d: YES\n", test++);
			continue;	
		}
		if (test==8)
		printf("check point 2\n");	
		if (LawnMower(Lawn,n,m))
			fprintf(op,"Case #%d: YES\n", test);
		else
			fprintf(op,"Case #%d: NO\n", test);

	
		test++;
		free(Lawn);
	}
	//system("PAUSE");
	return 0;
	//scanf("");
}
