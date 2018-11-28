#include <cstdio>

using namespace std;

int main()
{
    int testcase,row,check=0,number=0,save[4],num[100];
    int m[4][4],j,k,p,n;


    scanf(" %d", &testcase);


    for(p=1;p<=testcase;p++)
    {
        check=0;
    for(n=0;n<2;n++)
    {
       scanf(" %d", &row);
        row--;
    for(j=0;j<4;j++)
    {
        for(k=0;k<4;k++)
        {
scanf(" %d", &m[j][k]);

        }
    }
    if(check==0)
    {
    for(int i=0;i<4;i++)
    {
        save[i]=m[row][i];
        check=1;
    }
    }
    else
    {
        number=0;
            for(j=0;j<4;j++)
            {
                for(k=0;k<4;k++)
                {

                    if(save[j]==m[row][k])
                    {
                    if(number==0)
                    {
                         num[p-1]=m[row][k];
                         number=1;
                         break;
                    }
                    else
                    {
                        num[p-1]=17;
                    }
                    }
                }
            }
            if(number==0)
            num[p-1]=18;
    }
    }

    }
    for(p=1;p<=testcase;p++)
    {
     printf("Case #%d: ",p);
     if(num[p-1]==17)
      printf("Bad magician!");
     else if(num[p-1]==18)
      printf("Volunteer cheated!");
     else
     printf("%d",num[p-1]);
     printf("\n");
    }
    return 0;
}
