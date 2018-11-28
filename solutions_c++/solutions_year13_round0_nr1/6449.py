#include<iostream>
#include<sstream>
#include<string>
#include <fstream>
using namespace std;
int check_tab (char game_tab [][4]);
char game_tab [4][4];
int main() {
//Variables
  int i,j,num_cases,visited,index,cntr;
  int result;
  string line; 
  stringstream st;
  ifstream b_file ( "A-large.in" );
  ofstream b_out ("sol_large.out");

  getline(b_file,line);
  st<<line;
  st>>num_cases;
  cntr=0;
  while(cntr<num_cases) {
  
//Process Each Line
	   i=0;
	   for(i=0;i<4;i++){
	   	getline(b_file,line);
	   	for(j=0;j<4;j++){
	 		game_tab[i][j] = line[j];  		
	   	}
	   }
	   getline(b_file,line);
//	Check the conditions for winning
    result = check_tab(game_tab); 
		
	if(result==1){
		b_out<<"Case #"<<cntr+1<<": X won";
	    b_out<<"\n";
	} else if(result==2){
		
		b_out<<"Case #"<<cntr+1<<": O won";
	    b_out<<"\n";
	 
	} else if (result==3){
		b_out<<"Case #"<<cntr+1<<": Draw";
	    b_out<<"\n";
	} else {		   
	  b_out<<"Case #"<<cntr+1<<": Game has not completed";	  
	  b_out<<"\n";
	}
  cntr++;  
  }
 return 0; 
}

int check_tab (char game_tab [4][4]) {
//1 = X won
//2 - O won
//3 - Draw
//4 - not completed

 int xcnt, ocnt;
 int i,j;
 int total_count;
 total_count = 0;
 //row checks
 xcnt=0;
 ocnt=0;
 for(i=0;i<4;i++){
 	xcnt =0;
 	ocnt=0;
 	for(j=0;j<4;j++){
 		if((game_tab[i][j]=='X') || (game_tab[i][j]=='T')){
 			xcnt++;
 		}
 		if((game_tab[i][j]=='O') || (game_tab[i][j]=='T')){
 			ocnt++;
 		}
		
		if(game_tab[i][j]!='.'){
			total_count++;
		} 
		  		
 	}
 	if(xcnt==4){
 		return 1;
 	}
 	if(ocnt==4){
 		return 2;
 	}
 
 }
  	
 xcnt=0;
 ocnt=0;
 i=0;
 j=0;
 //col scan
  for(i=0;i<4;i++){
  	xcnt =0;
 	ocnt=0;
 	for(j=0;j<4;j++){
 		if((game_tab[j][i]=='X') || (game_tab[j][i]=='T')){
 			xcnt++;
 		}
 		if((game_tab[j][i]=='O') || (game_tab[j][i]=='T')){
 			ocnt++;
 		}
 		
 	}
 	if(xcnt==4){
 		return 1;
 	}
 	if(ocnt==4){
 		return 2;
 	}
 }	
 
 //diagonal scan
 i=0;
 j=0;
 xcnt =0;
 ocnt=0;
 while(i<4){
 	if((game_tab[i][j]=='X') || (game_tab[i][j]=='T')){
 			xcnt++;
 		}
 	if((game_tab[i][j]=='O') || (game_tab[i][j]=='T')){
 			ocnt++;
 	}
 	j++;
 	i++;
 }
 if(xcnt==4){
 		return 1;
 }
 if(ocnt==4){
 		return 2;
 }
 
 i=0;
 j=3;
 xcnt =0;
 ocnt=0;
 while(i<4){
 	if((game_tab[i][j]=='X') || (game_tab[i][j]=='T')){
 			xcnt++;
 		}
 	if((game_tab[i][j]=='O') || (game_tab[i][j]=='T')){
 			ocnt++;
 	}
 	j--;
 	i++;
 }
 if(xcnt==4){
 		return 1;
 }
 if(ocnt==4){
 		return 2;
 }
 
 if(total_count<16){
 	return 4;
 } else {
 	return 3;
 }
 
}

