#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <cstdio>
#include <deque>
#include <queue>
#include <set>
#include <stack>
#include <algorithm>
#include <cmath>
#include <utility>
#include <map>
#define inf 1000111222
#define ss second
#define chen insert
#define xoa erase
#define ff first
#define ii pair <int,int>

using namespace std;

int md[100], mc[100];
int sl, t;
int a,b;
int d[100][100];
int s[100][100];

bool xuly()
{    
    for ( int i=1; i<=a; i++){
        md[i]=0;
        for (int j=1; j<=b; j++) md[i]=max(md[i],s[i][j]);
    }
    
    for ( int i=1; i<=b; i++){
        mc[i]=0;
        for (int j=1; j<=a; j++) mc[i]=max(mc[i],s[j][i]);
    }
    
    for (int i=1; i<=a; i++)
        for (int j=1; j<=b; j++) d[i][j]= min( d[i][j], md[i]);
    for (int i=1; i<=b; i++)
        for (int j=1; j<=a; j++) d[j][i]= min( d[j][i], mc[i]);
    for (int i=1; i<=a; i++)
        for ( int j=1; j<=b; j++) if ( d[i][j] != s[i][j] ) return false;
    
    return true;
}

int main ()
{
    //freopen("test.inp","r",stdin);
    //freopen("test1.out","w",stdout);
    scanf("%d",&t);
    for (int o=1; o<=t; o++){
        scanf("%d %d",&a,&b);        
        for (int i=1; i<=a; i++)
            for (int j=1; j<=b; j++) {
                scanf("%d",&s[i][j]);
                d[i][j]=100;
            }
        if (xuly())
            printf("Case #%d: YES\n", o);
        else printf("Case #%d: NO\n", o);
    }
    return 0;
}
