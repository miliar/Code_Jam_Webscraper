#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int T, currentCase = 0;
	scanf("%d", &T);
	while(T--) {
		currentCase++;
		int N;
		scanf("%d", &N);
		vector<double> Nao(N);
		vector<double> Ken(N);
		for(int i=0; i<N; i++){
			cin>>Nao[i];
		}
		for(int i=0; i<N; i++){
			cin>>Ken[i];
		}
		
		/*
		printf("Before sort\n");
		for(int i=0; i<N; i++) {
			cout<<Nao[i]<<"\t";
		}
		printf("\n");
		for(int i=0; i<N; i++) {
			cout<<Ken[i]<<"\t";
		}
		printf("\n");
		*/
		
		sort(Nao.begin(), Nao.end());
		sort(Ken.begin(), Ken.end());
		
		/*
		printf("After sort\n");
		for(int i=0; i<N; i++) {
			cout<<Nao[i]<<"\t";
		}
		printf("\n");
		for(int i=0; i<N; i++) {
			cout<<Ken[i]<<"\t";
		}
		printf("\n");
		*/
		// determine war score for Nao
		int warScore = 0;
		vector<double> tempKen = Ken;
		for (int i=N-1; i>=0; i--) {
			if(Nao[i] > tempKen[tempKen.size()-1]) {
				warScore++;
				tempKen.erase(tempKen.begin());
			} else {
				tempKen.pop_back();
			}
		}
		
		//determine deceit war score for Nao
		int deceitWarScore = 0, NaoL = 0, NaoR = N-1;
		int KenL = 0, KenR = N-1;
		while (NaoL <= NaoR) {
			if (Ken[KenR] > Nao[NaoR]) {
				NaoL++;
				KenR--;
			} else {
				NaoR--;
				KenR--;
				deceitWarScore++;
			}
		}
		printf("Case #%d: %d %d\n", currentCase, deceitWarScore, warScore);
	}
	return 0;
}