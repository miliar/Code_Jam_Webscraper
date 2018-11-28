#include "stdio.h"
#include "assert.h"
#include "time.h"
#include "stdlib.h"

#include <iostream>
#include <fstream>
#include <string>


#define DIMM 4

using namespace std;

int main(int argc, char* argv[])
{

	std::ifstream in("A-large.in");
    std::streambuf *cinbuf = std::cin.rdbuf();
    std::cin.rdbuf(in.rdbuf());

	std::ofstream out("A-large.out");
    std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!
	
	int testNum = 0;
	cin >> testNum;

	char mat[DIMM][DIMM] = {0};

	string s;

	for (int i = 0; i < testNum; i++){
		int emptyFieldsCnt = 0;

		for(int k = 0; k < DIMM; k++){
			cin >> s;
			for(int l = 0; l < DIMM; l++){
				mat[k][l] = s[l];
				if (s[l] == '.')
					emptyFieldsCnt++;
			}
		}

		int res = 0;

		for (int k = 0; k < DIMM; k++){
			int flag = 1;
			//X
			for (int l = 0; l < DIMM; l++){
				if (!((mat[k][l] == 'X' || mat[k][l] == 'T') && mat[k][l] != 'O' && mat[k][l] != '.')){
					flag = 0;
					break;
				}
			}

			if (flag){
				res = 1;
				break;
			}
			flag = 1;

			//O
			for(int l = 0; l < DIMM; l++){
				if (!((mat[k][l] == 'O' || mat[k][l] == 'T') && mat[k][l] != 'X' && mat[k][l] != '.')){
					flag = 0;
					break;
				}
			}

			if (flag){
				res = 2;
				break;
			}
			flag = 1;

			//X
			for(int l = 0; l < DIMM; l++){
				if (!((mat[l][k] == 'X' || mat[l][k] == 'T') && mat[l][k] != 'O' && mat[l][k] != '.')){
					flag = 0;
					break;
				}
			}

			if (flag){
				res = 1;
				break;
			}
			flag = 1;

			//O
			for(int l = 0; l < DIMM; l++){
				if (!((mat[l][k] == 'O' || mat[l][k] == 'T') && mat[l][k] != 'X' && mat[l][k] != '.')){
					flag = 0;
					break;
				}
			}

			if (flag){
				res = 2;
				break;
			}
			flag = 1;

			//X
			for(int l = 0; l < DIMM; l++){
				if (!((mat[l][l] == 'X' || mat[l][l] == 'T') && mat[l][l] != 'O' && mat[l][l] != '.')){
					flag = 0;
					break;
				}
			}

			if (flag){
				res = 1;
				break;
			}
			flag = 1;
			
			//X
			for(int l = 0; l < DIMM; l++){
				if (!((mat[l][DIMM-l-1] == 'X' || mat[l][DIMM-l-1] == 'T') && mat[l][DIMM-l-1] != 'O' && mat[l][DIMM-l-1] != '.')){
					flag = 0;
					break;
				}
			}

			if (flag){
				res = 1;
				break;
			}
			flag = 1;

			//O
			for(int l = 0; l < DIMM; l++){
				if (!((mat[l][l] == 'O' || mat[l][l] == 'T') && mat[l][l] != 'X' && mat[l][l] != '.')){
					flag = 0;
					break;
				}
			}

			if (flag){
				res = 2;
				break;
			}
			flag = 1;

			for(int l = 0; l < DIMM; l++){
				if (!((mat[l][DIMM-l-1] == 'O' || mat[l][DIMM-l-1] == 'T') && mat[l][DIMM-l-1] != 'X' && mat[l][DIMM-l-1] != '.')){
					flag = 0;
					break;
				}
			}

			if (flag){
				res = 2;
				break;
			}

			if (emptyFieldsCnt != 0)
				res = 3;

		}

		string resStr;
		switch (res){
		case 0:
			resStr = "Draw";
			break;
		case 1:
			resStr = "X won";
			break;
		case 2:
			resStr = "O won";
			break;
		case 3:
			resStr = "Game has not completed";
			break;
		default:
			break;
		}
		
		cout << "Case #" << i+1 << ": " << resStr << endl;

	}



/*	for (int k = 0; k < DIMM; k++)
	{
		for(int l = 0; l < DIMM; l++)
		{
			cout << mat[k][l];
		}
		cout << endl;
	}
	*/
	std::cin.rdbuf(cinbuf);

	std::cout.rdbuf(coutbuf);

    float time = ((float)clock()) / CLOCKS_PER_SEC;
    printf("profiling time: %f\n", time);

	system("pause");

	return 0;
}