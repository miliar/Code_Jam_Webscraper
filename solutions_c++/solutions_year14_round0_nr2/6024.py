#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
	FILE * fin;
	FILE * fout;
	fin = fopen("input.txt", "r");
    fout = fopen("output.txt", "w");
	
	int T;
	
	fscanf(fin, "%d", &T);
	for(int i = 0 ; i < T ; i++){
		double C = 0, F = 0, X = 0;
		double ans = 0;
		double min = 0;
		
		fscanf(fin, "%lf %lf %lf", &C, &F, &X);
		min = X/2.0;
		if(X <= 2){
			ans = X/2.0;
			fprintf(fout, "Case #%d: %.7lf\n", i+1, ans);
			continue;
		} 
		
		double n = 0;
		double V = 2.0;
		
		while(ans <= min){
			ans = 0;
			for(int i = 0 ; i < n+1 ; i++){
				ans += C/(V+i*F);
			}		
			ans += X/(V+(n+1)*F);
			n++;
			if(min >= ans) min = ans;
		}
		fprintf(fout, "Case #%d: %.7lf\n", i+1, min);		
	}
	
	
	fclose(fin);
    fclose(fout);
	return 0;
}
