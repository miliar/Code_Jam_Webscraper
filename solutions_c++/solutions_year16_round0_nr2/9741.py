// PanCake.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//


#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <math.h>
#include <string>


int main()

{


	int N, T;

	std::ifstream infile("a.txt");
	std::ofstream outfile("b.txt");

	infile >> T;
	for (int iy = 1; iy <= T; iy++) {

		bool stack[120],stack_temp[120];
		std::string input = "";
		infile >> input;

///		input = "+-";//////
		int len = input.size();
		for (int i = 0; i <=len; i++) {
			stack[i] = false;
		}

		for (int i = 0; i < len; i++) {
			if (input[i] == '+') 
				stack[len-i] = (stack[len-i] | (1 << i));
		}

		int done = 0;
		stack[done] = true;
		int swap = 0;
		while (done <len) {
			while (stack[done+1]) {
				done++;
				if (done == len) break;
			}

			if (done < len) {
				/////
				
				int topswapix = len;
				if (stack[topswapix] == true) {
					swap++;
					do{
						stack[topswapix] = false;
						topswapix--;
					} while (stack[topswapix] == true);
					
				}
				
				
				for (int j = done; j <= len; j++) { // copying and reversing to temp
					stack_temp[j]= stack[j]^1;

				}

				swap++;
				for (int j = done+1; j <= len; j++) { // copying and reversing to temp
					stack[j] = stack_temp[len-j+done+1];

				}
				for (int j = 1; j <= len; j++) { // copying and reversing to temp
//					std::cout << stack[j];					
				}
				std::cout << std::endl;

			}/////
			
		}





	
		//std::getline(infile,input);
		outfile << "case #" << iy << ": " << swap << std::endl;
		std::cout << "case #" << iy << ": " << swap << std::endl;
		
	
	}
	getchar();

	
	return 0;
}

