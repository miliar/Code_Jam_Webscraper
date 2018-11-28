#include<iostream>
using namespace std;

int main()
{
  int T, N;
  float Wn[1000], Wk[1000], temp;
  int war, deceitful_war;
  int n, k;

  cin >> T;
  for(int t = 1; t <= T; t++)
  {
    war = 0; deceitful_war = 0; n = 0; k = 0;

    cin >> N;
    for(int i = 0; i < N; i++)
      cin >> Wn[i];
    for(int i = 0; i < N; i++)
      cin >> Wk[i];
    for(int i = N-1; i > 0; i--)
      for(int j = 0; j < i; j++)
      {
        if(Wn[j] > Wn[j+1])
        {
          temp = Wn[j];
          Wn[j] = Wn[j+1];
          Wn[j+1] = temp;
        }
        if(Wk[j] > Wk[j+1])
        {
          temp = Wk[j];
          Wk[j] = Wk[j+1];
          Wk[j+1] = temp;
        }
      }

    for(n = 0, k = 0; k < N; k++)
      if(Wn[n] < Wk[k])
        ++n;
    war = N-n;

    for(n = 0, k = 0; n < N; n++)
      if(Wn[n] > Wk[k])
        ++k;
    deceitful_war = k;

    cout << "Case #" << t << ": " << deceitful_war << " " << war << endl;
  }
  return 0;
}
