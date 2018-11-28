#include <cstdlib>
#include <iostream>
#include <Math.h>
#include "set"

using namespace std;

int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T;
    int N;    
    cin >> T;
    string SS[100];

	int y;
	int try1;
	int _move;
	int char_1;
	int char_2;
	bool nomove;
	bool noanswer;
	char cchar_1;
	int char_n;
	int char_n2;
	int charx[100];
	int chary[100];
    for (int T_i=0; T_i<T;T_i++){
        cin >> N;
        y = 10000;
        for (int I=0;I <N;I++){
            cin >> SS[I];        
        }
        for (int try1=0; try1<1; try1++){
            _move= 0;
            noanswer = false;
            char_1=0;
            
           while ( SS[try1].length() > char_1) {
            
           if (SS[try1].length() > char_1) {
              cchar_1 = SS[try1][char_1]; 
              while ((SS[try1].length() > char_1) && (cchar_1 == SS[try1][char_1])){
                 char_n++;
                 char_1++;   
              }
           }      
            
            int max_c = 0;
            int min_c = 1000;
            
            for (int i=0;i <N;i++){
               char_2 = 0;
               char_n2 = 0;
               if (SS[i].length() > char_2) {
                  while ((SS[i].length() > char_2) && ((cchar_1 == SS[i][char_2]) || (SS[i][char_2] == ' ' )   )){
                     if (SS[i][char_2] == cchar_1) char_n2++;
                     SS[i][char_2] = ' ';
                     char_2++;     
                  }
               }
               charx[i] = char_n2;                
            }            

//            for (int i=0;i<N;i++) chary[i]=0;
            
            for (int i=0;i<N;i++) {
                if (charx[i] ==0) noanswer = true;
//                chary[charx[i]] ++;
                max_c = max_c + charx[i];
                }

//            for (int i=0;i<N;i++) {
//                if (chary[i] > chary[max_c]) max_c = i;}
            max_c = round (max_c * 1.0 / N);
            
//            cout << cchar_1 << " " << noanswer << " " << max_c << endl;
            for (int i=0;i<N;i++) 
                _move = _move +abs(charx[i]-max_c);
            
            }
            
            
        }

            for (int i=0;i <N;i++){
               char_2 = 0;
               if (SS[i].length() > char_2) {
                  while (SS[i].length() > char_2  ){
                     if (SS[i][char_2] != ' ') noanswer=true;
                     char_2++;     
                  }
               }
            }            


        if (noanswer) 
        cout << "Case #" << T_i+1 << ": Fegla Won" << endl;
        else
        cout << "Case #" << T_i+1 << ": " << _move << endl;
        
    }
    return EXIT_SUCCESS;
}
