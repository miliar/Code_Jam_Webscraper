#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int deceit( vector<float> &naomi, vector<float> &ken, int blocks )
{
   int losses = 0;

   while (true) {
      bool failed = false;
      for (int i = 0; i < blocks - losses; ++i) {
         if (naomi[i + losses] < ken[i]) {
            ++losses;
            failed = true;
            break;
         }
      }
      if (losses == blocks)
         return 0;

      if (failed)
         continue;
      else
         break;
   }

   return blocks - losses;
}

int war( vector<float> &naomi, vector<float> &ken, int blocks )
{
   int n = blocks - 1, k = blocks - 1;
   int score = 0;
   int points = 0;

   while (n >= 0 && k >= 0)
   {
      if (naomi[n] > ken[k]) {
         n--;
         if (score == 0)
            points++;
         else
            score++;
      }
      else
      {
         k--;
         score--;
      }
   }
   
   return points; 
}

int main()
{
   int games;
   cin >> games;
   int num = 1;
   while (num <= games) {
      int blocks;
      vector<float> naomi;
      vector<float> ken;
      cin >> blocks;
      for (int i = 0; i < blocks; ++i) {
         float b;
         cin >> b;
         naomi.push_back(b);
      }
      for (int j = 0; j < blocks; ++j) {
         float b;
         cin >> b;
         ken.push_back(b);
      }

      sort(naomi.begin(), naomi.end());
      sort(ken.begin(), ken.end());

      cout << "Case #" << num << ": ";
      cout << deceit(naomi, ken, blocks) << " " << war(naomi, ken, blocks) << endl;

      num++;
   }
   return 0;
}
