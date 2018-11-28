#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>


using namespace std;

int main(){
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	
	scanf("%d", &T);

	for(int i =  1; i <= T; i++){
		//SMax
		int max;
		cin >> max;

		//SMax+1
		string ppl;
		cin >> ppl;

		int friends = 0;
		int standing = 0;

		for(int x = 0; x < max+1; x++){
			int pplInRow = ppl[x] - '0';

			if(x == 0){
				if(pplInRow == 0){
					friends++;
					standing++;
				}else{
					standing += pplInRow;
				}
			}else{
				if(standing < x){
					friends += x-standing;
					standing += x-standing;
				}

				standing += pplInRow;
			}
		}

		printf("Case #%d: %d\n", i, friends);
	}

	return 0;
}