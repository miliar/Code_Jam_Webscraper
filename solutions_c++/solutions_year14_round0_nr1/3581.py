#include<iostream>
using namespace std;
int main()
{
    int t;
    scanf("%d",&t);
    for(int d=1;d<=t;d++)
    {
              int x,a1,a2,a3,a4;
              scanf("%d",&x);
              int a[4][4];
              for(int i=0;i<4;i++)
              {
                      for(int j=0;j<4;j++)
                      {
                              scanf("%d",&a[i][j]);
                             
                      }
                      if(i==x-1)
                              { a1=a[i][0];
                              a2=a[i][1];
                              a3=a[i][2];
                              a4=a[i][3];
                              }
              }
              int y,c=0,s;
              scanf("%d",&y);
              int b[4][4];
              for(int i=0;i<4;i++)
              {
                      for(int j=0;j<4;j++)
                      {
                              scanf("%d",&b[i][j]);
                              if(i==y-1)
                              {
                                        if(b[i][j]==a1 || b[i][j]==a2 ||b[i][j]==a3||b[i][j]==a4)
                                        {c++;
                                        if(c==1) s=b[i][j];
                                        }
                              }
                      }
              }
              if(c==1)
              printf("Case #%d: %d\n",d,s);
              else
              {
                  if(c==0)
                  printf("Case #%d: Volunteer cheated!\n",d);
                  else
                  printf("Case #%d: Bad magician!\n",d);
              }
              
    }
    return 0;
}

              
