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
         
         //begin:
         //======
         
         int R;
         datei >> R;
         int C;
         datei >> C;
         
         char A[R][C];
         bool critical[R][C];
         for(int i = 0; i < R; i++)
            for(int j = 0; j < C; j++)
               critical[i][j] = false;
         
         for(int i = 0; i < R; i++)
         {
            bool onlyPoints = true;
            int toRight = -1;
            for(int j = 0; j < C; j++)
            {
               datei >> A[i][j];
               if(A[i][j] != '.')
               {
                  if(onlyPoints)
                  {
                     onlyPoints = false;
                     if(A[i][j] == '<')
                        critical[i][j] = true;
                  }
                  if(toRight != -1)
                  {
                     critical[i][toRight] = false;
                  }
                  if(A[i][j] == '>')
                  {
                     toRight = j;
                     critical[i][j] = true;
                  }
               }
            }
         }
         
         for(int j = 0; j < C; j++)
         {
            bool onlyPoints = true;
            int toDown = -1;
            for(int i = 0; i < R; i++)
            {
               if(A[i][j] != '.')
               {
                  if(onlyPoints)
                  {
                     onlyPoints = false;
                     if(A[i][j] == '^')
                        critical[i][j] = true;
                  }
                  if(toDown != -1)
                  {
                     critical[toDown][j] = false;
                  }
                  if(A[i][j] == 'v')
                  {
                     toDown = i;
                     critical[i][j] = true;
                  }
               }
            }
         }
         
         int count = 0;
         for(int i = 0; i < R; i++)
         {
            for(int j = 0; j < C; j++)
            {
               bool bad = true;
               if(critical[i][j])
               {
                  count++;
                  if(A[i][j] != 'v')
                  {
                     for(int l = i+1; l < R; l++)
                     {
                        if(A[l][j] != '.')
                        {
                           bad = false;
                           break;
                        }
                     }
                  }
                  if(bad && A[i][j] != '^')
                  {
                     for(int l = i-1; l >= 0; l--)
                     {
                        if(A[l][j] != '.')
                        {
                           bad = false;
                           break;
                        }
                     }
                  }
                  if(bad && A[i][j] != '<')
                  {
                     for(int l = j-1; l >= 0; l--)
                     {
                        if(A[i][l] != '.')
                        {
                           bad = false;
                           break;
                        }
                     }
                  }
                  if(bad && A[i][j] != '>')
                  {
                     for(int l = j+1; l < C; l++)
                     {
                        if(A[l][j] != '.')
                        {
                           bad = false;
                           break;
                        }
                     }
                  }
                  if(bad)
                  {
                     goto badend;
                  }
               }
            }
         }
         cout << count;
         goto goodend;
         
         badend:
         cout << "IMPOSSIBLE";
            
         
         //end
         //===
         goodend:
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
