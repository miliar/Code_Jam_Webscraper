#include <stdio.h> 

int main(){
	FILE *fp;
	char fileName[] = "B-large.in",outputfileName[]="B-large.out";
	int i,j,k,t,status[101], a[100][100],m,n,row[100],col[100];

	if((fp=fopen(fileName, "r")) == NULL){
		printf("Can't read file");
		return -1;
   }

	fscanf(fp, "%d ",&t);
for(k=1;k<=t;++k){
	status[k] = 0;
	fscanf(fp, " %d %d", &m, &n);
	for(j=0;j<n;++j){
		col[j] = 0;
	}
	for(i=0;i<m;++i){
		row[i] = 0;
		for(j=0;j<n;++j){
			fscanf(fp, " %d", &a[i][j]);
			if(a[i][j] > row[i]){
				row[i] = a[i][j];
			}
			if(a[i][j] > col[j]){
				col[j] = a[i][j];
			}
		}
	}
	for(i=0;i<m;++i){
		for(j=0;j<n;++j){
			if(a[i][j] < row[i] && a[i][j] < col[j]){
					status[k] = 1;
					break;
			}
		}
		if(status[k] == 1){
			break;
		}
	}
}
fclose(fp);

	if((fp=fopen(outputfileName, "w")) == NULL){
		printf("Can't write file");
		return -1;
    }

for(k=1;k<=t;++k){
	if(status[k] == 1){
		fprintf(fp,"Case #%d: NO\n", k);
	}else{
		fprintf(fp,"Case #%d: YES\n", k);
	}
}
	fclose(fp);
	return 1;
}
