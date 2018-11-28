#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int optimDeceiv(vector<double>& nao, vector<double>& ken)
{
  int naoMin = 0;
  int naoMax = nao.size() - 1;
  int kenMax = ken.size() - 1;
  int points = 0;
  for (unsigned int i = 0; i < ken.size(); ++i) {
    if ( ken[kenMax] < nao[naoMax] ) {
      kenMax--;
      naoMax--;
      points++;
    }
    else {
      kenMax--;
      naoMin++;
    }
  }
  return points;
}

int optimWar(vector<double>& nao, vector<double>& ken)
{
  int naoMax = nao.size() - 1;
  int kenMin = 0;
  int kenMax = ken.size() - 1;
  int points = 0;
  for (unsigned int i = 0; i < ken.size(); ++i) {
    if ( ken[kenMax] < nao[naoMax]) {
      kenMin++;
      points++;
    }
    else 
      kenMax--;
    naoMax--;
  }

  return points;
}

int main()
{
  int T, N = 1;
  cin >> T;
  while ( N <= T ) {
    int size;
    cin >> size;
    vector<double> nao(size, 0);
    vector<double> ken(size, 0);
    for (int i = 0; i < size; ++i)
      cin >> nao[i];
    for (int i = 0; i < size; ++i)
      cin >> ken[i];
    sort(nao.begin(), nao.end());
    sort(ken.begin(), ken.end());

    cout << "Case #" << N << ": " << optimDeceiv(nao, ken) << " " << optimWar(nao, ken) << endl;
    ++N;
  }
}
