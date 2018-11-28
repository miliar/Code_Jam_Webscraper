#include <iostream>

int Rings (int r, int t){
	int rings = 0;
	while (t >= 0) {
		t = t - (2*r+1);
		r = r+2;
		rings++;
	}	
	return rings-1;
}


int main (int argc, char *argv){
	int testCase=1,T,t,r;
	FILE * ip = fopen("A-small-attempt1.in","r");
	fscanf(ip,"%d", &T);
	FILE * op = fopen("output11.txt","w");
	
	while (testCase <= T){
		fscanf(ip,"%d %d", &r, &t);
		fprintf(op,"Case #%d: %d\n", testCase,Rings(r,t));
		testCase++;
	}
	fclose(ip); 
	fclose (op);	
	//system("PAUSE");
	return 0;
}
