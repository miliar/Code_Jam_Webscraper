#include <iostream>

using namespace std;

int t,n,m;
int a[100][100];
int inrow[100];
int incol[100];

int main(){
	FILE * inp;
	FILE * outp;
	inp = fopen("input.in", "r");
	outp = fopen("output.txt", "w");

	fscanf(inp, "%d\n",&t);
	for(int i = 0; i < t; ++i){
		for(int h = 0; h < 100; h++){
			inrow[h] = 0;
			incol[h] = 0;
		}
		fscanf(inp, "%d %d\n",&n,&m);
		/*cout<<n<<" "<<m<<"\n";
		if((n == 1)||(m == 1)){
			fprintf(outp,"Case #%d: YES\n", i+1);
			continue;
		}*/
		for(int j = 0; j < n; ++j){
			for(int k = 0; k < m; ++k){
				fscanf(inp, "%d",&a[j][k]);
				if(a[j][k] > incol[k])
					incol[k] = a[j][k];
				if(a[j][k] > inrow[j])
					inrow[j] = a[j][k];
			}
		}
		bool p = 0;
		for(int j = 0; j < n; ++j){
			for(int k = 0; k < m; ++k){
				if((a[j][k] < incol[k])&&(a[j][k] < inrow[j])){
					p = 1;
					break;
				}
			}
			if(p)
				break;
		}
		if(p)
			fprintf(outp,"Case #%d: NO\n", i+1);
		else fprintf(outp,"Case #%d: YES\n", i+1);
	}
	fclose(inp);
	fclose(outp);
	return 0;
}