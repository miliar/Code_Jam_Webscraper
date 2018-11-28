#include<iostream>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define inf 1000
using namespace std;
int row,col;
int desire[105][105];
int field[105][105];
int r_m[105],c_m[105];
void func_c_m()
{
    for(int j=0; j<col; j++)
    {
        int m=-1000;
        for(int i=0; i<row; i++)

        {

            m=max(m,desire[i][j]);

        }
        c_m[j]=m;
    }

}
void cutting()
{
    for(int i=0; i<row; i++)
    {
        for(int j=0; j<col; j++)
            field[i][j]=min( field[i][j],r_m[i]);
    }


   for(int j=0; j<col; j++)
    {
        for(int i=0; i<row; i++)

            field[i][j]=min(c_m[j],field[i][j]);
    }

}
bool checking()
{
    for(int i=0; i<row; i++)
    {
         for(int j=0; j<col; j++)
        {
            if(desire[i][j]!=field[i][j])
                return false;
        }
    }

return true;
}
int main()
{
    FILE *f;
    f=fopen("outputB.txt","w");
    int t,kase=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d %d",&row,&col);
        for(int i=0; i<row; i++)
        {
            int m=-1000;
            for(int j=0; j<col; j++)
            {

                scanf("%d",&desire[i][j]);
                m=max(m,desire[i][j]);
                field[i][j]=inf;
            }
            r_m[i]=m;
        }

        func_c_m();
        cutting();
        fprintf(f,"Case #%d: ",kase++);
        if(checking())
        {
            fprintf(f,"YES\n");
        }
        else
        {
            fprintf(f,"NO\n");
        }

       /* puts("OUTPUT:::\n");
           for(int i=0;i<row;i++)
          {
              for(int j=0;j<col;j++)
             cout<<field[i][j]<<" ";
             //cout<<c_m[i];
            puts("");
          }
          puts("\n");*/
//cout<<c_m[1];


    }
}
