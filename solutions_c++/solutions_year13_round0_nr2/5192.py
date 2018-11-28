/*

 E-Mail : mayank.ry@gmail.com
 Just For You :)

 */

#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;


//#define SMALL
#define LARGE
int main()
{
    int d1,d2,N,M,arr[102][102],i,j,k,status,max,K;
    int mark;

    #ifdef SMALL
	       freopen("B-small-attempt0.in","rt",stdin);
	       freopen("B-small.out","wt",stdout);
    #endif
    #ifdef LARGE
	       freopen("B-large.in","rt",stdin);
	       freopen("B-large.out","wt",stdout);
    #endif
    cin>>K;
    for(k =1;k<=K;k++)
    {
          cin>>M>>N;
          printf("Case #%d: ",k);
          for(i=1;i<=M;i++)
            {
                max = 0;
                for(j=1;j<=N;j++)
                {
                    cin>>mark;
                    //cout<<mark;
                    arr[i][j] = int(mark);
                    if(mark>max)
                    max=mark;
                }
                arr[i][N+1]=max;

            }

            d1=0;
            d2=0;

            for(i=1;i<=N;i++)
            {
                max = 0;
                for(j=1;j<=M;j++)
                {
                    if(arr[j][i]>max)
                    max=arr[j][i];
                }
                arr[M+1][i]=max;
            }

            status = 1;

            for(i=1;i<=M;i++)
            {
                for(j=1;j<=N;j++)
                {
                    if (arr[i][j]<arr[i][N+1] && arr[i][j]<arr[M+1][j])
                    {
                        status=0;
                        break;
                    }
                }
            }
            if (status==0)
            printf("NO \n");
            else
            printf("YES\n");

    }


	return 0;

}
