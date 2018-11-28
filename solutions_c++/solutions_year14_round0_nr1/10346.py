#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

void isFound( vector <int> temp1, vector <int> temp2, int testCase ) {
     int counter = 0;
     int tempAns = 0;
     //sort(temp1.begin(), temp1.end());
     //sort(temp2.begin(), temp2.end());
     
     for( int i = 0; i < 4; i++ ) {
              for( int j = 0; j < 4; j++ ) {
                  if( temp1[i] == temp2[j] ) {
                      counter++;
                      tempAns = temp1[i];
                  }
              }
     }
     
     if( counter == 1 )
     {
         cout << "Case #" << testCase << ": " << tempAns << endl;
     } else if( counter > 1 ) {
            cout << "Case #" << testCase <<": Bad magician!\n";
     } else {
            cout << "Case #" << testCase << ": Volunteer cheated!\n";
     }

}

int main()
{
    int testCase;
        
    cin >> testCase;
    
    int testCount = 0;
    
    while( testCase-- ) {
           int firstAns;
           int inpMatrics1[4][4];
           int secondAns;
           int inpMatrics2[4][4];
           vector <int> temp1;
           vector <int> temp2;
           
           cin >> firstAns;
           for( int i = 0; i < 4; i++ ) {
                for( int j = 0; j < 4; j++ ) {
                     cin >> inpMatrics1[i][j];
                }
           }
           cin >> secondAns;
           for( int i = 0; i < 4; i++ ) {
                for( int j = 0; j < 4; j++ ) {
                     cin >> inpMatrics2[i][j];
                }
           }
           
           for(int i = 0; i < 4; i++ ) temp1.push_back(inpMatrics1[firstAns-1][i]);
           for(int i = 0; i < 4; i++ ) temp2.push_back(inpMatrics2[secondAns-1][i]);
           
           isFound(temp1, temp2, ++testCount);
    }
//    system("pause");
}
