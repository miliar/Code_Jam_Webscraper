#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <stdlib.h>
#include <string>
#include <queue>
#include <vector>
#include <set>
#define maxn
#define oo 1000000000
#define clearAll(a) memset(a,0,sizeof(a))
#define sq(a) ((a)*(a))
#define eps (1e-10)
using namespace std;

typedef long long ll;

int main()
{
    freopen("H:\\Users\\Yun\\Desktop\\input.txt","r",stdin);
    //freopen("H:\\Users\\Yun\\Desktop\\output.txt","w",stdout);
    int tt;
    cin >> tt;
    double C,F,X;
    double v=2.0;
    double ans=0.0;
    int id=0;
    double t1,t2;
    while (tt--)
    {
    	id++;
    	ans=0;
    	v=2.0;
    	cin >> C >> F >> X;
    	while (X>eps)
    	{
    		t1 = X / v;
    		t2 = C / v + X / (v+F);
    		if (t1-eps<t2)
    		{
    			ans += t1;
    			break;
    		} else
    		{
    			ans += C/v;
    			v += F;
    		}
    	}
    	printf("Case #%d: %.7f\n",id,ans);
    }

    return 0;
}
