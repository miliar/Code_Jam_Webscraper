/*

*/

#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <unistd.h>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <sstream>
#include <cctype>
#include <climits>
#include <iterator>


using namespace std;

int T,t;
unsigned long long i,p,q,temp;
float elf;

void solve()
{
    scanf("%d",&T);
    for(t=1;t<=T;++t)
    {
        temp=1;
        bool flag=false;
        scanf("%lld/%lld",&p,&q);
        elf=(float)p/(float)q;
        while(temp<q)
        {
            temp*=2;
            if(temp==q)
                flag=true;
        }
        for(i=1;;++i)
        {
            elf*=2;
            if(elf>=1 && flag)
            {
                cout << "Case #" << t << ": " << i << endl;
                break;
            }
            else if(!flag && elf>1)
            {
                printf("Case #%d: impossible\n",t);
                break;
            }
        }
    }
}

int main(int argc,char *argv[])
{
	solve();
    return 0;
}
