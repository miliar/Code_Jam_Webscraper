#include <string>
#include <fstream>
#include <iostream>
using namespace std;

int main () {
  ifstream myfile;
  ofstream output ("output.txt"); 
  int t=0; 
  myfile.open ("A-small-attempt2.in");
  if (myfile.is_open())
  {      
                
    myfile >> t;
    
    for (int k = 0; k < t; k++)
    {
         
    int answerA, answerB, num = 0,card;
    int cardA [4][4], cardB [4][4];
      myfile >> answerA;
      //get card array
      for (int i = 0; i < 4; i++)
          for (int j = 0; j < 4; j++)
              myfile>>cardA[j][i]; 
      
      myfile >> answerB;
      //get card array
      for (int i = 0; i < 4; i++)
          for (int j = 0; j < 4; j++)
              myfile>>cardB[j][i]; 
              
      // compare rows of both arrays
      // if only one number exists that is the same, output number
      for (int i = 0; i < 4; i++)
          for (int j = 0; j < 4; j++)
              if (cardA[i][answerA - 1] == cardB[j][answerB-1])
              {
                 num++; 
                 card = cardA[i][answerA-1];
                 }
      
      output<<"Case #"<<(k+1)<<": ";
      if (num == 0)
         output<<"Volunteer cheated!";
      else if (num == 1)
           output<<card;
      else
          output<<"Bad magician!"; 
          
      output<<"\n"; 
      
      num = 0; 
          
    }
  }
  
  
  return 0;
}
