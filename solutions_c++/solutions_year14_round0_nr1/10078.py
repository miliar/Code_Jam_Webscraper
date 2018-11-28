#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

using namespace std;

int main(int argc, char *argv[]) {
	
   short int karty1[4][4], karty2[4][4], w1, w2;
   int T;
   
   cin >> T;
   
   for(int c=1; c<=T; c++)
   {
	cin >> w1;
	w1--;
	
	for(int w=0; w<4; w++)	
	 for(int k=0; k<4; k++)
	  cin >> karty1[w][k];	
	
		
	cin >> w2;
	w2--;
	
	for(int w=0; w<4; w++)	
	 for(int k=0; k<4; k++)
	  cin >> karty2[w][k];	
	  
	
	int liczba_zgodnych=0, zgodna;
	
	for(int m=0; m<4; m++)
	 for(int n=0; n<4; n++)
	  if(karty1[w1][m]==karty2[w2][n]) { liczba_zgodnych++;  zgodna=karty1[w1][m]; }
	
	
	cout << "Case #" << c << ": ";
	  
	if(liczba_zgodnych==0) cout << "Volunteer cheated!" << endl;
	else if(liczba_zgodnych>1) cout << "Bad magician!" << endl;
	else cout << zgodna << endl;
	
	
	
    }
		
		
		
		
	
	
	
	
	return 0;
}
