#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main(int argc, char *argv[])
{
   //Eingabe des Dateinamens über Konsole oder Übergabe als Eingabeparameter
   char* filename;
   if(argc > 1)
   {
      filename = argv[1];
   }
   else
   {
      char buffer[256];
      cout << "Input file name (up to 255 Characters): " << endl;
      cin >> buffer;
      filename = buffer;
   }
   
   int T = 0;
   
   try
   {    
      ifstream datei(filename);
      if(!datei.is_open())
         throw 1;
      
      if(!datei.good())
         throw 2;
      datei >> T;
      if(T <= 0)
         throw 3;
      
      
      for(int k = 0; k < T; k++)
      {
         cout << "Case #" << k+1 << ": ";
          
         int D;
         datei >> D;
          
         int P[D];
         int max = 0;
         for(int i = 0; i < D; i++)
         {
            datei >> P[i];
            if(P[i] > max)
               max = P[i];
         }
         
         //Algorithm begins here:
         int minMinutes = max;
         for(int l = 1; l <= max; l++)
         {
            int lMinutes = l;
            for(int i = 0; i < D; i++)
               lMinutes += ((int) ceil((P[i]+0.0)/l))-1;
            if(lMinutes < minMinutes)
               minMinutes = lMinutes;
         }
         
         cout << minMinutes;
         
         cout << endl;
      }
   }
   catch(int e)
   {
      cout << "Fehler (Nr. " << e << ") beim Einlesen der Datei.";
      int a;
      cin >> a;
      return 1;
   }
    
    //int a;
    //cin >> a;
    return 0;    
}
