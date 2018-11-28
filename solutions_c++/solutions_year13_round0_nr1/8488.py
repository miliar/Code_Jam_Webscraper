#include <iostream>
#include <cstdlib>
#include <fstream>
using namespace std;

//char board[4][4];
unsigned int victory[10];
unsigned int xb;
unsigned int ob;
ofstream fout("A-small-attempt0.out");
void init()
{
	victory[0] = 0xF000;
	victory[1] = 0x0F00;
	victory[2] = 0x00F0;
	victory[3] = 0x000F;
	victory[4] = 0x8888;
	victory[5] = 0x4444;
	victory[6] = 0x2222;
	victory[7] = 0x1111;
	victory[8] = 0x8421;
	victory[9] = 0x1248;
}
int checkWinLose()
{
	
	for(int i=0; i < 10; i++ ){
		if( (xb & victory[i]) == victory[i] ){
			return 0;
		}
	}
	for(int i=0; i < 10; i++ ){
		if( (ob & victory[i]) == victory[i] ){
			return 1;
		}
	}
	if( (xb | ob) != 0xFFFF ){	//full board, draw
		
		return 3;
	}
	else{	//not completed
		return 2;
	} 
}
int main()
{
	xb = 0;
	ob = 0;
	int num;
	char board[4][4];
	init();
	//memset(board, 0, sizeof(board) );
	cin >> num;
	char symbol;
	for( int i=0 ; i<num ; i++ ){
		xb = 0;
		ob = 0;
		for( int j=0; j<16 ; j++ ){
			cin >> symbol;
			if(symbol == 'X' ){
				xb <<= 1;
				xb ++;
				ob <<= 1;
			}
			else if(symbol == 'O') {
				ob <<= 1;
				ob ++;
				xb <<= 1;
			}
			else if(symbol == 'T'){
				xb <<= 1;
				xb ++ ;
				ob <<= 1;
				ob ++ ;
			}
			else if( symbol == '.' ){
				ob <<= 1;
				xb <<= 1;
			}
		}
		//cout << "xb " << xb << "  ob " << ob << endl;
		if( checkWinLose()==0 ){		//X won
			fout << "Case #" << i+1 << ": X won" << endl;
		}
		else if( checkWinLose()==1 ){	//O won
			fout << "Case #" << i+1 << ": O won" << endl;
		}
		else if( checkWinLose()==2 ){	// Draw
			fout << "Case #" << i+1 << ": Draw" << endl;
		}
		else if( checkWinLose()==3 ){	//not completed
			fout << "Case #" << i+1 << ": Game has not completed" << endl;
		}
		
	}
	system("pause");
	return 0;
}
