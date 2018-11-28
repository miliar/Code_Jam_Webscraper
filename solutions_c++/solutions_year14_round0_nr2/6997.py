//RandomUsername(Nikola Jovanovic)
//Google Code Jam 2014
//Qualification Round
//B : Cookie Clicker

#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>
#include <set>
#include <queue>
#include <stack>

using namespace std;

int t;
double c,f,x,inc,tim;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    //cout<<t<<endl;
    for(int tt=1;tt<=t;tt++)
    {
       scanf("%lf %lf %lf",&c,&f,&x);
       inc=2.0;
       tim=0.0;
       while(!( c/inc + x/(inc+f) > x/inc ))
       {
           tim+=c/inc;
           inc+=f;
       }
       tim+=x/inc;
       printf("Case #%d: %0.10lf\n",tt,tim);
    }
    return 0;
}
