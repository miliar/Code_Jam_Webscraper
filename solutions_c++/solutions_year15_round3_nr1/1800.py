#include <stdio.h>
#include <iostream>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <string>
#include <algorithm>
#include <cmath>
#include <limits.h>
#include <set>
#include <stack>
#include <vector>
#include <map>
#include <queue>
#include <sstream>
#define mod 1000000007
#define M_PI 3.14159265358979323846
using namespace std;
long long power(int b , int pow)
{
    if(pow ==0)
        return 1;
    if(pow&1)
        return b *power(b,pow-1);
    long long temp= power(b,pow/2);
    return temp * temp;

}
int main()
{
  freopen("inpt.in","r",stdin);
   freopen("output.in","w",stdout);
    cin.sync_with_stdio(false);
    int t ;
    int tc=1;
    cin >> t;
    //memset(dp,-1,sizeof dp);
    while(t--)
    {
        int n,r,c;
        cin >> r;
        cin >> c;
        cin >> n;
        long long res = c/n +(n-1)+(c%n !=0);
        cout << "Case #" <<tc++ <<": "<<res*r<<endl;
        //printf("Case #%d: %0.6f\n",tc++,res);
    }
    return 0;
}


