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


#define SMALL
//#define LARGE
int main()
{
    int A,B,i,j,k,K,ans;
    int mark;

    #ifdef SMALL
	       freopen("C-small-attempt0.in","rt",stdin);
	       freopen("C-small.out","wt",stdout);
    #endif
    #ifdef LARGE
	       freopen("C-large.in","rt",stdin);
	       freopen("C-large.out","wt",stdout);
    #endif
    cin>>K;
    for(k =1;k<=K;k++)
    {
          cin>>A>>B;
          printf("Case #%d: ",k);
            ans = 0;

            if (1>=A && 1<=B)
            ans++;

            if (4>=A && 4<=B)
            ans++;

            if (9>=A && 9<=B)
            ans++;

            if (121>=A && 121<=B)
            ans++;

            if (484>=A && 484<=B)
            ans++;


            printf("%d\n",ans);

    }


	return 0;

}
