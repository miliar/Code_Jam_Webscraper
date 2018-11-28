#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
FILE *in = fopen("large0.in", "r");
FILE *out = fopen("output.out", "w");
using namespace std;
int T, test;
vector<double> nao, ken, warNao, warKen;
double block;
int main(){
	int i, j, size, sizeWar;
	int naoWin = 0, naoWar = 0;
	fscanf(in, "%d", &T);
	test = T;
	while (T--){
		naoWin = naoWar = 0;
		fscanf(in, "%d", &size);
		nao.clear();
		ken.clear();
		nao.resize(size);
		ken.resize(size);
		sizeWar = size;
		for (i = 0; i < size; i++)
			fscanf(in, "%lf", &nao[i]);
		sort(nao.begin(), nao.end());
		warNao.assign(nao.begin(), nao.end());
		for (i = 0; i < size; i++)
			fscanf(in, "%lf", &ken[i]);
		sort(ken.begin(), ken.end());
		warKen.assign(ken.begin(), ken.end());
		do{
			if (nao[0] < ken[0]){
				nao.erase(nao.begin());
				ken.pop_back();
			}
			else{
				nao.erase(nao.begin());
				ken.erase(ken.begin());
				naoWin++;
			}
		} while (--size);
		do{
			if (warKen[sizeWar - 1] < warNao[sizeWar - 1]){
				warKen.erase(warKen.begin());
				warNao.pop_back();
				naoWar++;
			}
			else{
				for (i = 0; warNao[sizeWar - 1] > warKen[i]; i++)
					;
				warNao.pop_back();
				warKen.erase(warKen.begin() + i);
			}
		} while (--sizeWar);
		fprintf(out, "Case #%d: %d %d\n", test - T, naoWin, naoWar);
	}
	fcloseall();
	return 0;
}