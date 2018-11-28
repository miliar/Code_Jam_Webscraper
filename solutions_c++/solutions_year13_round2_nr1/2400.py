#include <iostream>
#include <stdio.h>
#include <vector>
#include <math.h>
using namespace std;
int TMP;
int count_stps(int st, int dest)
{
    int sum=st;
    int cnt=0;
    while(sum<=dest)
    {
                    sum += (sum-1);
                    cnt++;
    }
    TMP=sum;
    return cnt;
}                    
int main()
{
    int t;
    scanf("%d", &t);
    int strt;
    int n,sum;
    int t1;
    int cnt;
    vector<int> V;
    for(int k=1; k<=t; k++)
    {
         sum = 0;
         cnt = 0;
         V.clear();
         scanf("%d %d",&strt, &n);
         for(int i=0; i<n; i++)
         {
                 scanf("%d", &t1);
                 V.push_back(t1);
         }
         if(strt==1)
         {
                    printf("Case #%d: %d\n", k, n);
                    continue;
                    }
         sort(V.begin(), V.end());
         sum = strt;
         for(int i=0; i<n; i++)
         {
                 if(sum > V[i])
                        sum += V[i];
                 else
                 {
                      int tmp = count_stps(sum, V[i]);
                  //    printf("-->%d\n", tmp);
                      if(tmp < n-i)//it means its better to add than removing further elements...
                      {
                           sum = TMP+V[i];
                     //      printf("s=>%d\n", sum);
                           cnt += tmp;
                      }
                      else //if its better to remove the elements further.. than to continue...
                      {
                            cnt += n-i;
                            break;
                      }
                 }
         }
         printf("Case #%d: %d\n", k, cnt);
    }
    return 0;
}                                              
