#include<stdio.h>
#include<string.h>

int lawn[100][100];
int result[100];

FILE *in;
FILE *out;
int main(){

	int t, i, j, test, n, m, temp;
	int val, res1=0, res2=0;
	
	in = fopen("B-large.in", "r");
	out = fopen("B-large.out", "w");

	fscanf(in, "%d", &t);

	for(test=0 ; test< t ; test++){
		memset(lawn, NULL, 10000*sizeof(int));

		fscanf(in, "%d", &n);
		fscanf(in, "%d", &m);

		for(i=0 ; i < n ;i++){
			for(j=0 ; j< m ; j++)
				fscanf(in, "%d", &lawn[i][j]);
		}

		for(i=0 ; i < n ; i++){
			for(j=0 ; j< m; j++){
				val = lawn[i][j];
				lawn[i][j] = 0;
				for(temp = 0; temp<n ; temp++){
					if(val < lawn[temp][j])
						res1 = 1;		
				}
				for(temp = 0 ; temp<m ; temp++){
					if(val < lawn[i][temp])
						res2 = 1;
				}
				lawn[i][j] = val;
				if(res1 == 1 && res2 == 1)
						result[test] = 1;
				res1 = 0;
				res2 = 0;
			}
		}
	}

	for(test=0 ; test < t; test++){
		fprintf(out, "Case #%d: ", test+1);
		switch(result[test]){
		case 0 : 
			fprintf(out, "YES\n");
			break;
		case 1:
			fprintf(out, "NO\n");
			break;
		}
	}

	fclose(in);
	fclose(out);

	return 0;
}