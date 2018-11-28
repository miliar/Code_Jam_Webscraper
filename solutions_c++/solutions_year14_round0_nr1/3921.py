#include <iostream>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <map>
#include <stack>
#include <algorithm>
#include <stdlib.h>
#include <fstream>
#include <string>
#include <queue>
#include <sstream>
#include <cassert>
#include <cctype>
#include <climits>


#define FOR(i, n) for(int i=0; i<n; i++)

using namespace std;

/*


3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

*/



int main()
{

int total;
cin >> total;

int cards1[4][4] = {0};
int cards2[4][4] = {0};


FOR(i, total){
    
    int first;
    cin >> first;
    
    
    FOR(j, 4){
        FOR(k, 4){
            
            cin >> cards1[j][k];            
        }        
    }


    vector<int> temp1;
    
    
    FOR(j, 4){
        temp1.push_back(cards1[first-1][j]);        
    }
    
    
    

    int second;
    cin >> second;
    
    
    FOR(j, 4){
        FOR(k, 4){
            cin >> cards2[j][k];            
        }        
    }


    int count = 0;
    
    int num = -1;
    
    FOR(j, 4){

        FOR(k, temp1.size()){
            
            if(cards2[second-1][j] == temp1[k]){
                count++;
                num = temp1[k];
            }
            
        }

    }
    
    
    if(count == 0){
        cout <<"Case #" << i+1 << ": " << "Volunteer cheated!" << endl;
    }
    else if(count > 1){
        cout <<"Case #" << i+1 << ": " << "Bad magician!" << endl;
    }
    else if(count == 1)
    {
        cout <<"Case #" << i+1 << ": " << num << endl;        
    }
    
    
    
}

    
    
    
   
   return 0;
}
