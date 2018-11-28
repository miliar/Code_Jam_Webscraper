
#include <iostream>;
using namespace std;

int main()

{

int T, max, F = 0;
FILE *in, *out;
char a[100];
in = fopen("input.txt", "r");
out = fopen("output.txt", "w");

fscanf(in, "%d", &T);

for (int i=1; i<=T; i++) {
    fscanf(in, "%d", &max);
    for (int j=0; j<1; j++) {
        fscanf(in, "%s", &a[j]);
    }
	int dif=0;
    for (int j=0; j<=max; j++) {
        //if (a[j] == '0') {
			
		int y=dif;
			for(int  k=0 ;k<=j;k++){
				y+=a[k]-'0';
			}
			if(y<=j){
            F++;
			dif++;
			}
        //}
    }
    if (i == T) {
        fprintf(out, "Case #%d: %d",i,F);
    }
    else {
        fprintf(out, "Case #%d: %d\n",i,F);
    }
    F = 0;
}
fclose(in);
fclose(out);
return 0;
}