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


#define IN "A-small-attempt1.in"
#define OUT "output.txt"
int main(){
    //freopen(IN,"r",stdin);
    //freopen(OUT,"w",stdout);
    int T, r, c, loop, ret, cnt[20];
    memset(cnt, 0, sizeof cnt);
    scanf("%d\n",&T);
    For(CASE,1,T){
        loop = 0;
        rep(LOOP,2){
            scanf("%d\n",&r);
            For(i,1,4){
                For(j,1,4){
                    scanf("%d",&c);
                    if(i==r)
                        if(cnt[c]==CASE)loop++,ret=c;
                            else
                                cnt[c] = CASE;
                }
                scanf("\n");
            }
        }
        //cout<<loop<<" "<<ret<<endl;
        if(loop==1)printf("Case #%d: %d\n",CASE,ret);
            else
                if(loop==0)printf("Case #%d: Volunteer cheated!\n",CASE);
                    else
                        printf("Case #%d: Bad magician!\n", CASE);
    }
    //----------- Code ----------
    return 0;
}
