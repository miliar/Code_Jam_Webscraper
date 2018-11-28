#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
using namespace std;

const char CDATA[] = "C-large-1.in";
const char CRES[]  = "output.out";

bool IsPal(long long);

int main()
{
    ifstream fin(CDATA);
    ofstream fout(CRES);

    long long lim = pow(10,14);
    vector<long long> fairs;
    for (long long i = 1; i <= 10000000; ++i)
      if (IsPal(i) && IsPal(i*i)) fairs.push_back(i*i);

  //  cout << fairs.size() << endl;
  //  for (int i = 0; i < fairs.size(); ++i)
 //     cout << "i:  " << fairs[i] << "  " << sqrt(fairs[i]) << endl;
    int t;
    fin >> t;
    for (int i = 0; i < t; ++i)
    {
       int kiek = 0;
       long long a,b;
       fin >> a >> b;
       for (int j = 0; j < fairs.size(); ++j)
         if (fairs[j] >= a && fairs[j] <= b) kiek++;
       fout << "Case #" << i+1 << ": " << kiek << endl;
    }

    fin.close();
    fout.close();

    return 0;
}

bool IsPal(long long a)
{
   vector<char> sk;
   while (a != 0)
   {
      sk.push_back(a % 10);
      a /= 10;
   }

   for (int i = 0; i < int(sk.size())/2; ++i)
      if (sk[i] != sk[sk.size()-i-1]) return false;
   return true;
}
