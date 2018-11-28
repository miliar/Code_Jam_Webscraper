#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
#define Z
char a[1005];
int b[1005];
int main() {

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
    int t,n,i,cnt,tmp,cs=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        scanf("%s",&a);

        for(i=0;a[i];i++)
        {
            b[i]=a[i]-'0';
        }
        tmp=0; cnt=0;
        for(i=1;a[i];i++)
        {
           tmp+=b[i-1];
           if(tmp<i)
           {
               cnt+=(i-tmp);
               tmp+=(i-tmp);
           }
        }
        printf("Case #%d: %d\n",cs++,cnt);
    }
	return 0;
}
