#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
        ifstream fin("Bbig.in");
        ofstream fout("Bbig.out");
        int t;
        fin >> t;
        for (int T = 1; T <= t; ++T)
        {
                int d;
                fin >> d;
                vector<int> p(d);
                for (int j = 0; j < d; ++j)
                        fin >> p[j];
                
                int best = 100000000;
                for (int j = 1; j <= 1000; ++j)
                {
                  int yo = j;
                  for (int i = 0; i < d; ++i)
                  {
                        int lol = p[i];
                        while (lol > j)
                        {
                                lol -= j;
                                ++yo;
                        }
                  }
                  best = min(best,yo);
                }
                cout << "Case #" << T << ": " << best << endl;        
                cout << "********************************" << endl;
                //getchar();
                fout << "Case #" << T << ": " << best << endl;
        }
}
