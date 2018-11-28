#include <cstdio>
using namespace std;
FILE* in=stdin;
FILE* out=stdout;
long long n, cur, curcpy, curcpycpy, total;
bool seen[10];

int main(){
	fscanf(in, "%lld", &n);
	for(long long i=0; i<n; i++){
		for(int ii=0; ii<10; ii++)
			seen[ii]=false;
		total=0;
		fscanf(in, "%lld", &cur);
		for(long long ii=1; total!=10 && ii<100; ii++){
			curcpy=ii*cur;
			curcpycpy=curcpy;
			while(curcpy){
				if(!seen[curcpy%10]){
					seen[curcpy%10]=true;
					total++;
				}
				curcpy/=10;
			}
		}
		if(curcpycpy==0)
			fprintf(out, "Case #%lld: INSOMNIA\n", i+1);
		else
			fprintf(out, "Case #%lld: %lld\n", i+1, curcpycpy);
	}
}
