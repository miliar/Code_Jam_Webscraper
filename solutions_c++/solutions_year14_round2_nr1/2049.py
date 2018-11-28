#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <queue>
#include <vector>
#include <fstream>
#include <stack>
#include <utility>

#define NB_MACHINES 30
#define NB_OBJET 1000

using namespace std;


int main()
{
  ifstream cin("in.txt");
  ofstream cout ("out.txt");

   int N, T;

   cin >> T;

   string s1, s2;

   for(int i = 1; i <= T; i++)
   {

        cin >> N;

       cin.ignore();
       cin >> s1 >> s2;
        char last = '*';
        int jS2 = 0;
        int compteur = 0;
        bool perdu = false;

       for(int jS1 = 0; jS1 < s1.size(); jS1++)
       {
           while(s1[jS1] != s2[jS2] && !perdu)
           {
               if(jS1 == 0 || jS1 > s1.size()-1)
               {
                    perdu = true;
               }
               else
               {
                   if(last == s2[jS2])
                   {
                       jS2++;
                       compteur++;
                   }
                   else if(last == s1[jS1])
                   {
                       jS1++;
                       compteur++;
                   }
                   else
                        perdu = true;

               }
           }
            last = s2[jS2];
            jS2++;
       }
       for(jS2; jS2 < s2.size(); jS2++)
       {

           compteur++;
           if(last != s2[jS2])
                perdu = true;
       }

       if(perdu)
       {
           cout << "Case #" << i << ": Fegla Won" << endl;
       }
       else
       {
           cout << "Case #" << i << ": " << compteur << endl;
       }
   }
    return 0;
}
