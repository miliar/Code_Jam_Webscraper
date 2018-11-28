#include <stdio.h>
#include <stdlib.h>

int main()
{
    int T,Orin_M[4][4],Change_M[4][4];
    freopen("C:\\Users\\zy\\Desktop\\A-small-attempt8.in","r", stdin);
    freopen("C:\\Users\\zy\\Desktop\\A-small-attempt8.txt","w", stdout);
    scanf("%d",&T);
    int k = 1;
    int i,j;
    while(T > 0)
    {
       int om,cm;
       scanf("%d",&om);
       for(i = 0; i < 4; i ++)
       {
           for(j = 0; j < 4; j ++)
             scanf("%d",&Orin_M[i][j]);
       }
       scanf("%d",&cm);
       for(i = 0; i < 4; i ++)
       {
           for(j = 0; j < 4; j ++)
             scanf("%d",&Change_M[i][j]);
       }
        printf("Case #%d: ",k);
     int count = 0;
     int temp;
     for(i = 0; i < 4; i ++)
     {
        for(j = 0; j < 4; j++)
        {
           if(Orin_M[om-1][i] == Change_M[cm-1][j]) 
           {  count++; temp = Orin_M[om-1][i];
            }
        }
     }
     if(count == 0) printf("Volunteer cheated!\n");
     if(count == 1) printf("%d\n",temp);
     if(count > 1) printf("Bad magician!\n");
     k++;
       T--;
    }
    
    
    system("pause"); 
    return 0; 
}
