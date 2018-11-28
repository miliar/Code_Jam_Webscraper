#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>
#include <utility>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <deque>
#include <iostream>
#include <math.h>
#include <sstream>
#include <assert.h>
#include <numeric>
#include <fstream>
#include <limits>
#include <bitset>
#define INF 0x3f3f3f3f
#define MAX 1000

using namespace std;

int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int caso=1; caso<=t; caso++)
    {
        double c,f,x;
        scanf("%lf%lf%lf",&c,&f,&x);

        double minimum_time=x/2.0, time;
        double t_farms[100000];

        t_farms[0] = c/2.0;
        for(int i=1; i<100000; i++)
        {
            t_farms[i] = t_farms[i-1] + (c/(2+f*(double)i));
        }

        for(int i=0; i < 100000; i++)
        {
            time = t_farms[i] + x/(2+f*(double)(i+1));
            minimum_time = min(minimum_time, time);
        }

        printf("Case #%d: %.7lf\n",caso,minimum_time);
    }
    return 0;
}

