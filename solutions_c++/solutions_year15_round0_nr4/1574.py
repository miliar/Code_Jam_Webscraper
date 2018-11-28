  /*Harsh Vardhan :) */

#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<vector>
#include<set>
#include<map>
#include<stdlib.h>
#include<string.h>
#include<queue>
#include<stack>

using namespace std;

#define MAX 100005
#define gi(n) scanf("%d",&n)
#define gl(n) scanf("%lld",&n)
#define pi(n) printf("%d\n",n)
#define pl(n) printf("%lld\n",n)
#define all(c) c.begin(), c.end()
#define MOD 1000000007
#define M_PI 3.14159265358979323846
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define mp make_pair
#define F first
#define S second
#define SET(p,v) memset(p, v, sizeof(p))
#define chkC(x,n) (x[n>>6]&(1<<((n>>1)&31)))
#define setC(x,n) (x[n>>6]|=(1<<((n>>1)&31)))
typedef long long ll;
typedef pair<int,int> pii;

int main()
{
    //freopen("H:\\input.txt","r",stdin);
    //freopen("H:\\output.txt","w",stdout);
    int t;
    gi(t);
    for(int i=1;i<=t;i++)
    {
        int x,r,c;
        gi(x);gi(r);gi(c);
        if((((r>=x) && (c>=x-1)) || ((r>=x-1)&&(c>=x)))&&((r%x==0)||(c%x==0)))
				printf("Case #%d: GABRIEL\n",i);
        else
				printf("Case #%d: RICHARD\n",i);
    }
    return 0;
}