#include <iostream>
#include <algorithm>
#define MAXN 1000
#define BUG system("pause")
#include <cstdio>
using namespace std; 
int main(void){
	int T;
	cin >> T;
	FILE *fp = fopen("out.txt", "w");
	for(int t=1; t<=T; ++t){
		double c, f, x;
		cin >> c >> f >> x;
		int farm = 0;
		double time = 0.0;
		double start = 2.0;
		while(x/start >= x/(start+f)+c/start){
			time += c/start;
			start += f;
		}
		time += x/start;
		fprintf(fp, "Case #%d: %.7lf\n", t, time);
		
	}
}
