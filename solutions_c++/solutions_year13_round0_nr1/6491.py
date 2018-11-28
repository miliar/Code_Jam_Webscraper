#include <iostream>
#include <string>

char g_line[256];

class Case{
public:
	Case()
	{
		for(int i = 0; i < 4; ++i){
			std::cin.getline(g_line, 256);
			for(int j = 0; j < 4; ++j){
				c[i][j] = g_line[j];
			}
		}
		
		std::cin.getline(g_line, 256);	//Skip blank line
	}
	
	bool finished(){
		for(int i = 0; i < 4; ++i){
			for(int j = 0; j < 4; ++j){
				if(c[i][j] == '.'){
					return false;
				}
			}
		}
		return true;
	}
	
	// return true if win
	bool process(char u){
		int win, i, j;
		win = i = j = 0;
		

			//print(m[mc]);
			// check column
			for(i = 0; i < 4; ++i){
				win = 0;
				for(j = 0; j < 4 && (c[i][j] == u || c[i][j] == 'T'); ++j){
					win++;
				}
				if(win == 4){
					//std::cout << "Straight: {" << i << "," << j << "|" << mc << "}" << std::endl;
					return true;
				}
			}

			// check row
			for(i = 0; i < 4; ++i){
				win = 0;
				for(j = 0; j < 4 && (c[j][i] == u || c[j][i] == 'T'); ++j){
					win++;
				}
				if(win == 4){
					//std::cout << "Straight: {" << i << "," << j << "|" << mc << "}" << std::endl;
					return true;
				}
			}

			
			// check diagonal
			win = 0;
			for(i = 0; i < 4; ++i){
				for(j = 0; j < 4; ++j){
					if(i==j && (c[i][j] == u || c[i][j] == 'T')){
						win++;
					}
				}
			}
			if(win == 4){
				//std::cout << "Diagonal 1: {" << i << "," << j << "|" << mc << "}" << std::endl;
				return true;
			}
			
			// check diagonal
			win = 0;
			for(i = 0; i < 4; ++i){
				for(j = 0; j < 4; ++j){
					if(i==(3-j) && (c[i][j] == u || c[i][j] == 'T')){
						win++;
					}
				}
			}
			if(win == 4){
				//std::cout << "Diagonal 2: {" << i << "," << j << "|" << mc << "}" << std::endl;
				return true;
			}
		
		
		return false;
	}
	
private:
	char c[4][4];
	int row, col;
};

int main(){
	
	std::cin.getline(g_line, 256);
	int t_cases = atoi(g_line);
	
	for(int t = 0; t < t_cases; ++t){
		Case c;
		
		if(c.process('X')){
			std::cout << "Case #" << t+1 << ": " << "X won" << std::endl;
		}else if(c.process('O')){
			std::cout << "Case #" << t+1 << ": " << "O won" << std::endl;
		}else if(c.finished()){
			std::cout << "Case #" << t+1 << ": " << "Draw" << std::endl;
		}else{
			std::cout << "Case #" << t+1 << ": " << "Game has not completed" << std::endl;
		}
	}
	
}
//EOF
