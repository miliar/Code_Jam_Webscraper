#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<stdlib.h>
#include<cmath>
using namespace std;

char s[100];

bool ok( long long v ){
    int sn = 0;
    while( v>0 ){ s[sn++] = v%10; v /= 10; }
    for(int i=0; i<sn; i++) if( s[i]!=s[sn-1-i] ) return false;
    return true;
}

int main(){
    int *is = new int[10000008];
    is[0] = 0;
    for(int i=1; i<=10000000; i++){
        if( ok(i) && ok((long long)i*i) ) is[i]=is[i-1]+1;
        else is[i] = is[i-1];
    }
    int T; long long a, b;
    scanf("%d",&T);
    for(int t=1; t<=T; t++){
        scanf("%lld%lld",&a,&b);
        long long aq = (int)sqrt(a+0.5), bq = (int)sqrt(b+0.5);
        if( (aq-1)*(aq-1)>=a ) aq -= 1;
        else if( aq*aq<a ) aq += 1;
        
        if( (bq-1)*(bq-1)>=b ) bq -= 1;
        //else if( (bq*bq<b ) bq += 1;

        //printf("%lld %lld %d %d\n",aq,bq,is[bq],is[aq-1]);
        printf("Case #%d: %d\n",t,is[bq]-is[aq-1]);
    }
    delete []is;
    return 0;
}

