#include <fstream>
#include <iostream>
#include <stdio.h>
using namespace std;

int T;
double C, F, X;
double cookieRate;
double t1, t2;
int cnt;
double tmp;

int main(){
	FILE* in = fopen("C:\\Users\\Jinhyuk\\Desktop\\CodeJam 2014\\Qual\\B-large.in", "r");
	FILE* out = fopen("C:\\Users\\Jinhyuk\\Desktop\\CodeJam 2014\\Qual\\testResult.txt", "w");
	
	fscanf(in, "%d", &T);
	for(int i=0; i<T; i++){
		cookieRate = 2;
		cnt = 0;
		fscanf(in, "%lf %lf %lf", &C, &F, &X);
		t1 = X/cookieRate;
		while(1){
			t2 = X/(cookieRate + F);	
			
			for(int j=0; j<=cnt; j++)
				t2 += C/(2+F*j);
			cookieRate += F;
			
			cnt++;
			if(t1 < t2) break;
			else t1 = t2;
		}
		fprintf(out, "Case #%d: %.7lf\n", i+1, t1);
	}
	fclose(in);
	fclose(out);
	return 0;
}

