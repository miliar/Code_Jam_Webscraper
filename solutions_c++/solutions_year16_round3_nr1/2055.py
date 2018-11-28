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
#define MAX 1005
#define pii pair<int , int>
#define mp make_pair
#define pb push_back

bool check( priority_queue<pii> Q ){
    vector<pii> a;
    int sum = 0;
    while( !Q.empty() ){
        pii p = Q.top(); Q.pop();
        a.pb( p );
        sum += p.first;
    }

    for( int i = 0 ; i < a.size() ; ++i ){
        if( a[i].first > sum/2.0 )
            return false;
    }
    return true;
}

int main() {
    //srand (time(NULL));
    int t, n, x;
    scanf("%d", &t) ;
    //vector<pii> a;
    priority_queue< pii > Q;
    vector<int> a, aux;
    for( int q = 1 ; q <= t && scanf("%d" , &n ) ; ++q ){
        //a = vector<pii>(n , 0);
        while( !Q.empty() ) Q.pop();
        //Q.clear();
        //for( int i = 0 ; i < n && scanf("%d" , &a[i].first) ; ++i ){
        int sum = 0;
        //a.clear();
        for( int i = 0 ; i < n && scanf("%d" , &x) ; ++i ){
            //a.pb( x );
            //a[i].second = i;
            sum += x;
            Q.push( mp( x , i ));
        }

        //sort( a.rbegin(), a.rend() );
        printf("Case #%d:", q  );
        while( !Q.empty() ){
            /*if( !check(Q)){
                cout<<"wrong"<<endl;
                break;
            }*/
            pii p = Q.top(); Q.pop();
            //cout<<p.first<<" "<<p.second<<" "<<Q.size()<<endl;
            if(p.first == 1 && Q.size() > 1 ){
                if( p.first - 1 > 0 )
                    Q.push( mp( p.first - 1 , p.second ) );
                printf(" %c", p.second + 'A');
            }else if( !Q.empty() ){
                pii p2 = Q.top(); Q.pop();

                if( p.first - 1 > 0 ){
                    Q.push( mp( p.first - 1 , p.second ) );
                }

                if( p2.first - 1 > 0 ){
                    Q.push( mp( p2.first - 1 , p2.second ) );
                }
                printf(" %c%c", p.second + 'A', p2.second + 'A');
            }else{
                if( p.first - 1 > 0 )
                    Q.push( mp( p.first - 1 , p.second ) );
                printf(" %c", p.second + 'A');
            }
        }
        printf("\n");

    }
    return 0 ;
}
