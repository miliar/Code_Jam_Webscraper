#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<algorithm>
#include<ctime>
#include<cctype>
#include<cmath>
#include<string>
#include<cstring>
#include<stack>
#include<queue>
#include<vector>
#include<map>
#define sqr(x) ((x)*(x))
#define LL long long
#define INF 0x3f3f3f3f
#define PI 3.14159265358979
#define eps 1e-10
#define mm

using namespace std;

double c,f,x,s,temp,total;

int main()
{
	#ifndef ONLINE_JUDGE
		freopen("t","r",stdin);
        freopen("t2","w",stdout);
	#endif

	int tt;

	scanf("%d",&tt);


	for (int t=1;t<=tt;t++)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        s=2;
        temp=0;
        total=0;
        while (x/s>(c/s+x/(s+f)))
        {
            total+=(c/s);
            s+=f;
        }

        total+=(x/s);

        printf("Case #%d: %.7f\n",t,total);


    }


	return 0;
}
