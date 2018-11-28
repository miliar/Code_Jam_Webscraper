#include <cassert>
#include <cctype>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <list>
#include <deque>
#include <stack>
#include <iterator>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <functional>
#include <numeric>
#include <algorithm>
using namespace std;
int main()
{
    freopen("1a.in","r",stdin);
    freopen("1a.out","w",stdout);
    int te;
    cin>>te;
    for(int c=1;c<=te;c++)
    {
    long long r ,t;
    cin>>r>>t;
    int n=0;
    while(1)
    {
    int temp=((r+1)*(r+1))-(r*r);
    if(t>=temp){
    n++;
    t-=temp;
    }
    else break;
    r=r+2;
    }
    printf("Case #%d: %d\n",c,n);
    }
return 0;
}
