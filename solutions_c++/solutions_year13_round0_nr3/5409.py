#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <bitset>
#include <functional>
#include <utility>//pair
#include <iomanip>

using namespace std;
int huiwen(int n)
{
    int sum = 0;
    int t = n;
    while(t)
    {
        sum = sum*10+t%10;
        t/=10;
    }    
    //printf("%d %d\n",sum,n);
    if(sum==n) return 1;
    else return 0;
}    
int main()
{
    freopen("C-small-attempt2.in","r",stdin); 
    freopen("C-small.out","w",stdout);
    int a,b,t,l=1;
    scanf("%d",&t);
    while(t--)
    {
        int cnt = 0;
        scanf("%d%d",&a,&b);
        int m1 = (int)sqrt((double)a);
        if(m1*m1!=a) m1++;
        int m2 = (int)sqrt((double)b) + 1;
        //printf("%d %d\n",m1,m2);
        for(int i=m1;i<m2;i++)
        {
            if(huiwen(i)&&huiwen(i*i)) cnt++;
        }    
        printf("Case #%d: %d\n",l++,cnt);
    }    
    getchar(); getchar();
    return 0;
}
