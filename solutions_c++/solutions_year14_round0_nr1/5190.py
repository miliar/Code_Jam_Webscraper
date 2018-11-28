/******************************************************************************************
*           .--.																		  *
* ::\`--._,'.::.`._.--'/::			@author Ana M. Mihut	@course GCJ					  *
* ::::. `  __::__ ' .:::::			@alias  LT-Kerrigan		@date   11.04.2014			  *
* ::::::-:.`'..`'.:-::::::			@link   https://code.google.com/codejam/		      *
* ::::::::\ `--' /::::::::			@detail	Magic trick ;]								  *
*																						  *
*******************************************************************************************/

#include <fstream>
#include <vector>
#include <iostream>
#include <limits>
#include <string>

int Check(int* a, int* b){
	int check[4] = { 0 };
	int answer;

	for (int i = 0; i < 4; i++){
		for (int j = 0; j < 4; j++){
			if (a[i] == b[j]){
				check[i] = 1;
				answer = a[i];
			}
		}
	}

	int count = 0;
	for (int i = 0; i < 4; i++){
		if (check[i] == 1){
			count++;
		}
	}
	if (count == 1) return answer;
	else if (count == 0) return 0;
	else if (count > 1) return -1;

}

int main(){

	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A.out", "w", stdout);
	
	int T;
	std::cin >> T;

	for (int i = 0; i < T; i++){
		printf("Case #%d: ", i+1);

		int a1, a2;
		int r1[16];
		int sr1[4];
		int r2[16];
		int sr2[4];

		std::cin >> a1;
		int count = 0;
		for (int i = 0; i < 16; i++){
			std::cin >> r1[i];
			
			if (i >= (a1 - 1)*4 && i <= ((a1 - 1)*4)+3){
				sr1[count] = r1[i];
				count++;
			}
		}

		std::cin >> a2;
		int count2 = 0;
		for (int i = 0; i < 16; i++){
			std::cin >> r2[i];
			

			if (i >= (a2 - 1) * 4 && i <= ((a2 - 1) * 4) + 3){
				sr2[count2] = r2[i];
				count2++;
			}
		}

		int result = Check(sr1, sr2);
		if (result == -1){
			std::cout << "Bad magician!";
		}
		else if (result == 0){
			std::cout << "Volunteer cheated!";
		}
		else{
			std::cout << result;
		}
		printf("\n");
	}

}
