#include <fstream>
#include <iostream>
using namespace std;

int main(){
	ifstream read;
    read.open("input", ios::in);
    ofstream write;
    write.open ("output");

    int size;
    read>>size;
    int  **cases = new int*[size];
    for(int i = 0; i<size; i++){
    	cases[i] = new int[16];
    }
    for(int i = 0;i<size; i++){
 		for(int j = 0; j<16; j++){
 			cases[i][j]= -1;
 		}
 	}

    int index = 0;
    int count = 0;
    while (!read.eof()) {
    	char c;
    	read>>c;
    	
    	if(c=='\n'){
    		if(index== 15){
    			index = 0;
    			count++;
    		}
    		continue;
    	}
    	else if(c == 'X'){
    		cases[count][index] = 0;
    	}
    	else if(c == 'O'){
    		cases[count][index] = 1;
    	}
    	else if(c == 'T'){
    		cases[count][index] = 2;
    	}
    	else{
    		cases[count][index] = -1;
    	}
    	index++;
 	}
 	// for(int i = 0;i<size; i++){
 	// 	for(int j = 0; j<16; j++){
 	// 		write<<cases[i][j]<<" ";
 	// 	}
 	// 	write<<endl;
 	// }

 	bool *xFlag = new bool[size];
 	bool *oFlag = new bool[size];
 	for(int i = 0; i< size; i++){
		xFlag[i] = false;
 		oFlag[i] =false;
 	}

 	for(int i = 0; i < size; i++){
 		for(int k = 0; k<13 ; k = k+4){
 			//looking for horizontal X
 			if(cases[i][k] == 0 && cases[i][k+1] == 0 && cases[i][k+2] == 0 && cases[i][k+3] == 0)
 				xFlag[i] = true;
 			else if(cases[i][k] == 0 && cases[i][k+1] == 0 && cases[i][k+2] == 0 && cases[i][k+3] == 2)
 				xFlag[i] = true;
 			else if(cases[i][k] == 2 && cases[i][k+1] == 0 && cases[i][k+2] == 0 && cases[i][k+3] == 0)
 				xFlag[i] = true;
 			//looking for horizontal O
 			if(cases[i][k] == 1 && cases[i][k+1] == 1 && cases[i][k+2] == 1 && cases[i][k+3] == 1)
 				oFlag[i] = true;
 			else if(cases[i][k] == 1 && cases[i][k+1] == 1 && cases[i][k+2] == 1 && cases[i][k+3] == 2)
 				oFlag[i] = true;
 			else if(cases[i][k] == 2 && cases[i][k+1] == 1 && cases[i][k+2] == 1 && cases[i][k+3] == 1)
 				oFlag[i] = true;
 		}
 		for(int k =0 ; k<4 ; k++){
 			//looking for vertical X
 			if(cases[i][k] == 0 && cases[i][k+4] == 0 && cases[i][k +8] == 0 && cases[i][k+12] == 0)
 				xFlag[i] = true;
 			else if(cases[i][k] == 0 && cases[i][k+4] == 0 && cases[i][k +8] == 0 && cases[i][k+12] == 2)
 				xFlag[i] = true;
 			else if(cases[i][k] == 2 && cases[i][k+4] == 0 && cases[i][k +8] == 0 && cases[i][k+12] == 0)
 				xFlag[i] = true;
 			//looking for vertical O
 			if(cases[i][k] == 1 && cases[i][k+4] == 1 && cases[i][k+8] == 1 && cases[i][k+12] == 1)
 				oFlag[i] = true;
 			else if(cases[i][k] == 1 && cases[i][k+4] == 1 && cases[i][k+8] == 1 && cases[i][k+12] == 2)
 				oFlag[i] = true;
 			else if(cases[i][k] == 2 && cases[i][k+4] == 1 && cases[i][k+8] == 1 && cases[i][k+12] == 1)
 				oFlag[i] = true;
 		}
 		 			//looking for diagonal X
 			if(cases[i][0] == 0 && cases[i][5] == 0 && cases[i][10] == 0 && cases[i][15] == 0)
 				xFlag[i] = true;
 			else if(cases[i][0] == 0 && cases[i][5] == 0 && cases[i][10] == 0 && cases[i][15] == 2)
 				xFlag[i] = true;
 			else if(cases[i][0] == 2 && cases[i][5] == 0 && cases[i][10] == 0 && cases[i][15] == 0)
 				xFlag[i] = true;
 			else if(cases[i][3] == 0 && cases[i][6] == 0 && cases[i][9] == 0 && cases[i][12] == 0)
 				xFlag[i] = true;
 			else if(cases[i][3] == 0 && cases[i][6] == 0 && cases[i][9] == 0 && cases[i][12] == 2)
 				xFlag[i] = true;
 			else if(cases[i][3] == 2 && cases[i][6] == 0 && cases[i][9] == 0 && cases[i][12] == 0)
 				xFlag[i] = true;
 			//looking for diagonal O
 			if(cases[i][0] == 1 && cases[i][5] == 1 && cases[i][10] == 1 && cases[i][15] == 1)
 				oFlag[i] = true;
 			else if(cases[i][0] == 1 && cases[i][5] == 1 && cases[i][10] == 1 && cases[i][15] == 2)
 				oFlag[i] = true;
 			else if(cases[i][0] == 2 && cases[i][5] == 1 && cases[i][10] == 1 && cases[i][15] == 1)
 				oFlag[i] = true;
 			else if(cases[i][3] == 1 && cases[i][6] == 1 && cases[i][9] == 1 && cases[i][12] == 1)
 				oFlag[i] = true;
 			else if(cases[i][3] == 1 && cases[i][6] == 1 && cases[i][9] == 1 && cases[i][12] == 2)
 				oFlag[i] = true;
 			else if(cases[i][3] == 2 && cases[i][6] == 1 && cases[i][9] == 1 && cases[i][12] == 1)
 				oFlag[i] = true;
 	}
 	for(int i = 0; i<size; i++){
 		if(xFlag[i] == true && oFlag[i] == true)
 			write<<"Case #"<<i+1<<": Draw\n";
 		else if(xFlag[i] == true && oFlag[i] == false)
 			write<<"Case #"<<i+1<<": X won\n";
 		else if(xFlag[i] == false && oFlag[i] == true)
 			write<<"Case #"<<i+1<<": O won\n";
 		else if(xFlag[i] == false && oFlag[i] == false)
 		{
 			bool notComp = false;
 			for(int j= 0; j<16; j++){
 				if(cases[i][j] == -1){
 					notComp =true; 					
 				}
 			}		
 			if(!notComp)
 				write<<"Case #"<<i+1<<": Draw\n";
 			else
 				write<<"Case #"<<i+1<<": Game has not completed\n";
 		}
 			
 		
 	}
 		read.close();
 		write.close();
 			
	return 0;
}