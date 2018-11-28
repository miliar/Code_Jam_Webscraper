#include <iostream>
#include <fstream>

using namespace std;

int main()
{
   ifstream in("input.txt");
   ofstream out("output.txt");
   
   int testCaseCount;
   in >> testCaseCount;
   
   for(int caseNum = 0; caseNum < testCaseCount; caseNum++)
   {
       int maxStanding;
       in >> maxStanding;
       
       int extraNeeded = 0;
       int totalStanding = 0;
       for(int standingRequirement = 0; standingRequirement <= maxStanding; standingRequirement++)
       {
           if(totalStanding < standingRequirement)
           {
               extraNeeded += standingRequirement - totalStanding;
               totalStanding += standingRequirement - totalStanding;
           }
           
           char inChar;
           in >> inChar;
           int standing = (int)inChar - 48;
           
           totalStanding += standing;
           
        
       }
       out << "Case #" << caseNum + 1 << ": " << extraNeeded << endl;
   }
   
   
   return 0;
}

