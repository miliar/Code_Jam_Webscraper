#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <utility>
#include <stack>
#include <sstream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <deque>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>

using namespace std;

#define FOR(i,a,b)				for (i=a;i<b;i++)
#define s(n)					scanf("%d",&n)
#define p(n)					printf("%d\n",n)
#define sd(n)					int n;scanf("%d",&n)
#define pb(n)                                   push_back(n)
#define clr(a)                                  memset(a,0,sizeof(a))
#define all(c)                                  (c).begin(),(c).end()
#define PI 3.14159265
#define mod 747474747
#define MAX 6666

typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <string> vstr;
typedef long long ll;
int i,j,k;

int mulmod(int a,int b,int MOD)
{
	ll t=(ll)a*b;
	if (t>=MOD) t=t%MOD;
	return t;
}

int addmod(int a,int b,int MOD)
{
	ll t=(ll)a+(ll)b;
	if (t>=MOD) t=t%MOD;
	return t;
}

int main()
{
    
    int T=1;
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    //T = g_fi.ReadNext();
    cin>>T;
    int arr[1001];
    int temp=0;
    FOR(i,0,1001)
    {
        if(i==1 || i==4 || i==9||i==121||i==484)
            temp++;
        arr[i]=temp;
    }
    FOR(k,0,T)
    {
        int a,b;
        cin>>a>>b;
        int ans = arr[b] - arr[a-1];
        cout<<"Case #"<<k+1<<": "<<ans<<endl;
    }
    return 0;
}