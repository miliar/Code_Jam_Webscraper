#include<iostream>
#include<vector>
#include<string.h>
#include<algorithm>
#include<fstream>
#include<stdio.h>
using namespace std;
bool descCmp(double i, double j){
	return i > j;
}
int main(){
	ifstream in("D-large.in");
	FILE *pFile = fopen("D.out", "w");
	int t, n, d, w;
	double reader;
	in >> t;
	for(int x = 1; x <= t; ++ x){
		vector<double> ken, naomi;
		d = w = 0;
		in >> n;
		for(int i = 0; i < 2*n; ++ i){
			in >> reader;
			if(i < n) naomi.push_back(reader);
			else ken.push_back(reader);
		}
		sort(naomi.begin(),naomi.end());
		sort(ken.begin(),ken.end());
		int front = 0;
		for(int i = 0; i < n; ++ i){
			if(naomi[i] > ken[front]){
				front++;
				d++;
			}
		}
		sort(naomi.begin(),naomi.end(),descCmp);
		sort(ken.begin(),ken.end(),descCmp);
		for(int i = 0; i < n; ++ i){
			if(ken[w] > naomi[i])
				w++;
		}
		fprintf(pFile, "Case #%d: %d %d\n", x, d, n - w);
	}
	return 0;
}