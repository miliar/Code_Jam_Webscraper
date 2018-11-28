#include<stdio.h>
#include<stdint.h>
#include<math.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;

int main()
{
    int t,cas=1;
    scanf("%d",&t);
    while(t--)
    {
        int64_t arr[100][100]={0},ans[100][100]={0};
        int a,b,x=0;
        scanf("%d",&a);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&arr[i][j]);
                if(i+1==a)
                {
                     ans[a-1][arr[i][j]]=1;
                }
            }

        }
        scanf("%d",&b);
        int cnt=0,an;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&arr[i][j]);
                if(i+1==b)
                {
                    if(ans[a-1][arr[i][j]]==1)
                    {
                        cnt++;
                        an=arr[i][j];
                    }

                }
            }

        }
        printf("Case #%d: ",cas);
        if(cnt==0)
        {
            printf("Volunteer cheated!\n");
        }
       else if(cnt>1)
        {
            printf("Bad magician!\n");
        }
        else if(cnt==1)
        {
             printf("%d\n",an);
        }
        cas++;
    }
}
