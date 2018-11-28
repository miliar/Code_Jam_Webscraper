#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <bitset>
#include <cmath>
#include <numeric>
#include <iterator>
#include <iostream>
#include <cstdlib>
#include <functional>
#include <queue>
#include <stack>
#include <list>
using namespace std;

int T,N;
int bb[4];
int cc[4];
char str[22];

int getAns() {
    int res = 0;
    for(int i = 0 ; i  <N ; i++ ) {
        res += __builtin_popcount(cc[i]) - __builtin_popcount(bb[i]);
    }
    return res;
}

bool ok() {
    int mask = 0;
    for(int i = 0 ; i < N; i++ ) {
        mask |= cc[i];
    }
    for(int i = 0 ; i < N ; i++ ) {
        if( (bb[i]&cc[i]) != bb[i] ) return false;
        if(cc[i] == 0 ) return false;
    }
    if( mask != ((1<<N)-1) ) return false;
    for(int i = 0 ; i < N ; i++ ) {
        for(int j = i ; j < N ; j++ ) {
            if( cc[i] & cc[j] ) {
                if(cc[i] != cc[j] ) return false;
            }
        }
    }
    int a[10];
    for(int i = 0 ; i < N ;i++) a[i] = i;
    do{
        bool flag = true;
        for(int i = 0 ; i < N ; i++ ) {
            if( !((cc[i] >> a[i])&1) ) flag = false;
        }
        if(flag) return true;
    }while( next_permutation(a,a+N) );
    return false;
}

int main() {
    scanf("%d",&T);
    int cases = 1;
    while( T-- ) {
        scanf("%d",&N);
        memset(bb,0,sizeof(bb));
        for(int i = 0 ; i < N ; i++ ){
            scanf("%s",str);
            for(int j = 0 ; j<N ; j++ ) {
                if(str[j] == '1' ) {
                    bb[i] |= (1<<j);
                }
            }
        }
        int ans = 99999;
        for(int i = 0 ; i < (1<<N); i++ ) {
            for(int j = 0 ; j < (1<<N) ; j++ ) {
                for(int k = 0 ; k < (1<<N); k++ ) {
                    for(int l = 0 ; l < (1<<N) ; l++ ) {
                        cc[0] = i; cc[1] = j ; cc[2] = k; cc[3] = l;
                        if( ok() ) {
                            ans = min(ans,getAns());
                        }
                    }
                }
            }
        }
        printf("Case #%d: %d\n",cases++,ans);
        
    }
    return 0;
}