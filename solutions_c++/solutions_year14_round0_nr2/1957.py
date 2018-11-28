#include<iostream>
#include<cstdio>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<string>
#include<math.h>
#include<stdlib.h>
#define pb push_back
#define tr(c,i) for(typeof((c).begin() )i = (c).begin(); i != (c).end(); i++)
//typedef pair<int,int> ii;
//typedef vector< vector<pair<int,int> > > dk;
//map<string,int> m;

using namespace std;


int main()
{ freopen("B-large.in", "r", stdin);
    freopen("outsmall0.txt", "w", stdout);
    int tst,i;
    double c,f,x,r,b,nb,t;
    scanf("%d",&i);
    for(tst=1;tst<=i;tst++)
    {
       scanf("%lf%lf%lf",&c,&f,&x);
       r=2; t=0;
       while(1)
       {
           nb=x/r;
           b=c/r;
           if(nb<=b+(x/(r+f)))
           {
               t+=nb;
               break;
           }
           t+=b;
           r+=f;
           //cout<<"t is: "<<t<<"  rate is: "<<r<<"\n";

       }

        printf("Case #%d: %lf\n",tst,t);



    }


    return 0;
}


