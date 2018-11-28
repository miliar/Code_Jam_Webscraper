#include <iostream>
#include <fstream>
#include <string>

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
      
      
      for(int k0 = 0; k0 < T; k0++)
      {
         cout << "Case #" << k0+1 << ": ";
         
         
         //start
         string S;
         datei >> S;
         
         int a[26];
         int x[10];
         for(int i = 0; i < 26; i++)
         {
         	a[i] = 0;
		 }
         for(int i = 0; i < S.length(); i++)
         {
         	a[(int) (S[i] - 'A') % 26]++;
		 }
		 
		 x[0] = a[(int) ('Z' - 'A') % 26];
		 x[2] = a[(int) ('W' - 'A') % 26];
		 x[4] = a[(int) ('U' - 'A') % 26];
		 x[6] = a[(int) ('X' - 'A') % 26];
		 x[7] = a[(int) ('S' - 'A') % 26] - x[6];
		 x[8] = a[(int) ('G' - 'A') % 26];
		 x[3] = a[(int) ('H' - 'A') % 26] - x[8];
		 x[5] = a[(int) ('V' - 'A') % 26] - x[7];
		 x[9] = a[(int) ('I' - 'A') % 26] - x[5] - x[6] - x[8];
		 x[1] = a[(int) ('O' - 'A') % 26] - x[0] - x[2] - x[4];
         
         for(int i = 0; i < 10; i++)
         {
         	for(int j = 0; j < x[i]; j++)
         	{
         		cout << i;
			}
		 }
         //end
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
