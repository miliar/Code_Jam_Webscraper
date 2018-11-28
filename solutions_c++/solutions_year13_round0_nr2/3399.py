/*******************************************************************
** AUTHOR   : Wenzheng jiang
** EMAIL    : jwzh.hi@gmail.com 
** OS       : ArchLinux 
** EDITER   : VIM
******************************************************************/
#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
using namespace std;

#define pf(x) printf("%d\n",x)
#define pf2(x,y) printf("%d %d\n",x,y)
#define pf3(x,y,z) printf("%d %d %d\n",x,y,z)
#define pf4(x,y,z,k)printf("%d %d %d %d\n",x,y,z,k)
#define sf(x) scanf("%d",&x)
#define sf2(x,y) scanf("%d%d",&x,&y)
#define sf3(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define sf4(x,y,z,k) scanf("%d%d%d%d",&x,&y,&z,&k)
typedef long long ll;
double const eps = 1e-6;
const int inf = 0x3fffffff;
const int size = 100000 + 5;
int n,m;
int a[200][200];
bool check(int x,int y)
{
    int cnt = 0;
    for(int i = 0; i < n; i++)
        if(a[i][y] > a[x][y]) {
            cnt++;
            break;
        }
    for(int j = 0; j < m; j++)
        if(a[x][j] > a[x][y]){
            cnt++;
            break;
        }
    if(cnt == 2) return false;
    else return true;
}
bool estimate()
{
    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            if(!check(i,j)) return false;
    return true;
}
int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int t,ncase = 0;
    sf(t);
    while(t--){
        sf2(n,m);        
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
                sf(a[i][j]);
        printf("Case #%d: ",++ncase);
        if(estimate()) 
            puts("YES");
        else 
            puts("NO");
    }
}

