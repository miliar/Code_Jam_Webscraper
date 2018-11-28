#include <iostream>
#include <conio.h>

using namespace std;

void Solve(int k)
{
     int a,b, number;
     int A[4], B[4];
     cin >> a;
     for (int i=0; i<4; i++)
         if (i==a-1)
            for (int j=0; j<4; j++)
                cin >> A[j];
         else
         {
             int temp;
             for (int j=0; j<4; j++)
                 cin >> temp;
         }
         
     bool found_1=false, found_2=false;
     cin >> b;
     for (int i=0; i<4; i++)
         if (i==b-1)
            for (int j=0; j<4; j++)
            {
                int temp;
                cin >> temp;
                for (int q=0; q<4; q++)
                {
                    if (temp==A[q])
                       if (!found_1)
                       {
                          found_1=true;
                          number=temp;
                       }
                       else
                           found_2=true;
                }
            }
         else
         {
             int temp;
             for (int j=0; j<4; j++)
                 cin >> temp;
         }
     
     if (found_2)
        cout << "Case #" << k+1 << ": Bad magician!" << endl;
     if (!found_2 && found_1)
        cout << "Case #" << k+1 << ": " << number << endl;
     if (!found_2 && !found_1)
        cout << "Case #" << k+1 << ": Volunteer cheated!" << endl;
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("OUTPUT.txt", "w", stdout);
    int K;
    cin >> K;
    for (int i=0; i<K; i++)
        Solve(i);
    return 0;
}
