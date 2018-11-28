/*
*********************
** @Author lion_IT **
*********************
*/
//------ Library --------
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
//------ Containers -------
#include <vector>
#include <stack>
#include <queue>
#include <map>
//-------------------------
#define For(i,a,b) for(int i = int(a); i <= int(b); i++)
#define Ford(i,b,a) for(int i = int(b); i >= int(a); i--)
#define rep(i,n) for(int i = 0; i < int(n);i++)
#define repd(i,n) for(int i = int(n)-1; i >=0 ;--i)
#define fi first
#define se second
#define mp make_pair
#define pii pair<int, int>
#define VI vector<int>
#define pb push_back
#define PI acos(-1)

#define BUG(a) cout<<a
#define BUG_(a) cout<<a<<endl
typedef long long llint;
struct Point{
    int x, y;
    Point(){
        x = 0, y = 0;
    }
    Point(int _x,int _y){
        x = _x;
        y = _y;
    }
};
using namespace std;


#define IN "B-large.in"
#define OUT "output.txt"
int main(){
    //freopen(IN,"r",stdin);
    //freopen(OUT,"w",stdout);
    int T, loop;
    double C, F, R, tmp, ret;
    scanf("%d\n",&T);
    For(CASE, 1, T){
        scanf("%lf%lf%lf\n",&C,&F,&R);
        loop = int((2*C-F*R)/(C*F))*(-1)-1;
        //cout<<C<<" "<<F<<" "<<R<<" "<<loop<<endl;
        loop = max(0, loop);
        ret = 0;
        rep(i,loop)ret += C/(2+i*F);
        tmp = ret+C/(2+loop*F)+R/(2+(loop+1)*F);
        ret = ret+R/(2+loop*F);
        //cout<<ret<<" "<<tmp<<endl;
        ret = min(ret,tmp);
        printf("Case #%d: %.07lf\n",CASE,ret);
    }
    //----------- Code ----------
    return 0;
}
