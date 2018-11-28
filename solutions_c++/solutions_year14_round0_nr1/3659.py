#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <utility>
#define inf 2000000000
#define ll long long
#define Max 105

using namespace std;


int main()
{
    int n,choice1,choice2,temp;
    int array[16],t1[4],t2[4];
    freopen("input.in","r",stdin);
     freopen("out.in","w",stdout);
    scanf("%d", &n);
    for(int i=0; i<n;i++)
    {
        scanf("%d", &choice1);
       for(int j=0;j<16;j++)
        {
            scanf("%d",&array[j]);
          //  cout<<array[j]<<" ";
        }
        t1[0] = array[(4*(choice1-1))];
        t1[1] = array[(4*(choice1-1)) + 1];
        t1[2] = array[(4*(choice1-1)) +2];
        t1[3] = array[(4*(choice1-1)) +3];

        scanf("%d", &choice2);
        for(int j=0;j<16;j++)
        {
            scanf("%d",&array[j]);
          // cout<<array[j]<<" ";
        }
        t2[0] = array[(4*(choice2-1))];
        t2[1] = array[(4*(choice2-1)) + 1];
        t2[2] = array[(4*(choice2-1)) +2];
        t2[3] = array[(4*(choice2-1)) +3];

        int count =0;
        int flag=0;
        int num;
        for(int k=0; k<4;k++)
        {
            for(int m=0;m<4;m++)
            {
                if(t1[k] == t2[m])
                  {
                      count++;
                      num = t1[k];
                      if(flag == 0)
                        flag =1;
                       else
                        flag = 2;
                  }
                  if(flag == 2)
                    break;
            }
           if(flag == 2)
                    break;

        }

        if(flag == 0)
            printf("Case #%d: Volunteer cheated!\n",i+1);

        if(flag == 1)
            printf("Case #%d: %d\n",i+1,num);
        if(flag == 2)
            printf("Case #%d: Bad magician!\n",i+1);


    }

    return 0;
}
