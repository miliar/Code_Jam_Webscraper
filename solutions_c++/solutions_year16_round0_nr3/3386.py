#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <stdlib.h>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <numeric>
#include <utility>
#include <deque>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <queue>
#include <limits>
#include <fstream>
#include <list>
#include <sstream>
#include <iostream>
#include <iomanip>
//#include <time.h>
using namespace std;
//#define MAX 1005
#define pii pair<long long , long long>
#define mp make_pair
#define MAX 40
long long pot(long long a,long long b){if(!b)return 1;if(b&1)return a*pot(a*a,b>>1); else return pot(a*a,b>>1);}
long long base[ MAX ];

bool isPrime(long long n)
{
    long long i;
    if( n == 2 )
        return 1;

    if( n % 2 == 0)
        return 0;

    for( i = 3 ; i * i <= n; i += 2 )
        if( n % i == 0 )
            return 0;
    return 1;
}

int main() {
    //srand (time(NULL));
    int t;
    int n,m;
    scanf("%d", &t) ;
    for( int q = 1 ; q <= t && scanf("%d %d" , &n , &m ) ; ++q ){
        printf("Case #%d:\n", q  );

        for( long long i = 0 ; i < 1LL<<n ; ++i ){
            //cout<<i<<endl;
            if( (i & (1LL<<0)) && (i & (1LL<<(n - 1))) ){
                //cout<<i<<endl;
                bool possible = true;
                memset( base , 0 , sizeof( base ));
                for( int j = 0 ; j < n ; ++j ){
                    if( i & (1<<j)){
                        for( int k = 2 ; k <= 10 ; ++k ){
                            base[k] = base[k] + pot(k, j);
                        }
                    }
                }

                for( int j = 2 ; j <= 10 ; ++j ){
                    //cout<<"base "<<j<<" --> "<<base[j]<<endl;
                    if( isPrime( base[j] ) ){
                        possible = false;
                        break;
                    }
                }

                if( possible ){
                    for( int j = n - 1 ; j >= 0 ; --j ){
                        if( i & (1<<j) ){
                            printf("1");
                        }else
                            printf("0");
                    }

                   // printf(" ");

                    for( int j = 2 ; j <= 10 ; ++j ){
                        for( long long k = 2 ; k * k <= base[j] ; ++k  ){
                            if( base[j] % k == 0 ){
                                printf(" %lld" , k );
                                break;
                            }
                        }
                    }
                    printf("\n");
                    m--;
                    if( m == 0 ) goto end;
                }
            }
        }
        end:
        m--;

    }
    return 0 ;
}
