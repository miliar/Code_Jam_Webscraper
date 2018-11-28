#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
using namespace std;


int main() 
{

        freopen ("B-small-attempt0.in","r",stdin);
        freopen ("lawn_out.txt","w",stdout);



        int T;
        scanf("%d",&T);

        int testcase=0;
        while(T--)
        {
            int N,M;
            scanf("%d%d",&N,&M);

            int arr[N+1][M+1];

            for(int i=0;i<N;i++)
            {
                for(int j=0;j<M;j++)
                {
                    scanf("%d",&arr[i][j]);
                }
            }


            int flag[N+1][M+1];
            memset(flag, 0, sizeof(flag));



            for(int i=0;i<N;i++)
            {
                int maxx=-1;

                for(int j=0;j<M;j++)
                {
                    maxx=max(maxx,arr[i][j]);
                }

                for(int j=0;j<M;j++)
                {
                    if(arr[i][j] == maxx)
                    {
                        flag[i][j]=-1;
                    }
                }
            }


            int flag2=1;
            
            for(int i=0;i<N;i++)
            {
                for(int j=0;j<M;j++)
                {
                    if(flag[i][j] == 0)
                    {
                        for(int k=0;k<N;k++)
                        {
                            if(arr[k][j] == arr[i][j]) continue;
                            else
                            {
                                flag2=0;
                                goto down;
                            }
                        }
                    }
                }
            }

            down:
             if(flag2 == 0)
             {
                 printf("Case #%d: NO\n",++testcase);
             }
             else
             {
                 printf("Case #%d: YES\n",++testcase);

             }

        }


		return 0;
}


