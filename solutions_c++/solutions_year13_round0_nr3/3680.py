#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

int main()
{
    freopen( "input3.in", "r", stdin );
	freopen( "output3.out", "w", stdout );

    int test,kase=0;
    scanf("%d",&test);
    while(test--)
    {
        int lo,hi,i,ans=0;
        scanf("%d%d",&lo,&hi);
        for(i=lo;i<=hi;i++)
        {
            int tmp,chk=0,val=i;
            while(val!=0)
            {
                tmp=val%10;
                chk=tmp+(chk*10);
                val=val/10;
            }

            if(chk==i)
            {
                double frac=sqrt(i);
                int flor=int(frac);
                if(frac==flor)
                {
                    val=flor;
                    chk=0;
                    while(val!=0)
                    {
                        tmp=val%10;
                        chk=tmp+(chk*10);
                        val=val/10;
                    }
                    if(chk==flor)
                    {
                        ans++;
                    }
                }
            }
        }

        printf("Case #%d: %d\n",++kase,ans);
    }
    return 0;
}
