#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>

using namespace std;

vector<int> getRow ( int rowNum );
vector<int> getIntersection (vector<int> v1, vector<int> v2);

/*************** main ***************/
int main () {
    freopen ( "input.in","r", stdin );
    freopen ( "output.out","w", stdout );
    
    int T, rNum; // rNum is row number
    vector <int> r1;
    vector <int> r2;
    
    cin >> T;
    
    for ( int t=1; t<=T; t++) {
        vector <int> intersec;
        // Read first row number
        cin >> rNum;
        
        // Read first row
        r1 =getRow ( rNum );
        
        // Read second row number
        cin >> rNum;
        
        // Read second row
        r2 = getRow ( rNum );
        
        // Get intersection
        intersec = getIntersection (r1, r2);
        
        // First case: Only one card
        cout << "Case #" << t <<": ";
        if ( intersec.size() == 1 ) {
            cout << intersec[0] << endl;
            continue;
        }
        
        // Second case: More than one card
        if ( intersec.size() > 1 ) {
            cout << "Bad magician!\n";
            continue;
        }
        
        // Third case: Empty
        cout << "Volunteer cheated!\n";
        
    }
    
    fclose ( stdin );
    fclose ( stdout );

    return 0;
}
/*************** ***** ***************/


/*************** getRow ***************/
vector<int> getRow ( int rowNum ) {
    vector<int> ret(4,0);
    int toSkip;
    
    for ( int r=1; r<=4; r++ ) {
    
        if ( r != rowNum ) {
            for ( int i=0; i<4; i++ ) {
                cin >> toSkip;
            }
            continue;
        }
        
        for ( int i=0; i<4; i++ ) {
            cin >> ret[i];
        }
        
    }
    
    return ret;
}
/*************** ***** ***************/

/*************** getIntersection ***************/
vector<int> getIntersection (vector<int> v1, vector<int> v2) {
    vector<int> ret;
    bool finished;
    int ind1=0, ind2=0;
    
    sort ( v1.begin(), v1.end() ); 
    sort ( v2.begin(), v2.end() ); 
    
    finished = ( ind1 == v1.size()) || (ind2 == v2.size() );
    
    while ( !finished ) {
    
        if ( v1[ind1]  == v2[ind2] ) {
            ret.push_back ( v1[ind1] );
            ind1++;
            ind2++;
        }
        
        else if ( v1[ind1]  < v2[ind2] ) {
            ind1++;
        }
        
        else {
            ind2++;
        }
    
    
        finished = ( ind1 == v1.size() ) || ( ind2 == v2.size() );
    }
    
    return ret;
}
/*************** ***** ***************/
