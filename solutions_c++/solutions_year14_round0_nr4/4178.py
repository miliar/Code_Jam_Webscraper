#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector> 
using namespace std;

int main (){
	int T;
	cin >>T;
	int truth[T];
	int deciet[T];
	for (int i=0; i < T; i++){
		int input_size;
		cin >> input_size;
		vector <double> naomi;
		vector <double> ken;
		vector <double>::iterator it_naomi;
		vector <double>::iterator it_ken;
		double val;
		for (int j =0; j< input_size; j++){
			scanf("%lf",&val);
			naomi.push_back(val);
		}
		for (int j =0; j< input_size; j++){
			scanf("%lf",&val);
			ken.push_back(val);
		}
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		/*
		   for (int k = 0 ; k < input_size ; k++){
		   cout << naomi.at(k)<<" ";
		   }
		   cout <<"\n";
		   for (int k = 0 ; k < input_size; k++){
		   cout << ken.at(k)<<" ";
		   }
		 */
		int count_win_naomi = 0;
		int index_naomi_start =0, index_naomi_end = input_size - 1;
		int index_ken_start =0, index_ken_end = input_size - 1;
		if (naomi[input_size - 1] < ken[0]){
			truth[i] = 0;
			deciet[i]=0;
		}else {
			for (int k =0; k < 2*input_size;){

				if (naomi[index_naomi_end] > ken[index_ken_end]){
					index_naomi_end--;
					index_ken_start++;
					count_win_naomi++;
					k+=2;
				}else if (naomi[index_naomi_end] < ken[index_ken_end]){
					index_ken_end--;
					index_naomi_end--;
					k+=2;
				}else if (naomi[index_naomi_start]> ken[index_ken_end]){
					count_win_naomi+=index_naomi_end - index_naomi_start + 1;
					break;	
				}

			}
		}


		truth[i] = count_win_naomi;	 

		int count_naomi_deceit =0; 
		int k_ken=0;
		for (int k =0; k<input_size;k++){
			if (naomi[k]<ken[k_ken]){
				continue;
			}else {
				count_naomi_deceit++;
				k_ken++;
			}
		}		
		deciet[i] = count_naomi_deceit;
	}

	for (int i =0; i< T; i++){
		printf("Case #%d: %d %d\n",i+1, deciet[i], truth[i]);
	}
} 
