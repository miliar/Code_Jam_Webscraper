// ProgrammingCompetition.cpp : Defines the entry point for the console application.
//

#include "windows.h"

#include <iostream>     // std::cout
#include <fstream>      // std::ifstream
#include <string>
#include <sstream>

using namespace std;

int main () {
  ifstream ifs("C:\\input.in");
  ofstream output;
  output.open("C:\\output.txt",std::ofstream::out);
  //ifs.open("input.txt");
  stringstream ss;
  string l1, l2, l3, line;
  getline(ifs, l1);
  stringstream ss1(l1);
  int no_of_cases, ans1, ans2;
  ss1 >> no_of_cases;
  int array1[4][4];
  int array2[4][4];
  int x;
  for(int i=0;i<no_of_cases;i++)
  {
	 getline(ifs,l2);
	 stringstream ss2(l2);
	 ss2>>ans1;
	 for (int j =0;j<4;j++){
		 
		  getline(ifs,line);
		  stringstream ss(line);
		  
		 for(int k=0;k<4;k++){
			 ss>>x;
			 array1[j][k] = x;
		 }

		 ss<<"";
		 ss.clear();
	 }

	 getline(ifs,l3);
	 stringstream ss3(l3);
	 ss3>>ans2;
	 for (int j =0;j<4;j++){
		 
		  getline(ifs,line);
		  stringstream ss(line);
		  
		 for(int k=0;k<4;k++){
			 ss>>x;
			 array2[j][k] = x;
		 }

		 ss<<"";
		 ss.clear();
	 }
	 int count = 0;
	 int card_num = 100;
	 for(int m=0; m<4;m++){

		 for(int n=0;n<4;n++){
			 
			 if(array1[ans1-1][m] == array2[ans2-1][n])
			 {
				 count++;
				 card_num = array1[ans1-1][m];
			 }
		 }
	 }
	
	 if(count==0){
		 printf("No match\n");
		 output<<"Case #"<<i+1<<": Volunteer cheated!\n";

	 }
	 else if(count==1){
		 printf("card is %d\n",card_num);
		 output<<"Case #"<<i+1<<": "<<card_num<<"\n";
	 }
	 else{
		 printf("bad magician\n");
	 	 output<<"Case #"<<i+1<<": Bad magician!\n";
	 }

  }
  ifs.close();
  output.close();
  return 0;
}
