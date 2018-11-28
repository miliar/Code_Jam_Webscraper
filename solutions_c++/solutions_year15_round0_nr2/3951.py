#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>

using namespace std;

struct state {
    vector <int> diner;
    int step;
};

set < vector<int> > s;

int t, n, x, maxu, ans;

void print( vector <int> tmp ) {

    for ( vector <int>::iterator pos = tmp.begin(); pos != tmp.end(); ++pos )
        cout << *pos << " ";
    cout << endl;

}

int main( ) {

    scanf( "%d", &t );
    
    for ( int T = 0; T < t; ++T ) {
        
        scanf( "%d", &n );
        
        state start;
        
        for ( int i = 0; i < n; ++i ) {
            scanf( "%d", &x );
            
            if ( i == 0 ) {
                maxu = x;
            }else {
                maxu = max( maxu, x );
            }
            
            start.diner.push_back( x );
        }
        
        start.step = 0;
        
        queue <state> q;
        
        q.push( start );
        s.clear();
        
        while ( !q.empty() ) {
        
            state top = q.front();
            q.pop();
            
            //cout << "pop" << endl;
            
            //cout << top.step << ", maxu = " << maxu << endl;
            
            ++top.step;
            
            if ( top.step > maxu ) {
                continue;
            }
            
            state tmp = top;
            
            //print( tmp.diner );
            
            int all_zero = tmp.diner.size();
            
            for ( int i = 0; i < tmp.diner.size(); ++i ) {
                --tmp.diner[i];
                if ( tmp.diner[i] == 0 ) {
                    tmp.diner.erase( tmp.diner.begin() + i );
                    //print( tmp.diner );
                    --i;
                    --all_zero;
                }
            }
            
            if ( tmp.diner.size() == 0 ) {
                //printf( "%d FOUND %d\n", T+1, tmp.step );
                ans = tmp.step;
                break;
            }
            
            sort( tmp.diner.begin(), tmp.diner.end() );
            
            if ( s.find( tmp.diner ) == s.end( ) ) {
                s.insert( tmp.diner );
                q.push( tmp );
            }
            
            for ( int i = 0; i < top.diner.size(); ++i ) {
         
                 for ( int j = 1; j < top.diner[i]-1; ++j ) {
                
                    tmp = top;
                    
                    tmp.diner[i] -= j;
                    tmp.diner.push_back( j );
                
                    sort( tmp.diner.begin(), tmp.diner.end() );
                
                    if ( s.find( tmp.diner ) == s.end( ) ) {
                        s.insert( tmp.diner );
                        q.push( tmp );
                    }
            
                }
                
            }
           
        }
        
        printf( "Case #%d: %d\n", T+1, ans );
        
    }

    return 0;

}