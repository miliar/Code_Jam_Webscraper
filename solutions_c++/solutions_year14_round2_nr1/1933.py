#include <bits/stdc++.h>
using namespace std;

FILE * saida;

string p[120];
set<char> chars[120];
vector<char> pc[120];
int totlet[120];
int let[120][120];

int media(int a, int b){
	int m = a/b;
	if(abs((m+1)*b -a) < abs(m*b - a))
		return m++;
	return m;
}

int main(int argc, char const *argv[]){
	//saida = stdout;
	saida = fopen("a.out", "w");
	int nc;
	scanf("%d", &nc);
	for(int caso = 1; caso <= nc; caso++){
		int n;
		scanf("%d", &n);
		for(int i = 0; i < 110; i++)
			totlet[i] = 0;
		for(int i = 0; i < n; i++){
			cin >> p[i];
			char last = '\0';
			pc[i].clear();
			for(int k = 0; k < p[i].size(); k++){
				if(p[i][k] != last){
					pc[i].push_back(p[i][k]);
					let[i][pc[i].size()-1] = 1;
					totlet[pc[i].size()-1]++;
					last = p[i][k];
				}
				else{
					let[i][pc[i].size()-1]++;
					totlet[pc[i].size()-1]++;
				}
			}
		}
		bool ok = true;
		for(int i = 0; i < n-1; i++){
			if(pc[i] != pc[i+1]){
				ok = false;
				break;
			}
		}
		if(!ok){
			fprintf(saida, "Case #%d: Fegla Won\n", caso);
		}
		else{
			int resp = 0;
			for(int i = 0; i < pc[0].size(); i++){
				int val = media(totlet[i], n);
				for(int k = 0; k < n; k++){
					resp += abs(val - let[k][i]);
				}
			}
			fprintf(saida, "Case #%d: %d\n", caso, resp);
		}
	}
	fclose(saida);
	return 0;
}