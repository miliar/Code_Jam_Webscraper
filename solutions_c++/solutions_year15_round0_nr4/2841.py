#include <iostream>
#include <cstdio>

FILE *fin = fopen("input.txt","r");
FILE *fout = fopen("output.txt","w");
using namespace std;
void proc()
{
  int x,r,c;
  fscanf(fin,"%d %d %d",&x,&r,&c);
  if(r>c)
  {
      int temp=r;
      r=c;
      c=temp;
  }
  int result[5][5][5];
  //G:1
  //R:2
  result[1][1][1]=1;
  result[1][1][2]=2;
  result[1][1][3]=2;
  result[1][1][4]=2;

  result[1][2][1]=1;
  result[1][2][2]=1;
  result[1][2][3]=2;
  result[1][2][4]=2;

  result[1][3][1]=1;
  result[1][3][2]=2;
  result[1][3][3]=2;
  result[1][3][4]=2;

  result[1][4][1]=1;
  result[1][4][2]=1;
  result[1][4][3]=2;
  result[1][4][4]=2;

  result[2][2][1]=1;
  result[2][2][2]=1;
  result[2][2][3]=2;
  result[2][2][4]=2;

  result[2][3][1]=1;
  result[2][3][2]=1;
  result[2][3][3]=1;
  result[2][3][4]=2;

  result[2][4][1]=1;
  result[2][4][2]=1;
  result[2][4][3]=2;
  result[2][4][4]=2;

  result[3][3][1]=1;
  result[3][3][2]=2;
  result[3][3][3]=1;
  result[3][3][4]=2;

  result[3][4][1]=1;
  result[3][4][2]=1;
  result[3][4][3]=1;
  result[3][4][4]=1;

  result[4][4][1]=1;
  result[4][4][2]=1;
  result[4][4][3]=2;
  result[4][4][4]=1;
  /*
     1 2 3 4
1 1 G R R R
1 2 G G R R
1 3 G R R R
1 4 G G R R
2 2 G G R R
2 3 G G G R
2 4 G G R R
3 3 G R G R
3 4 G G G G
4 4 G G R G
*/
/*
for(int i=1;i<=4;i++)
    for(int j=1;j<=4;j++)
    {
        if(i<=j)
        {
            for(int k=1;k<=4;k++)
                fprintf(fout,"%d ",result[i][j][k]);
            fprintf(fout,"\n");
        }
    }
    */

 if(result[r][c][x]==1)
    fprintf(fout,"GABRIEL\n");
 else
    fprintf(fout,"RICHARD\n");
}
int main()
{
    int t;
    fscanf(fin,"%d",&t);
    for(int i=0;i<t;i++)
    {
        fprintf(fout,"Case #%d: ",i+1);
        proc();
    }
    return 0;
}
