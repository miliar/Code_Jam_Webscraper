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
#define F(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)
#define S(n) scanf("%d",&n)
using namespace std;
#define LARGE
int t,cs;
double c,f,x,tmp,r,sm,pt,t1,t2;
int main(){
	#ifdef LARGE
	freopen("D-large.in","rt",stdin);
	freopen("output1.out","wt",stdout);
#endif
#ifdef SMALL
	freopen("D-small-attempt0.in","rt",stdin);
	freopen("output.out","wt",stdout);
#endif
	double ken[2000],naomi[2000];
	int t,i,j,n,k;
	S(t);
	F1(k,t) {
        cin>>n;
        F(i,n)
            cin>>naomi[i];
        F(i,n)
            cin>>ken[i];
        sort(naomi,naomi+n);
        sort(ken,ken+n);
        int d_war=0,war=0;
        i=0,j=0;
        while(i<n&&j<n) {
            if(naomi[i]>ken[j]) {
                d_war++;
                i++;
                j++;
            }
            else
                i++;
        }
        i=0,j=0;
        while(i<n&&j<n) {
            if(naomi[i]<ken[j]) {
                war++;
                i++;
                j++;
            }
            else
                j++;
        }
        printf("Case #%d: %d %d\n",k,d_war,n-war);
    }
	return 0;
}
