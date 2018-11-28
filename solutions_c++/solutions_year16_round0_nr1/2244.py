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
         
         
         
         int N;
         datei >> N;
         
         if(N == 0)
            cout << "INSOMNIA";
         else
         {
            bool a[10];
            for(int i = 0; i < 10; i++)
            {
               a[i] = false;
            }
            
            int i = 1;
            for(i = 1; i < 100000; i++)
            {
               int M = i*N;
               while(M != 0)
               {
                  a[M % 10] = true;
                  M = M/10;
               }
               bool done = true;
               for(int j = 0; j < 10; j++)
               {
                  if(!a[j])
                  {
                     done = false;
                     break;
                  }
               }
               if(done)
               {
                  break;
               }
            }
            if(i >= 100000)
               cout << "INSOMNIA";
            else
            {
               cout << i*N;
            }
            
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
