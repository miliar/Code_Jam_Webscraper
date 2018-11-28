#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

const int Maxn=10000;
const int p[4]={10,100,1000,10000};

typedef long long LL;

int n=0;
LL a[Maxn];

int tt[16];
bool isPali(LL num) {
    int k = 0;
    while ( num>0 ) {
        tt[k++] = num%10;
        num /= 10;
    }
    for ( int i=0;i<k/2;i++ ) {
        if ( tt[i]!=tt[k-1-i] )
            return false;
    }
    return true;
}

int t[4];
void getPali(int num) {
    int temp = num;
    int k = 0;
    memset(t,0,sizeof(t));
    while ( temp>0 ) {
        t[k++] = temp%10;
        temp /= 10;
    }
    LL powt;
    for ( int mid=k-1;mid<4;mid++ ) {
        temp = 0;
        for ( int i=0;i<mid;i++ ) {
            temp = temp*10+t[i];
        }
        temp = temp*p[mid]+num;
        powt = (LL)temp*(LL)temp;
        if ( isPali(powt) ) {
            a[n++] = powt;
            //printf("%d %lld\n",temp,powt);
        }
        temp = 0;
        for ( int i=0;i<=mid;i++ ) {
            temp = temp*10+t[i];
        }
        temp = temp*p[mid]+num;
        powt = (LL)temp*(LL)temp;
        if ( isPali(powt) ) {
            a[n++] = powt;
            //printf("%d %lld\n",temp,powt);
        }
    }
}

int main() {
    //freopen("C-large-1.in","r",stdin);
    //freopen("C-large-1.out","w",stdout);
    for ( int i=0;i<1000;i++ ) {
        for ( int j=1;j<10;j++ ) {
            getPali(i*10+j);
        }
    }
    sort(a,a+n);
    //printf("%d\n",n);
    //for ( int i=0;i<n;i++ ) printf("%lld\n",a[i]);
    int T;
    scanf("%d",&T);
    for ( int Ti=1;Ti<=T;Ti++ ) {
        LL A,B;
        scanf("%lld %lld",&A,&B);
        int k1 = 0;
        while ( a[k1]<A )
            k1++;
        int k2 = n-1;
        while ( a[k2]>B )
            k2--;
        printf("Case #%d: %d\n",Ti,k2-k1+1);
    }
    return 0;
}
