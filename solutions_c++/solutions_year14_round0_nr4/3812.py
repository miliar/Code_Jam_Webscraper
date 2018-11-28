#include <iostream>     // std::cout
#include <algorithm>    // std::sort
#include <vector>       // std::vector

using namespace std;

double choose(vector<double> &Ken, const double &Naomi);

static bool isGreater(double u, double v)
{
   return u > v;
}

int main ()
{
  int T, i, N, k, dWar, War;
  double d;

  double z; 

  cin >> T;
  for (i = 1; i <= T; ++i)
  {
    cin >> N;

    vector<double> Naomi;
    vector<double> Ken;
    vector<double> dKen;
    for (k = 0; k < N; ++k)
    {
      cin >> d;
      Naomi.push_back(d);
    }    

    for (k = 0; k < N; ++k)
    {
      cin >> d;
      Ken.push_back(d);
      dKen.push_back(d);
    }

    sort(Naomi.begin(), Naomi.end(), isGreater);
    sort(dKen.begin(), dKen.end());

    War = 0;
    for(vector<double>::size_type index = 0; index < Naomi.size(); ++index)
    {
      z = choose(dKen, Naomi[index]);
      if(z < Naomi[index])
      {         
        //cout << z << endl;
        //cout << Naomi[index] << endl;
        War++;
        //dKen.erase(dKen.begin());
      }
      //dKen.erase(&dKen[index]);
      //dKen.erase(dKen.begin());
    }

    //sort(Naomi.begin(), Naomi.end(), isGreater);
    sort(Ken.begin(), Ken.end(), isGreater);
    dWar = 0;
    for(vector<double>::size_type index = 0; index < Naomi.size(); ++index)
    {
      if(Ken[index] > Naomi[index])
      {
        Ken.erase(Ken.begin());
        Naomi.erase(Naomi.begin()+Naomi.size()-1);
        index--;
      }
      else
      {
        Ken.erase(Ken.begin());
        Naomi.erase(Naomi.begin());
        index--;
        dWar++;
      }
    }
        

    cout << "Case #" << i << ": " << dWar << " " << War << endl;      
  }
  
  return 0;
}

double choose(vector<double> &Ken, const double &Naomi)
{
  vector<double>::iterator it = Ken.begin();
  double d = *it;

  for (; it != Ken.end(); it++)
  {
    d = *it;
    if (d > Naomi)
    {      
      Ken.erase(it);
      return d;
    }
  }

  Ken.erase(Ken.begin());
  return d;
}