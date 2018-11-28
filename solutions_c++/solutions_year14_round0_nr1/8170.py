//#include "cute_algostudy.h"

#include <string>
#include <vector>
#include <iostream>

//namespace code_jam_2014_0_a {

int main(){
	int T;
	std::cin >> T;

	for(int i = 0; i < T; ++i){

		int answerRow;

		std::cin >> answerRow;
		int firstRows[4];
		int tmp[4];
		for(int j = 1; j <= 4; ++j){
			if(j == answerRow){
				std::cin >> firstRows[0] >> firstRows[1] >> firstRows[2] >> firstRows[3];
			}else{
				std::cin >> tmp[0] >> tmp[1] >> tmp[2] >> tmp[3];
			}
		}

		std::cin >> answerRow;
		int secondRows[4];
		for(int j = 1; j <= 4; ++j){
			if(j == answerRow){
				std::cin >> secondRows[0] >> secondRows[1] >> secondRows[2] >> secondRows[3];
			}else{
				std::cin >> tmp[0] >> tmp[1] >> tmp[2] >> tmp[3];
			}
		}

		std::vector<int> answer;
		for(int j = 0; j < 4; ++j){
			for(int k = 0; k < 4; ++k){
				if(firstRows[j] == secondRows[k]){
					answer.push_back(firstRows[j]);
				}
			}
		}

		std::cout << "Case #" << i+1 << ": ";
		if(answer.empty()){
			std::cout << "Volunteer cheated!" << std::endl;
		}else if(answer.size() > 1){
			std::cout << "Bad magician!" << std::endl;
		}else if(answer.size() == 1){
			std::cout << answer[0] << std::endl;
		}

	}

	return 0;
}

//CUTE_MAIN(__FILE__, main);

//}
