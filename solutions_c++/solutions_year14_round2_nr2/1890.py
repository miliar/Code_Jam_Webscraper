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

bool visite[1000];

int main()
{
  ifstream cin("in.txt");
  ofstream cout ("out.txt");

   int N, T;

   cin >> T;

   string s1, s2;

   for(int i = 1; i <= T ; i++)
   {
       int A, B, K;
       cin >> A >> B >> K;
       int compteur = 0;
       for(int iA = 0; iA < A; iA++)
       {
           for(int jB = 0; jB < B; jB++)
           {
               int c = iA&jB;
               if(c < K)
               {
                   visite[c] = true;
                   compteur++;
               }
           }
       }

       for(int j = 0; j < K; j++)
            visite[j] = false;

       cout << "Case #" << i << ": " << compteur << endl;
   }
    return 0;
}
