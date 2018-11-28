#include <cstdio>

using namespace std;
 
int t, n;

int main(){
	FILE *input, *output;
	input = fopen("A-small-attempt1.in", "r");
	output = fopen("A-small-output.txt", "w");
	fscanf(input, "%d", &t);
	for(int i = 1; i <= t; i++){
		fscanf(input, "%d", &n);
		fprintf(output, "Case #%d: ", i);
		if(n <= 200){
			bool a[10], flag;
			int j;
			for(j = 0;j < 10; j++){
				a[j] = false;
			}
			j = 0;
			while(true){
				j++;
				flag = true;
				for(int k = n*j; k > 0; k /= 10){
					a[k%10] = true;
				}
				if(j > 100){
					fprintf(output, "INSOMNIA\n");
					break;
				}
				for(int k = 0; k < 10 && flag; k++){
					if(!a[k]) flag = false;
				}
				if(flag){
					fprintf(output, "%d\n", n*j);
					break;
				}
			}
		}
	}
	fclose(input);
	fclose(output); 
	return 0;
}
