#include<iostream>
using namespace std;

char arr[5][5];
int x = 0, o = 0;

void check_vertical()
{
     int i, j;
     char c;
     for(j=0;j<4;j++)
      {
        if(arr[0][j] != 'T')
          c = arr[0][j];
        else
          c = arr[1][j];
        for(i=1;i<4;i++)
         {
           if(arr[i][j] != 'T' && arr[i][j] != c)
            break;
         }
         if(i == 4)
          {
              if(c == 'X')
               x++;
              else if(c == 'O')
               o++;
          }
      }
}

void check_horizontal()
{
     int i, j;
     char c;
     for(i=0;i<4;i++)
      {
        if(arr[i][0] != 'T')
          c = arr[i][0];
        else
          c = arr[i][1];
        for(j=1;j<4;j++)
         {
           if(arr[i][j] != 'T' && arr[i][j] != c)
            break;
         }
         if(j == 4)
          {
              if(c == 'X')
               x++;
              else if(c == 'O')
               o++;
          }
      }
}

void check_diagonal()
{
     int i, j;
     char c;
     
     if(arr[0][0] != 'T')
       c = arr[0][0];
     else
       c = arr[1][1];
       
     for(i=0;i<4;i++)
      {
         if(arr[i][i] != 'T' && arr[i][i] != c)
            break;
      }
      if(i == 4)
      {
        if(c == 'X')
         x++;
        else if(c == 'O')
         o++;
      }
     
     if(arr[0][3] != 'T')
       c = arr[0][3];
     else
       c = arr[1][2];
        
     for(j=0,i=3;i>=0;i--,j++)
      {
         if(arr[j][i] != 'T' && arr[j][i] != c)
            break;
      }
      if(i == -1)
      {
        if(c == 'X')
         x++;
        else if(c == 'O')
         o++;
      }
}
          
int main()
{
    int i, j, k, t, s=1;
    int flg = 0;
    
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    
    scanf("%d", &t);
    getchar();
    while(t--)
     {
        x = 0;
        o = 0;
        flg = 0;
        for(i=0;i<4;i++)
         {
            scanf("%s", &arr[i]);
         }
         
        for(i=0;i<4;i++)
         {
           for(j=0;j<4;j++)
            {
              //printf("%c", arr[i][j]);
              if(arr[i][j] == '.')
               flg = 2;
            }
            //printf("\n");
         }
         
         check_vertical();
         check_horizontal();
         check_diagonal();
     
     printf("Case #%d: ", s);    
         if(x == o && flg == 0)
          printf("Draw\n");
         else if(x > o)
          printf("X won\n");
         else if(x < o)
          printf("O won\n");
         else if(x == o && flg == 2)
          printf("Game has not completed\n");
     
     s++;
     }
   //system("pause");                 
}
