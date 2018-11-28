#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

vector<double> v1,v2;
int n ;

    int war_score(){
        set<double> data;
        int score = 0 ;
        for (int i = 0 ; i < n ; ++i )
            data.insert( v2[i] );
        for ( int i = 0 ; i < n ; ++i ){
            set<double> :: iterator it = data.lower_bound( v1[i] );
            if ( it == data.end() ){
                ++score;
                data.erase( data.begin() );
            }else
                data.erase( it );
        }
        return score;
    }
    int deceive_war_score(){
        set<double> data;
        int score = 0 ;
        for (int i = 0 ; i < n ; ++i )
            data.insert( v1[i] );
        for ( int i = 0 ; i < n ; ++i ){
            set<double> :: iterator it = data.lower_bound( v2[i] );
            if ( it!= data.end() ){
                data.erase( it );
                ++score;
            }else
                data.erase( data.begin() );
        }
        return score;
    }
    int work (){
        v1.clear();
        v2.clear();
        scanf("%d",&n);
        for (int i = 0 ; i < n ; ++i ){
            double a ;
            scanf("%lf",&a);
            v1.push_back(a);
        }
        for (int i = 0 ; i < n ; ++i ){
            double a ;
            scanf("%lf",&a);
            v2.push_back(a);
        }
        sort(v1.begin(),v1.end());
        sort(v2.begin(),v2.end());
        /*
        for (int i = 0 ; i < n ; ++i )
            cerr<<v1[i]<<' ';
        cerr<<endl;
        for (int i = 0 ; i < n ; ++i )
            cerr<<v2[i]<<' ';
        cerr<<endl;*/
        printf("%d %d\n",deceive_war_score(),war_score());
    }
    int main(){
        int t ;
        scanf("%d",&t);
        for ( int i = 0 ; i < t;  ++i ){
            printf("Case #%d: ",i+1);
            work();
        }
    }
