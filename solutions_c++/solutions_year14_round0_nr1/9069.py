#include <stdio.h>
using namespace std;

int main(){
	FILE *in, *out;
	in = fopen("magic.in.txt", "r");
	out = fopen("magic.out.txt", "w");
	int t;
	fscanf(in, "%d", &t);
	int a, b;
	int seta[16];
	int setb[16];
	int valid[16];
	int ans = -1;
	for (int i = 0; i < t; i++){
		for (int j = 0; j < 16; j++){
			valid[j] = 0;
		}
		fscanf(in, "%d", &a);
		//fprintf(out, "%d\n", a);
		for(int j = 0; j < 16; j++){
			fscanf(in, "%d", &seta[j]);
		}
		//fprintf(out, "got this far\n");
		for(int j = 0; j < 4; j ++){
			//fprintf(out, "got this far\n");
			//fprintf(out, "about to access %d * 4 + %d = %d\n", a, j, a*4+j);
			//fprintf(out, "about to access %d - 1 = %d\n", seta[a*4+j], seta[a*4+j]-1);
			valid[seta[(a-1)*4+j]-1] ++;
			
		}
		fscanf(in, "%d", &b);
		for(int j = 0; j < 16; j++){
			fscanf(in, "%d", &setb[j]);
		}
		for(int j = 0; j < 4; j ++){
			valid[setb[(b-1)*4+j]-1] ++;
		}
		ans = -1;
		/*for(int j = 0; j < 16; j++){
			fprintf(out, "%d ", valid[j]);
		}
		fprintf(out, "\n");*/
		for (int j = 0; j < 16; j++){
			//fprintf(out, "ans = %d, valid[j] == 2 : %d\n", ans, valid[j] == 2);
			if(valid[j] == 2){
				if(ans == -1){ans = j;}
				else{ans = -2;}
			}
		}
		fprintf(out, "Case #%d: ", i+1);
		if(ans == -1){fprintf(out, "Volunteer cheated!\n");}
		else if(ans == -2){fprintf(out, "Bad magician!\n");}
		else{fprintf(out, "%d\n", ans+1);}
	}
	
	fclose(in);
	fclose(out);
	
	return 0;
}
