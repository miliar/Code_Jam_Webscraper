#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;

int arr1[5][5], arr2[5][5];
int map1[17];
int ans1, ans2;
int t, c=1;
int flg = 0;
int ans = 0;

void initMap()
{
     for(int i=0;i<17;i++)
     {
                      map1[i] = 0;
     }
}

int main()
{
    int i, j;
    scanf("%d", &t);
    while(t--)
    {
              initMap();
              scanf("%d", &ans1);
              for(i=0;i<4;i++)
              {
                              for(j=0;j<4;j++)
                              {
                                              scanf("%d", &arr1[i][j]);
                                              if(i == (ans1-1))
                                              {
                                                   map1[arr1[i][j]] = 1;
                                              }
                              }
              }

              scanf("%d", &ans2);
              for(i=0;i<4;i++)
              {
                              for(j=0;j<4;j++)
                              {
                                              scanf("%d", &arr2[i][j]);
                              }
              }
              
              flg = 0;
              for(i=0;i<4;i++)
              {
                              if(map1[arr2[(ans2-1)][i]] == 1)
                              {
                                                         flg++;
                                                         ans = arr2[(ans2-1)][i];
                              }
              }
              
              if(flg == 0)
              {
                     printf("Case #%d: Volunteer cheated!\n", c++);
              }
              else if(flg == 1)
              {
                   printf("Case #%d: %d\n", c++, ans);
              }
              else
              {
                  printf("Case #%d: Bad magician!\n", c++);
              }
}
}
