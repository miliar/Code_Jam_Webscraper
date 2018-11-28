#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;
inline bool cmp(int a, int b){
    return a>b ;
}

int main(){
    int tt;
    int d;
    int p[1005];
    int i;
    int count;
    int div[1005];
    int temp;
    /*for(i=0; i<50; ++i){
        div[i]=i*(i+1);
    }*/
    int minu[1005];
    int maxdiv;
    int maxn[1005];
    freopen("in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&tt);
    for(int j=1 ; j<=tt ;++j){
        
        scanf("%d",&d);
        for( i =1 ; i<=d ; ++i){
            scanf("%d",&p[i]);
        }
        sort( p+1 , p+d+1 ,cmp);
        i = 0; 
        /*while( p[1] > div[i]) i++;*/
        maxdiv = p[1] ;
        /*for( i = maxdiv ; i > 0 ; i--){
            minu[i] = (p[1]-1)/i + 1;
            maxn[i] = minu[i];           
        }*/
        for( i = p[1] ; i >0 ; i--){
            minu[i] = i ;
            maxn[i] = i ;
        }
        for( i = 1 ; i<=d ;++i){
            for( int w = maxdiv ; w > 0 ; --w){
                minu[w] += ( p[i] -1 )/maxn[w] ;
                
            }
        }
        int time = p[1];
        for(int i = 1 ; i <= maxdiv ; ++i){
            if( time > minu[i])
                time = minu[i];
        }
        printf("Case #%d: ", j);
        printf("%d\n",time);
        
        
    }
    return 0;
}
