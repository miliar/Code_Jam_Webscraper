#include <iostream>
#include <stdio.h>
#include <list>

#define ARRANGEMENT 2
#define ROWS 4
#define COLS 4
#define CARDS 16

using namespace std;

int elementOf( int x, list<int> v );
list<int> sharedElements( list<int> u, list<int> v);

int main(){
    int T;
    cin >> T;

    int ans[2];
    int x;


    for ( int t = 1; t < T+1; ++t ){
        
        list<int> row;
        list<int> col;
           
        cin >> ans[0];
        for ( int i=0; i<CARDS; ++i){
            cin >> x;
            if ( i >= (ans[0]-1)*COLS && i < ans[0]*COLS){
                row.push_back(x);
            }
        }
        
        cin >> ans[1];
        for ( int i=0; i<CARDS; ++i){
            cin >> x;
            if ( i >= (ans[1]-1)*COLS && i < ans[1]*COLS){
                   col.push_back(x);
            }
        }
       
        list<int> shared = sharedElements(row,col);

        cout << "Case #" << t << ": ";
        if ( shared.size()==1 )
            cout << shared.front() << endl;  
        else if ( shared.size()>1 )
            cout << "Bad magician!" << endl;
        else
            cout << "Volunteer cheated!" << endl;
    }
    return 0;
}

list<int> sharedElements( list<int> u, list<int> v){
    list<int> w;

    for ( list<int>::iterator it=u.begin(); it!=u.end(); ++it){
        if ( elementOf(*it, v) ){
            w.push_back(*it);
        }
    }
    return w;
}

int elementOf( int x, list<int> v ){
    for ( list<int>::iterator it = v.begin(); it!=v.end(); ++it){
        if ( x == *it )
        {
            return 1;
        }
    }
    return 0;
}
