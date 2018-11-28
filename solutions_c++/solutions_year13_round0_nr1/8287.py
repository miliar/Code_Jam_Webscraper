#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream input;
	ofstream output;
	
	input.open("input.txt", ios::in);
	output.open("output.txt", ios::out);
	
	int T;
	char game[4][4];
	bool dot;
	bool flag = false;
	char ref;
	int result; // 2 = X wins, 1 = O wins, 0 = not finished or draw
	
	input >> T;
	cout << T << endl;
	
	for(int a = 0; a < T; a++){
		result = 0;
		flag = false;
		dot = false;
		
        for(int i = 0; i<4; i++){
    		for(int j = 0; j<4; j++){
    			input >> game[i][j];
    			cout << game[i][j];
    			if(game[i][j] == '.'){
    				dot = true;
    			}
    		}
    		cout << endl;
    	}
    	cout << endl;
    	
		
		// checking horizontal and vertical
		for (int i = 0; i<4; i++){
			ref = game[i][i];
			if(ref != '.'){
				if(ref == 'T'){
					if(i==3){
						ref = game[i][i-1];
					}
					else{
						ref = game[i][i+1];
					}
				}
				// horizontal
				for(int j = 0; j<4; j++){
					cout << j << ' ';
					
					if (game[i][j] != ref && game[i][j] != 'T')
						break;
					if (j==3){
						result = 2;
						if( game[i][i] == 'O'){
							result = 1;
						}
					}
				}
				cout << result << endl;
				//vertical
				if(game[i][i] == 'T'){
					if(i==3){
						ref = game[i-1][i];
					}
					else{
						ref = game[i+1][i];
					}
				}
				if(result == 0){
					for(int j = 0; j<4; j++){
						if (game[j][i] != ref && game[j][i] != 'T')
							break;
						if(j==3){
							result = 2;
							if( ref == 'O'){
								result = 1;
							}
						}
					}
				}
				cout << result << endl;
			}
			else
				flag = true;
		}
		if(result == 0){
			// top left to bottom right
			if( flag == false){
				ref = game[0][0];
				if (ref == 'T')
					ref = game[1][1];
				for (int i = 0; i<4; i++){
					if (game[i][i] != ref && game[i][i] != 'T')
						break;
					if(i == 3){
						result = 2;
						if(ref == 'O')
							result = 1;
					}
				}
			}
			// top right to bottom left
			ref = game[0][3];
			if(ref != '.'){
    			if(ref == 'T')
    				ref = game[1][2];
    			for (int i = 0; i<4; i++){
    				if(game[i][3-i] != ref && game[i][3-i] != 'T')
    					break;
    				if(i==3){
    					result = 2;
    					if(ref == 'O')
    						result = 1;
    				}
    			}
            }
		}
		
		if(result == 2){
			output << "Case #" << a+1 << ": X won" << endl;
		}
		else if(result == 1){
			output << "Case #" << a+1 << ": O won" << endl;
		}
		else if(dot == true){
			output << "Case #" << a+1 << ": Game has not completed" << endl;
		}
		else{
			output << "Case #" << a+1 << ": Draw" << endl;
		}
	}
						
			
	
	
	
    system("PAUSE");
    return EXIT_SUCCESS;
}
