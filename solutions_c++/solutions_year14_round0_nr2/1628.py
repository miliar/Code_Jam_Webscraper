#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<string>
#include<queue>
#include<set>
#include<map>
#include<iostream>
#include<cmath>
using namespace std;
#define mem(a,b) memset(a,b,sizeof(a))
#define pb push_back
typedef long long ll;

const int N = 110000;

int main()
{
	int T; scanf("%d",&T);
	for(int ka=1;ka<=T;ka++) {
        double c,x,f;
        scanf("%lf%lf%lf",&c,&f,&x);
        int k= max(0.0,((x+c)*f-2*c)/c/f-1);
        printf("Case #%d: ",ka);
        double t=0;
        for(int i=0;i<k;i++) {
            t+= c/(2+i*f);
        }
        t+= x/(2+k*f);
        printf("%.7f\n",t);
	}

    return 0;
}
