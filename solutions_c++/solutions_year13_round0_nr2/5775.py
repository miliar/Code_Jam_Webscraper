#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <memory>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;



int main()
{
int test,i,j,c,a,b,st[20][20]={0},st1[20][20]={0},p,t;
  freopen("input.txt","r",stdin);
 freopen ("output.txt","w",stdout);
    scanf("%d",&t);
    for(test=1;test<=t;test++)
    {
        c=1;
        scanf("%d%d",&a,&b);
        for(i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
            {
                scanf("%d",&st[i][j]);
            }
        }

        for(i=0;i<a;i++)
        {
            int p1=i,count=0;
            for(j=0;j<b;j++)
            {
                if(st[i][j]==2)
                {

              for(p=0;p<b;p++)
              {st1[p1][p]=2;}

                c=0;
                break;
                }
                else
                count++;

            }

            if(count==b)
          for(p=0;p<b;p++)
            {
                st1[i][p]=1;
            }
            }

        for(j=0;j<b;j++)
        {
            for(i=0;i<a;i++)
            {
                if(st[i][j]!=st1[i][j])
                {
                    for(p=0;p<a;p++)
                    {
                    st1[p][j]=1;
                    }
                    break;

                }
            }
        }

        c=1;

        for(i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
            {
                if(st[i][j]!=st1[i][j])
                {
                    printf("Case #%d: NO\n",test);
                    c=0;break;


                }
            }
            if(c==0)
            break;
        }
        if(c!=0)
        printf("Case #%d: YES\n",test);
}




    return 0;
}
