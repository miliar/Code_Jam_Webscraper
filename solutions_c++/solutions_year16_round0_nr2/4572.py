#include<iostream>
using namespace std;

int main() {
	FILE *fin, *fout;
	fin = fopen("B-large.in", "r");
	fout = fopen("B-large.out", "w");
	int Cases, cnt;
	char data[111], flag;
	fscanf(fin, "%d", &Cases);
	for( int i=1; i<=Cases; ++i ) {
		cnt = 0;
		fscanf(fin, "%s", data);
		flag=data[0];
		for( int j=0; data[j]; ++j ) {
			if(data[j]!=flag){
				flag=data[j];
				cnt+=1;
			}
		}
		if(flag=='-'){
			cnt+=1;
		}
		fprintf(fout, "Case #%d: %d\n", i, cnt); 
	}
	return 0;
}
