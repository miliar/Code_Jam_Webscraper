#include <iostream>
#include <fstream>
using namespace std;

int main()
{
  
    std::ifstream cin("input.txt"); 
   

    int T;
    int r;
    int a[2];
    int n[3][5][5]; 
    int N;
    int c = 0;
 int x =0;
    cin >> T ;
x=1;
    for(int l = 0; l<T; l++)
        {
            cin >> a[1];
            cin >> n[1][1][1];
            cin >> n[1][1][2];
            cin >> n[1][1][3]; 
            cin >> n[1][1][4];
            cin >> n[1][2][1];
            cin >> n[1][2][2];
            cin >> n[1][2][3];
            cin >> n[1][2][4];
            cin >> n[1][3][1];
            cin >> n[1][3][2];
            cin >> n[1][3][3];
            cin >> n[1][3][4];
            cin >> n[1][4][1];
            cin >> n[1][4][2];
            cin >> n[1][4][3];
            cin >> n[1][4][4];

            cin >> a[2]; 
            cin >> n[2][1][1] ;
            cin >> n[2][1][2];
            cin >> n[2][1][3];
            cin >> n[2][1][4];
            cin >> n[2][2][1];
            cin >> n[2][2][2];
            cin >> n[2][2][3];
            cin >> n[2][2][4];
            cin >> n[2][3][1];
            cin >> n[2][3][2];
            cin >> n[2][3][3];
            cin >> n[2][3][4];
            cin >> n[2][4][1];
            cin >> n[2][4][2];
            cin >> n[2][4][3];
            cin >> n[2][4][4];


            c = 0;

            for (int k=1;k < 5;k++)
            {

                for(int j=1;j < 5; j++)
                {

                    if(n[1][a[1]][k] == n[2][a[2]][j])
                    {
                        c++;
                        N=n[1][a[1]][k];
 
                    }

                }

            }
       

        if (c ==1)
        {
           printf ("Case #%d: %d \n",x, N);
        }
        else if(c == 0)
        {
            printf("Case #%d: Volunteer cheated!\n", x);
        } else
        { 
            printf("Case #%d: Bad magician!\n", x);
        }
  
   x++;
   }
   
   return 0;
}