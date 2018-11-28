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
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int check(int x)
{
    int i,j,k,len=1;
    if(x>=100)
        len=3;
    else if(x>=10 && x<100)
        len=2;
    if(len==1)
        return 1;
    else if (len==2)
    {
        k=x;
        if((k/10)==(k%10))
            return 1;
    }
    else
    {
        k=x;
        if((k/100)==(k%10))
            return 1;
    }
    return 0;
}
int main()
{
    //fflush(stdin);
    freopen("problem3.txt","r",stdin);
    freopen("ans3.txt","w",stdout);
    int i,j,k,N,count=0,A,B,m,d;
    scanf("%d",&N);
    for(i=1;i<=N;i++)
    {
        scanf("%d %d",&A,&B);
        d=(floor)(sqrt(A));
        count=0;
        for(j=d;j<=31;j++)
        {
            if((j*j)<=B && (j*j)>=A)
            {
                k=check(j*j);
                m=check(j);
                if(k==1 && m==1)
                {
                    count++;
                }
            }
        }
        printf("Case #%d: %d\n",i,count);
    }
    return 0;
}

