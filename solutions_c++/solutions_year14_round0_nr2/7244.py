#include<cstdio>
#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#include<cstring>
#include<cstdlib>
#include<map>
#include<set>

using namespace std;

#define REP(i,a,b) for(int i=(a);i<=(b);i++)
#define INF 2100000000
typedef long long int ll;
typedef vector<int> vi;
typedef pair<int,int> ii;

int main(){
    //freopen("input.in","r",stdin);
    //freopen("output.txt","w",stdout);
    int tc;
    double C,F,X,last,tmp,now,P,minim;
    scanf("%d",&tc);
    REP(tnc,1,tc){
        P=2;
        minim = 2100000000;
        printf("Case #%d: ",tnc);
        scanf("%lf%lf%lf",&C,&F,&X);
        tmp=INF;
        now=-1;
        last=0;
        do{
            if(now>-1)
                tmp = now;
            now = last + X / P;
            if(now<minim)
                minim = now;
            last+=C/P;
            P+=F;
        }while(tmp>now);
        printf("%.7lf\n",minim);
    }
    return 0;
}
