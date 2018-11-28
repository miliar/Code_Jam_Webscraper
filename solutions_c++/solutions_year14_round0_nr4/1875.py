#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <fstream>

using namespace std;
double eps = 1e-7;
int main()
{
	int t;
	//ifstream fin("B-small-attempt0.in");
	FILE *in, *out;
	in = fopen("D-large.in", "r");
	out = fopen("D-large.out", "w");
	//ifstream fin("in.txt");
	//fin >> t;
	fscanf(in, "%d\n", &t);
	//ofstream fout("B-small-attempt0.out");
	for (int test = 1; test <= t; test++) {
		int n;
		fscanf(in, "%d\n", &n);
		vector<double> nao, ken;
		double cur;
		for (int i=0; i < n; i++) {
			fscanf(in, "%lf", &cur);
			nao.push_back(cur);
		}
		for (int i=0; i < n; i++) {
			fscanf(in, "%lf", &cur);
			ken.push_back(cur);
		}
		sort(nao.begin(), nao.end());
		sort(ken.begin(), ken.end());
		int i=0, j=0;
		int ken_p = 0, nao_p = 0;
		while (i < n) {
			while (i < n && nao[i] < ken[j] - eps) {
				i++;
			}
			ken_p += i;
			j++;
			if (i < n) {	
				nao_p++;
				i++;
			}
		}
		int real_nao_p = 0;
		i = n-1;
		j = n-1;
		while (i >= 0) {
			while (i >= 0 && nao[i]  - eps> ken[j]) {
				i--;
				real_nao_p ++;
			}			
			j--;
			if (i >= 0 ) {	
				i--;
			}
		}
				
		fprintf(out, "Case #%d: %d %d\n", test,  nao_p, real_nao_p);
	//	fout << "Case #%" << test << ": " << time << endl;
	}
	//fout.close();
	return 0;
}
