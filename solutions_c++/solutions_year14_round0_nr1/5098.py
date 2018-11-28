#include<iostream>
using namespace std;

int main()
{
  int T;
  int ans1, ans2;
  int A[4], B[4];
  int count, card, temp;

  cin >> T;
  for(int t = 1; t <= T; t++)
  {
    count = 0;
    card = 0;

    cin >> ans1;
    --ans1;
    for(int r = 0; r < 4; r++)
      for(int c = 0; c < 4; c++)
        if(r == ans1)
          cin >> A[c];
        else
          cin >> temp;

    cin >> ans2;
    --ans2;
    for(int r = 0; r < 4; r++)
      for(int c = 0; c < 4; c++)
        if(r == ans2)
          cin >> B[c];
        else
          cin >> temp;

    for(int i = 0; i < 4; i++)
      for(int j = 0; j < 4; j++)
        if(A[i] == B[j])
        {
          ++count;
          card = A[i];
        }

    cout << "Case #" << t << ": ";
    if(count == 0)
      cout << "Volunteer cheated!";
    else if(count == 1)
      cout << card;
    else
      cout << "Bad magician!";
    cout << endl;
  }
  return 0;
}
