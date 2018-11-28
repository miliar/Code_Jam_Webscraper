/* ..abhishek kumar.. */
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
using namespace std;
#define LARGE
int t,cs;
double c,f,x,tmp,r,sm,pt,t1,t2;
int main(){
	#ifdef LARGE
	freopen("B-large.in","rt",stdin);
	freopen("output1.out","wt",stdout);
#endif
#ifdef SMALL
	freopen("B-small-attempt5.in","rt",stdin);
	freopen("output.out","wt",stdout);
#endif
	
	scanf("%d",&t);
    while(t--)
    {
       pt=0;
       sm=0;
       cs++;
       scanf("%lf %lf %lf",&c,&f,&x);
       r=2;
       while(pt!=x)
       {
           tmp=x/r;
           t1=c/r;
           t2=x/(r+f);
           if((t1+t2)<tmp)
           {
              r+=f;
              sm+=t1;
           }
           else
           {
               pt=x;
               sm+=tmp;
           }
       }
       cout<<fixed;
       cout<<"Case #"<<cs<<": "<<setprecision(7)<<sm<<"\n";
    }
	return 0;
}
