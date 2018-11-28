#include <iostream>
#include <cstdio>
using namespace std;
int main()
{ int T;
    cin >> T;
    
    FILE* output;
        output = fopen("output.out","w"); 
    for (int count = 1; count <= T; count++)
    {
        fprintf(output ,"Case #%d: ", count);
        int fans, sans;
            cin >> fans;
        int a[4][4];
        int flag[17] = {0};
            for (int i = 0; i < 4; i++)
            {    for (int j = 0; j < 4; j++)
                { 
                    cin >> a[i][j];
                    if ( i == fans - 1 )
                        flag[a[i][j]] = 1;
                }
            }
            
        int ans = 0,p = 0;
            cin >> sans;
            for (int i = 0; i < 4; i++)
            {   for ( int j = 0; j < 4; j++)
                {
                    cin >> a[i][j];
                        if ( i == (sans - 1)  && flag[a[i][j]] == 1)
                            {  
                                ans = a[i][j];
                                p++;
                            }

                }

            }
        if ( p == 1)
             fprintf(output,"%d\n",ans);
        else if ( p > 1)
             fprintf(output,"Bad magician!\n");
        else
             fprintf(output,"Volunteer cheated!\n");
    }
   return 0;
}
