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

int is_palin(char *s)
{
    int len=strlen(s);
    for(int i=0;i<len/2;i++)
    {
        if(s[i] != s[len-1-i])
        {
            return 0;
        }
    }

    return 1;

}



int main() 
{

        freopen ("C-small-attempt0.in","r",stdin);
        freopen ("out.txt","w",stdout);

        int T;
        scanf("%d",&T);
       
        int testcase=0;
        while(T--)
        {
            int A,B;
            scanf("%d%d",&A,&B);

            int count=0;
            for(int i=A;i<=B;i++)
            {
                char s[20];
                sprintf(s,"%d",i);
                
                if( !is_palin(s)) continue;

                int tmp=sqrt(i);
                if(tmp*tmp != i) continue;

                sprintf(s,"%d",tmp);

                if( !is_palin(s)) continue;

                ++count;
            }

            printf("Case #%d: %d\n",++testcase, count);
        }


		return 0;
}


