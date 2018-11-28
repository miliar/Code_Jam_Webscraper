/*
Author : Rashedul Hasan Rijul ( Silent_coder ).
*/
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<ctype.h>
#include<algorithm>
#include<vector>
#include<string>
#include<queue>
#include<stack>
#include<map>
#include<set>
using namespace std;

#define maxm 1000
#define inf (1<<29)
#define ii int

#define pi  acos(-1.0)
#define eps 1e-9
#define iseq(a,b) (fabs(a-b)<eps)

#define pii pair<int,int>
#define mp  make_pair
#define uu first
#define vv second

ii on(ii n,ii k){ return (n|(1<<k)); }
ii off(ii n,ii k){ return (n-(n&(1<<k))); }
bool chck(ii n,ii k){ return (n&(1<<k)); }

ii mini(ii a,ii b){ if(a<b) return a;  return b;  }
ii maxi(ii a,ii b){ if(a>b) return a;  return b;  }


int main(){

    int i,j,k,l,test,t=1;

    freopen("in2.in","r",stdin);
    freopen("out1.txt","w",stdout);

    scanf("%d",&test);

    while(test--){

        double C,F,X;

        scanf("%lf %lf %lf",&C,&F,&X);

        double req=0,ans=X/2.0;
        double prev=2.0;
        for(i=1;;i++){
            double ans1= req + C/(prev);
            req=ans1;
            prev+=F;
            ans1+=(X/prev);
            if(ans1<ans){
                ans=ans1;
            }
            else break;
        }
        printf("Case #%d: %.7lf\n",t++,ans);
    }

    return 0;
}

