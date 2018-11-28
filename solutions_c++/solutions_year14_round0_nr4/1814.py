#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <list>
#include <algorithm>
using namespace std;

int main () {

  ifstream myfile ("input.txt");
  if (myfile.is_open())
  {
   int tests;
   myfile >> tests;
   for(int i = 0; i < tests; i++)
   {
       //Build lists
        int lsize, WScore, DWScore;
        double buffer, Nchose, Kchose;
        list<double> naomi;
        list<double> ken;
        WScore = 0;
        DWScore = 0;

        myfile >> lsize;
       
       //Naomi's numbers
        for(int i = 0; i < lsize; i++)
        {
            myfile >> buffer;
            naomi.push_back(buffer);
        }
       //Ken's numbers
        for(int i = 0; i < lsize; i++)
        {
            myfile >> buffer;
            ken.push_back(buffer);
        }
       //Sort lists

       ken.sort();
       naomi.sort();
       
       //Copy lists for second game
        list<double> naomiD(naomi);
        list<double> kenD(ken);   
       

        
        //Normal War
        for(int i = 0; i < lsize; i++)
        {
            Nchose = naomi.back();
            naomi.pop_back();
            if(ken.back() < Nchose)
            {
                ken.pop_front();
                WScore++;
            }
            else
            {
                list<double>::iterator low=std::lower_bound (ken.begin(), ken.end(), Nchose);
                ken.remove(*low);
            }
        }
        
        //Deceitful War
        for(int i = 0; i < lsize; i++)
        {
            Kchose = kenD.front();
            kenD.pop_front();
            if(naomiD.back() < Kchose)
            {
                naomiD.pop_front();
            }
            else
            {
                list<double>::iterator low=std::lower_bound (naomiD.begin(), naomiD.end(), Kchose);
                naomiD.remove(*low);
                DWScore++;
            }
            
        }
        cout << "Case #" << i+1 << ": " << DWScore << " " << WScore << endl;
       
    
       
   }
   
    myfile.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}