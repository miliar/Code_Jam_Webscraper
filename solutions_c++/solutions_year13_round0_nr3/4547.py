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

int t, a, b, cnt;
int d[10000];

bool check ( int n )
{
    int ds[100];
    int len = 0;
    while ( n )
    {
        ds[++len] = n%10;
        n/=10;
    }
    for (int i=1; i<=len/2; i++) if ( ds[i]!=ds[len-i+1] ) return false;
    return true;
}

void ini(){
    cnt = 0;
    int i = 1;
    while ( i <= 31 ) {
        int k = i*i;
        //cout << k << endl;
        if ( check(i) && check ( k ) ) {
            d[++cnt]=k;
//            cout << "k "<< k << endl;
        }
        i++;
    }
}

int b1 ( int a ) {
    int lf = 1, rg = cnt;
    int mid;
    int kq=-1;
    while ( lf <=rg ) {
        mid = ( lf + rg ) /2;
        if ( d[mid] >= a )  {
            kq = mid;
            rg = mid -1;
        } else lf = mid + 1;
    }
    return kq;
}

int b2 ( int a ) {
    int lf = 1, rg = cnt;
    int mid;
    int kq=-1;
    while ( lf <=rg ) {
        mid = ( lf + rg ) /2;
        if ( d[mid] <= a )  {
            kq = mid;
            lf = mid +1;
        } else rg = mid - 1;
    }
    return kq;
}

int xuly(int a, int b){
    int i = b1 ( a );
    int j = b2 ( b );
    if ( i == -1 || j == -1 ) return 0;
    return ( j - i + 1 );
}

int main ()
{
    //freopen("test.inp","r",stdin);
    //freopen("test.out","w",stdout);
    scanf("%d",&t);    
    ini();
    for (int o=1; o<=t; o++){
        scanf("%d %d",&a,&b);
        printf("Case #%d: %d\n",o,xuly(a,b));
    }
    return 0;
}
