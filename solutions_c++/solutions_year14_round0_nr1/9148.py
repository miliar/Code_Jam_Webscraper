#include <fstream>
#include <iostream>
#include <stdio.h> 
#include <stdlib.h>
using namespace std;

int comparing(int firstRow[], int secondRow[], int game){
	//Comparing both arrays	 
	   int cont = 0;  
	   int volunteerNum;
	   for (int k=0;k<4;k++){
	   	for (int m=0; m<4; m++){
		   	if (firstRow[k]==secondRow[m]){
		   		cont ++;
			    volunteerNum = firstRow[k];	
		   	}	
	   	}	   	
	   }
	   
	   if (cont==1){
	   	 cout << "Case #"<< game+1 << ": " << volunteerNum << endl;
	   } 
	   if (cont > 1){
	   	 cout << "Case #"<< game+1 << ": " << "Bad magician!" << endl;
	   }
	   if (cont < 1){
	   	 cout << "Case #"<< game+1 << ": " << "Volunteer cheated!" << endl;
	   }
}

 
int main ()
{
   ifstream infile; 
   infile.open("input.txt"); 
 
   // Reading from the input.txt file 
   int numGames, volunteer1Row, volunteer2Row;
   infile >> numGames; 
   //cout << numGames << endl;
   
   int a, b, c, d;
   int firstRow[4];
   int secondRow[4];
   
   for(int i=0; i<numGames;i++){
   	   //cout << "Game N.:" << i+1 << endl;
	   
	   //First volunteer row selection
	   infile >> volunteer1Row; 
	   //cout << "Volunteer choose row 1st time:" << volunteer1Row << endl;
	   for (int j=0;j<4;j++){
	   	   infile >> a >> b >> c >> d;
	       //cout << a << " " << b << " " << c << " " << d<< endl;
	       if (j+1 == volunteer1Row){
		    firstRow[0] = a;
		    firstRow[1] = b;
		    firstRow[2] = c;
		    firstRow[3] = d;		   
		   	//cout << firstRow[0] << " " << firstRow[1] << " " << firstRow[2] << " " << firstRow[3]<< endl;
		   }	       
	   }
	   
	   //Second volunteer row selection
	   infile >> volunteer2Row; 	   
	   //cout << "Volunteer choose row 2nd time:" << volunteer2Row << endl;
	   for (int h=0;h<4;h++){
	   	   infile >> a >> b >> c >> d;
	       //cout << a << " " << b << " " << c << " " << d<< endl;
	       if (h+1 == volunteer2Row){
	        secondRow[0] = a;
		    secondRow[1] = b;
		    secondRow[2] = c;
		    secondRow[3] = d;		   
		   	//cout << secondRow[0] << " " << secondRow[1] << " " << secondRow[2] << " " << secondRow[3]<< endl;
		   }
	   }
	   
	   comparing(firstRow, secondRow, i);	   
   }  
   
   // closing the opened file.
   infile.close();  
   
   system("PAUSE");
   
   return 0;
   cin.get();
}
