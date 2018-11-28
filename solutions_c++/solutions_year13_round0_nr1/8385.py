/*
 * main.cpp
 *
 *  Created on: 12/04/2013
 *      Author: kaka
 */

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <stdio.h>

//#define DEBUG

using namespace std;
char table[4][4];
short int count_X_lines = 0, count_O_lines = 0;
short int count_X_cols = 0, count_O_cols = 0, count_P = 0;
short int count_X_diagonal = 0, count_O_diagonal = 0;
long int table_count = 0, count_line = 0;
bool win_x = false, win_o = false;

int main(int argc, char *argv[])
{
	int k = 3;
    // Abre arquivo para leitura
    char buff[4];
    ifstream arquivo;

    arquivo.open("tic_tac_input.txt");

    while(arquivo >> buff) // Enquanto não for fim de arquivo
    {
       // if(buff[0] != '\n'){
            for(int x=0; x<4; x++){
               table[count_line][x] = buff[x];
            }
            count_line++;
       // }
         if(count_line == 4){
    	   for(int x=0; x<4; x++){
      	   	 for(int y=0; y<4; y++){
      	   		if((table[x][y] == 'X') || (table[x][y] == 'T')){
    	   			count_X_lines++;
    	   		}
    	   		if((table[y][x] == 'X') || (table[y][x] == 'T')){
    	   		    count_X_cols++;
    	   		}
    	   		if((table[x][y] == 'O') || (table[x][y] == 'T')){
    	   			count_O_lines++;
    	   		}
    	   		if((table[y][x] == 'O') || (table[y][x] == 'T')){
    	   			count_O_cols++;
    	   		}
    	   		if(table[x][y] == '.'){
    	   		 	count_P++;
    	   		}
    	   		if((table[y][y] == 'X') || (table[y][y] == 'T')){
    	   			count_X_diagonal++;
    	   		}
    	   		if((table[y][y] == 'O') || (table[y][y] == 'T')){
    	   			count_O_diagonal++;
    	   		}
    	   	 }
      	   	 if((count_X_lines == 4) || (count_X_cols == 4) || (count_X_diagonal == 4)){
      	   		win_x = true;
      	   	 }
      	     if((count_O_lines == 4) || (count_O_cols == 4) || (count_O_diagonal == 4)){
      	      	win_o = true;
      	     }

                  #ifdef DEBUG
      	          cout << "count_P " << count_P << '\n';
      	       	  cout << "count_X_lines " << count_X_lines << '\n';
      	       	  cout << "count_O_lines " << count_O_lines << '\n';
      	       	  cout << "count_X_cols " << count_X_cols << '\n';
      	       	  cout << "count_O_cols " << count_O_cols << '\n';
      	          cout << "count_X_diagonal " << count_X_diagonal << '\n';
      	       	  cout << "count_O_diagonal " << count_O_diagonal << '\n';
                  #endif


      	     count_O_cols = count_O_lines = count_O_diagonal = 0;
      	     count_X_cols = count_X_lines = count_X_diagonal = 0;
    	  }
    	  for(int x=0; x<4; x++){
    		  if((table[x][k] == 'X') || (table[x][k] == 'T')){
    		      count_X_diagonal++;
    		  }
    		  if((table[x][k] == 'O') || (table[x][k] == 'T')){
    		      count_O_diagonal++;
    		  }
    		  k--;
    	  }
    	  k = 3;
    	  if(count_X_diagonal == 4){
    		  win_x = true;
    	  }
    	  if(count_O_diagonal == 4){
              win_o = true;
    	  }
    	  table_count++;


          #ifdef DEBUG
    	  cout << "count_X_diagonal " << count_X_diagonal << '\n';
    	  cout << "count_O_diagonal " << count_O_diagonal << '\n';
          #endif


    	  if(win_x){
    		  cout << "Case #" << table_count <<": X won" << '\n';
    	  }
    	  else if(win_o){
    		  cout << "Case #" << table_count <<": O won" << '\n';
    	  }
    	  else if(count_P != 0){
    	      cout << "Case #" << table_count <<": Game has not completed" << '\n';
    	  }
    	  else{
    		  cout << "Case #" << table_count <<": Draw" << '\n';
    	  }
    	  count_P = 0;
    	  count_X_lines = 0;
    	  count_O_lines = 0;
    	  count_X_cols = 0;
    	  count_O_cols = 0;
    	  count_X_diagonal = 0;
    	  count_O_diagonal = 0;
    	  win_x = false;
    	  win_o = false;


          #ifdef DEBUG
          for(int x=0; x<4; x++)
          {
             for(int y=0; y<4; y++)
             {
                cout << table[x][y];
             }
             cout << '\n';
          }
          cout << '\n';
          #endif


          count_line = 0;
       }
    }

      /*   for(int x=0; x<5; x++){
        	 for(int y=0; y<5; y++){
        		 cout << table[x][y];
        	 }
         }
         cout << '\n';*/

     // Exibe no vídeo

      //escrevo aqui a solução do problema


    /*
    // Gravando uma linha no arquivo :
    ofstream fout("a:tic_tac_output.txt"); // Cria arquivo para gravação
    //em modo texto
    fout << "Case #" << case << ""; */

    system("PAUSE");
    return EXIT_SUCCESS;
}
