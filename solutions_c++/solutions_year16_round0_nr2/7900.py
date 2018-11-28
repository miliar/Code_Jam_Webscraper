#include <iostream>
#include <sstream>
#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <vector>
#include <math.h>
#include <stack>
#include <queue>
#include <ctype.h>
#include <map>
#include <bitset>
#include <limits>
typedef long long ll;
#define filla(x,y) memset(x,y,sizeof(x))
#define pb push_back
#define mp make_pair
#define INF 0x3f3f3f3f
#define F first
#define S second
#define MOD 1000000007
using namespace std;
/*long long choose(int n,int k)
{
    if(k==0)
        return 1;
    else
    {
        long long f=1;
        if(k>n-k)
            k=n-k;
        int p=1;
        while(p<=k)
        {
            f*=n--;
            f/=p++;
        }
        return f;
    }
}
ll power(int a,int b)
{
    ll ret;
    if(b==0)
        return 1;
    if(b==1)
        return a;
    ret=power(a,b/2);
    ret=(ret*ret);
    if(b&1)
        ret=(ret*a);
    return ret;
}
bool cmp(int a,int b)
{
    return a>b;
}*/
int main()
{
    freopen("in2.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int z;
    string s;
    getline(cin,s);
    for(z=1;z<=t;z++)
    {
        getline(cin,s);
        int ctr=0,i;
        int l=s.length();
        for(i=1;i<l;i++)
        {
            if(s[i]==s[i-1])
                continue;
            else
            {
                ctr++;
            }
        }
        if(s[0]=='+')
        {
            if(ctr%2==0)
                printf("Case #%d: %d\n",z,ctr);
            else
                printf("Case #%d: %d\n",z,ctr+1);
        }
        else
        {
            if(ctr%2==0)
                printf("Case #%d: %d\n",z,ctr+1);
            else
                printf("Case #%d: %d\n",z,ctr);
        }
    }
    return 0;
}
