#include <iostream>
#include <fstream>

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
           
         int Smax;
         datei >> Smax;
         
         int S[Smax+1];
         int sum = 0;
         int additionalNeeded = 0;
         for(int i = 0; i <= Smax; i++)
         {
            char temp;
            datei >> temp;
            S[i] = (int) temp - ((int) '0');
            if(sum + additionalNeeded < i)
               additionalNeeded += i-(sum+additionalNeeded);
            sum += S[i];
         }
         
         cout << additionalNeeded;
         
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
