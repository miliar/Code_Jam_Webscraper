#include <iostream>
#include <fstream>
#include <string>
#include <bitset>

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
         cout << "Case #" << k+1 << ":" << endl;
         
         int N;
         datei >> N;
         
         int J;
         datei >> J;
         
         
         for(int X = 0; X < J; X++)
         {
            cout << "1";
            int X2 = X;
            for(int i = 0; i < N/2-1; i++)
            {
               cout << X2%2 << X2%2;
               X2 /= 2;
            }
            cout << "1 3 4 5 6 7 8 9 10 11";
            if(X < J-1)
               cout << endl;
         }
         
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
