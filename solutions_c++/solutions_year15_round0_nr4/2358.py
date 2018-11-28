#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool DetermineWinner(int Omino_Degree, int Board_Row, int Board_Column);

int main()
{
    ifstream fin("d.in");
    ofstream fout("d.out");
    
    int cases;
    int current_case = 1;
    fin >> cases;
    while(current_case <= cases)
    {
        int Omino_Degree;
        int Board_Row, Board_Column;
        fin >> Omino_Degree >> Board_Row >> Board_Column;
        
        bool winner;  //true = gabriel, false = richard
        winner = DetermineWinner(Omino_Degree, Board_Row, Board_Column);
       
        fout << "Case #" << current_case << ": ";
        if(winner)
          fout << "GABRIEL" << endl;
        else
          fout << "RICHARD" << endl;
        current_case++;
    }
    fin.close();
    fin.close();
    return 0;
}

bool DetermineWinner(int Omino_Degree, int Board_Row, int Board_Column)
{
    int Area = Board_Row * Board_Column;
    if(Omino_Degree == 1)
      return true;
      
    if(Omino_Degree == 2 && (Area % 2 == 0))
      return true;
      
    if(Omino_Degree == 3)
    {
      if(Area == 3 || (Area % 3 != 0) || Board_Row <= 1 || Board_Column <= 1)
        return false;
      else
        return true;
    }
    
    if(Omino_Degree == 4)
    {
      //now i just have to handle 4 omino pieces
      if(Area <= 8 )
        return false;
      if(Area % 4 != 0)
        return false;
      else
        return true;
    }
    return false;
}
