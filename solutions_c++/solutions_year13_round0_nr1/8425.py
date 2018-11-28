#include <iostream>
#include <string>
#include <vector>

struct tab{
	std::vector<std::string> ligne;
};

int main(){
	int nbTestCase(0);
	bool xWin(false), yWin(false), nc(false);

	std::cin >> nbTestCase;
	std::vector<tab> cases;

	for(int i = 0 ; i < nbTestCase ; ++i){

		xWin = false;
		yWin = false;
		nc = false;

		cases.push_back(tab());
		std::string temp;

		for(int j = 0 ; j < 4 ; ++j){
			std::cin >> temp;
			cases[i].ligne.push_back(temp);

			for(int k = 0 ; k < 4 ; k++){
				if(cases[i].ligne[j][k] == '.'){
					nc = true;
					break;
				}
			}

			int winTemp = cases[i].ligne[j][0] + cases[i].ligne[j][1] + cases[i].ligne[j][2] + cases[i].ligne[j][3];

			if(winTemp ==  4 * 'X' || winTemp == 3 * 'X' + 'T')
				xWin = true;
			else if(winTemp == 4 * 'O' || winTemp == 3 * 'O' + 'T')
				yWin = true;

			if(xWin && yWin)
				break;
		}

		for(int j = 0 ; j < 4 ; ++j){
			int winTemp = cases[i].ligne[0][j] + cases[i].ligne[1][j] + cases[i].ligne[2][j] + cases[i].ligne[3][j];

			if(winTemp ==  4 * 'X' || winTemp == 3 * 'X' + 'T')
				xWin = true;
			else if(winTemp == 4 * 'O' || winTemp == 3 * 'O' + 'T')
				yWin = true;

			if(xWin && yWin)
				break;
		}

		int winTemp(0);

		for(int j = 0 ; j < 4 ; ++j){
			winTemp += cases[i].ligne[j][j];
		}

		if(winTemp ==  4 * 'X' || winTemp == 3 * 'X' + 'T')
			xWin = true;
		else if(winTemp == 4 * 'O' || winTemp == 3 * 'O' + 'T')
			yWin = true;

		winTemp = 0;

		for(int j = 0 ; j < 4 ; ++j){
			winTemp += cases[i].ligne[j][3 - j];
		}

		if(winTemp ==  4 * 'X' || winTemp == 3 * 'X' + 'T')
			xWin = true;
		else if(winTemp == 4 * 'O' || winTemp == 3 * 'O' + 'T')
			yWin = true;

		std::cout << "Case #" << i + 1 << ": ";

		if(xWin && !yWin)
			std::cout << "X won" << std::endl;
		else if(!xWin && yWin)
			std::cout << "O won" << std::endl;
		else if(xWin && yWin)
			std::cout << "Draw" << std::endl;
		else if(!xWin && !yWin){
			if(nc)
				std::cout << "Game has not completed" << std::endl;
			else
				std::cout << "Draw" << std::endl;
		}
	}
	return 0;
}