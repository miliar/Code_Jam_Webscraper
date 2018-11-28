#include<stdio.h>
#include<stdint.h>
#include<math.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;

int main()
{
    int t,cas=1,ca=1;
    scanf("%d",&t);
    while(t--)
    {
        double c,f,x,cok=2,time=0;
        scanf("%lf%lf%lf",&c,&f,&x);
        double min=x/2.0;
        while(cas)
        {
            time+=c/cok;
            //printf("time=%f\n",time);
            cok+=f;
            //printf("cook=%f\n",cok);
            double temp=time+(x/cok);
            //printf("temp=%f\n",temp);
            if(min>temp)
            {
                min=temp;
            }
            if(temp>min)
                break;
        }
        printf("Case #%d: ",ca);
        printf("%.7f\n",min);
        ca++;
    }
}
