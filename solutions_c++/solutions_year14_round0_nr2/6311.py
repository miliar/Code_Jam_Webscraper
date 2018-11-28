#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<ctime>
#include<assert.h>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<limits.h>

using namespace std;

#define MAX(a,b) ((a)>(b) ? (a) : (b))
#define MIN(a,b) ((a)<(b) ? (a) : (b))
#define EPS 1e-7
#define asdf exit(0);


typedef long long LL;








int main()
{
    //freopen("B-small-attempt0.in","r",stdin);
	//freopen("B-small-attempt0.out","w",stdout);

    //freopen("B-small-attempt0.in","r",stdin);
	//freopen("B-small-attempt1.out","w",stdout);


    freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

    //freopen("B-large.in","r",stdin);
	//freopen("B-large1.out","w",stdout);


    int T,cs;
    double C,F,X;

    scanf("%d",&T);
    for(cs=1;cs<=T;cs++)
    {
        printf("Case #%d: ",cs);



        scanf("%lf %lf %lf",&C,&F,&X);


        double coki=0;
        double ans=X/2;
        double time=0;
        double now_freq=2;


        int it;
        for(it=1; time<ans  || fabs(ans-time)<EPS  ;it++)
        {
            double rest=X/now_freq;
            ans=min(ans,time+rest);
            time+=(C/now_freq);
            now_freq+=F;
        }






        printf("%.12lf\n",ans);



    }

    return 0;
}
