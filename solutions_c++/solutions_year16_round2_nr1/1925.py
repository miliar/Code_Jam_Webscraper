#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>

#define INF 2000000000

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int TC;

int main(){
	scanf("%d", &TC);
	for(int Tn = 1; Tn <= TC; Tn++){
		printf("Case #%d: ", Tn);
		char num[3000];
		scanf("%s", &num);

		vi dig;
		int digl[11];
		int size = 0;


		for(int i = 0; i < strlen(num); i++){
			if(num[i] == 'X'){
				dig.push_back(6);
				size++;
			}
		}
		digl[6] = size;
		
		size = 0;
		for(int i = 0; i < strlen(num); i++){
			if(num[i] == 'Z'){
				dig.push_back(0);
				size++;
			}
		}
		digl[0] = size;
		
		size = 0;
		for(int i = 0; i < strlen(num); i++){
			if(num[i] == 'W'){
				dig.push_back(2);
				size++;
			}
		}
		digl[2] = size;
		
		size = 0;
		for(int i = 0; i < strlen(num); i++){
			if(num[i] == 'G'){
				dig.push_back(8);
				size++;
			}
		}
		digl[8] = size;

		size = 0;
		for(int i = 0; i < strlen(num); i++){
			if(num[i] == 'H'){
				size++;
				if(size > digl[8]){
					dig.push_back(3);
				}
			}
		}
		digl[3] = size - digl[8];
		
		size = 0;
		for(int i = 0; i < strlen(num); i++){
			if(num[i] == 'R'){
				size++;
				if(size > (digl[3] + digl[0])){
					dig.push_back(4);
				}
			}
		}
		digl[4] = size - digl[3] - digl[0];
		
		size = 0;
		for(int i = 0; i < strlen(num); i++){
			if(num[i] == 'F'){

				size++;
			if(size > digl[4]){
				dig.push_back(5);
			}
		}
		}
		digl[5] = size - digl[4];
		
		size = 0;
		for(int i = 0; i < strlen(num); i++){
			if(num[i] == 'V'){

				size++;
			if(size > digl[5]){
				dig.push_back(7);
			}
		}
		}
		digl[7] = size - digl[5];
		
		size = 0;
		for(int i = 0; i < strlen(num); i++){
			if(num[i] == 'O'){

				size++;
			if(size > (digl[2] + digl[4]+ digl[0])){
				dig.push_back(1);
			}
		}
		}
		digl[1] = size - digl[2] - digl[4] - digl[0];

		size = 0;
		for(int i = 0; i < strlen(num); i++){
			if(num[i] == 'I'){

				size++;
			if(size > (digl[5] + digl[6] + digl[8])){
				dig.push_back(9);
			
			}
		}
		}
		
		sort(dig.begin(), dig.end());
		for(int i = 0; i < dig.size(); i++){
			printf("%d", dig[i]);
		}
		printf("\n");

	}
}