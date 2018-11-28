#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(void)
{
  int t, size;

  cin >> t;

  for(int i = 1; i <= t; i++)
  {
    cin >> size;
    vector<double> weightsK(size, 0), weightsN(size, 0);
    for(int j = 0; j < size; j++) cin >> weightsN[j];
    for(int j = 0; j < size; j++) cin >> weightsK[j];

    sort(weightsK.begin(), weightsK.end());
    sort(weightsN.begin(), weightsN.end());

    int points1 = 0, points2 = 0;
    
    /* For debugging
    for(int j = 0; j < size; j++) cerr << weightsK[j] << " ";
    cerr << endl;
    for(int j = 0; j < size; j++) cerr << weightsN[j] << " ";
    cerr << endl;
    */

    int Nmin = 0, Nmax = size - 1;
    
    for(int j = size - 1; j >= 0; j--)
    {
      if (weightsN[Nmax] < weightsK[j])
      {
        Nmin++;
      }
      else
      {
        points1++;
        Nmax--;
      }
    }    
    
    int Kmin = 0, Kmax = size - 1;
    for(int j = size - 1; j >= 0; j--)
    {
      if (weightsK[Kmax] < weightsN[j])
      {
        points2++;
        Kmin++;
      }
      else
      {
        Kmax--;
      }
    }  
    cout << "Case #" << i << ": " << points1 << " " << points2 << endl;
  }

  return 0;
}
