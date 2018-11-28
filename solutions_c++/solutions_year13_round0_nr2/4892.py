#include <stdio.h>
#include <set>

using namespace std;

typedef unsigned IT;

IT m[100][100], h[100], v[100];
set<int> s;

int main(){
	FILE* input = fopen("in.txt","r"),*output = fopen("out.txt","w");
	IT T;
	fscanf(input," %d ",&T);
	for(IT t=0;t<T;t++){
		fprintf(output,"Case #%d: ",t+1);
		IT I,J;
		fscanf(input," %d %d ",&I,&J);
		for(IT i=0;i<I;i++){
			for(IT j=0;j<J;j++){
				fscanf(input," %d ",&(m[i][j]));
			}
		}
		if(I == 1 || J == 1){
			goto ans_yes;
		}
		for(IT i=0;i<I;i++){
			h[i] = 1;
			for(IT j=0;j<J;j++){
				h[i] = max(h[i],m[i][j]);
			}
		}
		for(IT j=0;j<J;j++){
			v[j] = 1;
			for(IT i=0;i<I;i++){
				v[j] = max(v[j],m[i][j]);
			}
		}
		for(IT i=0;i<I;i++){
			for(IT j=0;j<J;j++){
				if(m[i][j] < h[i] && m[i][j] < v[j]){
					goto ans_no;
				}
			}
		}
		goto ans_yes;
ans_yes:
		fprintf(output,"YES");
		goto end;
ans_no:
		fprintf(output,"NO");
		goto end;
end:
		fprintf(output,"\n");
	}
	fclose(input);
	fclose(output);
	return 0;
}