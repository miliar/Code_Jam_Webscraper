#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int findAns(int tab[4][4])
{
    int sum;
    for(int i=0;i<4;i++)
    {
        sum=tab[0][i]+tab[1][i]+tab[2][i]+tab[3][i];
        if(sum/100==4) return 2;
        if((sum/10)%10==4) return 1;
    }
    sum=tab[0][0]+tab[1][1]+tab[2][2]+tab[3][3];
        if(sum/100==4) return 2;
        if((sum/10)%10==4) return 1;
    sum=tab[0][3]+tab[1][2]+tab[2][1]+tab[3][0];
        if(sum/100==4) return 2;
        if((sum/10)%10==4) return 1;
    int temp=0;
    for(int i=0;i<4;i++)
    {
        sum=tab[i][0]+tab[i][1]+tab[i][2]+tab[i][3];
        if(sum/100==4) return 2;
        if((sum/10)%10==4) return 1;
         //printf("temp=%d",temp);
        temp=temp+sum;
    }

    if(temp%10==0) return 3;
    else return 4;
}

int main(int argc, char *argv[]) {
  FILE *in;
  in=fopen("A-small-attempt1.in","r");
  int n;
  fscanf(in,"%d",&n);
  char buff[n][4];
  int ans[n];
  int table[4][4];
  for (int i = 0;i<n;i++) {
        for(int k=0;k<4;k++)
        {
            fscanf(in,"%s",&buff[i]);
            for(int j=0;j<4;j++)
            {
                if(buff[i][j]=='O') table[k][j]=100;
                else if(buff[i][j]=='X') table[k][j]=10;
                else if(buff[i][j]=='T') table[k][j]=110;
                else table[k][j]=1;
               // printf("table[%d][%d]=%d\n",k,j,table[k][j]);
            }
        }
        ans[i]=findAns(table);
        //printf("%d",ans[i]);
  }
    FILE *out;
    out=fopen("output1.txt","w");
  for(int q=0;q<n;q++)
  {
      if(ans[q]==1) fprintf(out,"Case #%d: X won\n",q+1);
      else if(ans[q]==2) fprintf(out,"Case #%d: O won\n",q+1);
      else if(ans[q]==3) fprintf(out,"Case #%d: Draw\n",q+1);
      else fprintf(out,"Case #%d: Game has not completed\n",q+1);
  }
}
