#include <iostream>
#include <fstream>

using namespace std;
ifstream f("inputa.txt");
ofstream g("a.txt");


int t;
int a[5][5];
int ans1[4],ans2[4];
int x1,x2;

int main()
{
    f >> t;
     for (int k=0; k < t; k++)
     {
        f >> x1;
         for (int i = 0; i < 4 ; i++)
            for (int j = 0; j < 4 ; j++)
                f >> a[i][j];
        for (int i = 0 ; i < 4 ; i++)
            ans1[i] = a[x1-1][i];

        f >> x2;
         for (int i = 0; i < 4 ; i++)
            for (int j = 0; j < 4 ; j++)
                f >> a[i][j];
        for (int i = 0 ; i < 4 ; i++)
            ans2[i] = a[x2-1][i];

       int sol = 0 , ras;

       for (int i = 0 ; i < 4 ; i++)
         for (int j = 0; j < 4 ; j++)
           if (ans1[i] == ans2[j])
           {
               sol++;
               ras = ans1[i];
           }
         g << "Case #"<< k+1 << ": ";
        if (sol == 1) g << ras << '\n';
            else if (sol > 1) g << "Bad magician!\n";
                else g << "Volunteer cheated!\n";
     }

    return 0;
}
