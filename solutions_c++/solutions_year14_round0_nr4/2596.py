#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;

double Naomi[1008],Ken[1008];

int main(){
	fstream mcout,mcin;
	mcout.open("d:\\data.txt",ios::out);
	mcin.open("d:\\D-large.in",ios::_Nocreate);

	int T;
	mcin>>T;

	int N;
	for(int i=1; i<=T; i++){
		mcin>>N;
		for(int j=0; j<N; j++) mcin>>Naomi[j];
		for(int j=0; j<N; j++) mcin>>Ken[j];
		
		//≈≈–Ú
		sort(Naomi,Naomi+N);
		sort(Ken,Ken+N);

		//decit
		int pmi,pken,ori,after;
		pmi = pken = 0;
		ori = after = N;

		while(pken < N){
			while(Ken[pken] < Naomi[pmi]) pken++;
			if(pken < N){
				ori -= 1; 
				pken++;
				pmi++;
			}
		}
		pmi = 0;
		pken = N-1;
		int pkens = 0;
		while(pmi < N ){
			if(Naomi[pmi] > Ken[pkens]){
				pmi++;
				pkens++;
			}
			else{
				pken--; pmi++;
				after--;
			}
			
		}
		mcout<<"Case #"<<i<<": "<<after<<" "<<ori<<endl;
	}
}