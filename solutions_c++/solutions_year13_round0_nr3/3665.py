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
#include <string.h>

#define SZ(c) c.size()
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define SORT(a) sort(a.begin(),a.end())
#define tests int test; scanf("%d",&test); while(test--)
#define dbg(n) cout<<#n<<" = "<<n<<endl;

using namespace std;

int strToInt(string str)
{
    int ans;
    stringstream s;
    s<<str;
    s>>ans;
    return ans;
}
string intToStr(int n)
{
    string str;
    stringstream s;
    s<<n;
    s>>str;
    return str;
}
int MAX(int a,int b)
{
    if(a >b) return a;
    return b;
}
int MIN(int a,int b)
{
    if(a <b) return a;
    return b;
}
int ABS(int a,int b)
{
    if(a >0) return a;
    return -a;
}

bool isPalin(int num)
{
    string str;
    str = intToStr(num);
    int len = str.size();
    for(int i=0;i<len;i++)
    {
        if(str[i]!=str[len-1-i])
            return false;
    }
    return true;
}

int main()
{
    freopen("read.txt","r",stdin);
    freopen("write.txt","w",stdout);
    int test;
    scanf("%d",&test);
    int n,m;

    for(int k=1; k<=test; k++)
    {
        scanf("%d %d",&n,&m);
        int ans =0,root;
        for(int i=n; i<=m;i++)
        {
            root = (int) sqrt((double)i);
            if(root*root != i)
                root =-1;
            if(isPalin(i) && isPalin(root))
                ans++;
        }
        printf("Case #%d: %d\n",k,ans);
    }


    return 0;
}



