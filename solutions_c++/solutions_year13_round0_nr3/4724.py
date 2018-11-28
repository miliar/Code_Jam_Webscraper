/*CODE_BY_MANAS_KIRTI
Algo:Ad-hoc
Date:13/04/2013*/
using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include<bitset>
#include <set>
# define LLU long long  int
# define LLD long long double
# define FOR(i,N) for(int i=0;i<(N);i++)
# define FOR1(i,a,N) for(int i=a;i<(N);i++)
# define pb push_back
# define in(x) scanf("%d",&x)
# define out(x) printf("%d\n",x)
# define clr(a) memset(a,0,sizeof(a))
# define fill(a,x) memset(a,x,sizeof(a))
# define mp make_pair
# define INF_MAX 2147483647
# define INF_MIN -2147483647
# define maxn 51
# define mod 1000000007
LLU arr[]={1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002};
int main()
{
    int t,cas=1;
    LLU x,y;
    in(t);
    while(t--)
    {
       cin>>x>>y;
       int ans=0;
       FOR(i,39)
       if(arr[i]*arr[i]>=x && arr[i]*arr[i]<=y)
       ans++;
       printf("Case #%d: ",cas++);
       out(ans);
    }
    return 0;
}
