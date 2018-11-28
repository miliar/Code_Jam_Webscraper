#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

int compare (const void * a, const void * b){
	return ( *(int*)a - *(int*)b );
}

int main(){
	ifstream input("D-large.in");
	ofstream output("D-large.out");
	
	int t, cs = 1;
	input >> t;
	
	while(t--){
		int n;
		input >> n;
		
		float naomi[n], ken[n], temp[n];
		
		for(int i=0; i<n; i++)
			input >> naomi[i];
			
		for(int i=0; i<n; i++)
			input >> ken[i];
		
		qsort(naomi, n, sizeof(float), compare);
		qsort(ken, n, sizeof(float), compare);
		
		for(int i=0; i<n; i++)
			temp[i] = ken[i];
		/*
		output << endl;
		for(int i=0; i<n; i++)
			output << ken[i] << " ";
		
		output << endl;
		*/
		int n_deceit = 0, n_war = 0;
		int i, j;
		
		for(i=0; i<n; i++){
			int idx = -1;
			for(j=0; j<n; j++){
				if(naomi[i]>ken[j]){
					idx = 1;
					ken[j] = 1.0;
					break;
				}
			}
			if(idx==1)
				n_deceit++;
		}
		
		for(int i=0; i<n; i++)
			ken[i] = temp[i];
		
		for(i=n-1, j=n-1; i>=0; i--){
			if(naomi[i] > ken[j]){
				n_war++;
			} else {
				j--;
			}
		}
		
		output << "Case #" << cs << ": ";
		output << n_deceit << " " << n_war << endl;
		cs++;
	}
	
	return 0;
}
