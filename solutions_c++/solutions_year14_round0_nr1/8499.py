#include <iostream>


using namespace std;


int main(int argc, char* argv[])
{

   int x;
   cin >> x;

   int sq1[4][4];
   int sq2[4][4];


   for(int test=0; test < x; ++test)
   {
      cout << "Case #" << test+1 << ": "; 

      int scenario = -1;
      int card = -1;
      int first;
      cin >> first;
      --first;
      for(int n=0; n <4; ++n)
      {
         for(int i=0; i < 4; ++i)
         {
            cin >> sq1[n][i]; //Row major
         }
      }



      int second;
      cin >> second;
      --second;
      for(int n=0; n <4; ++n)
      {
         for(int i=0; i < 4; ++i)
         {
            cin >> sq2[n][i]; //Row major
         }
      }

      
      for(int n=0; n < 4; ++n)
      {

         for(int i=0; i < 4; ++i)
         {
            if(sq1[first][n] == sq2[second][i])
            {
               if(card == -1)
                  card = sq1[first][n];
               else
                  scenario = 0;
            }
         }
      }

      if(card == -1)
         scenario = 1;
      else if(scenario == -1)
         cout << card;



      switch(scenario)
      {

         case 0:
            cout << "Bad magician!";
            break;
         
         case 1:
            cout << "Volunteer cheated!";
            break;

         case 2:
            scenario = 2;
            break;
      }

      cout << endl;
   }

	return 0;

};
