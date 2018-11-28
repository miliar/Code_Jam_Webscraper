#include <iostream>
#include <set>

using namespace std;

int main() {
  int numProb;
  cin >> numProb;

  for (int i = 0; i < numProb; i++ ) {
    int firstRow;
    cin >> firstRow;
    set<int> myset;
    int temp;
    for ( int j = 0; j < 4; j++) { 
      for ( int k = 0; k < 4; k++) {
        cin >> temp;
        if ( j == firstRow-1 ) { 
          myset.insert(temp);
        }
      }
    }

    int secondRow;
    cin >> secondRow;

    int numIntersection = 0;
    int someIntersect = 0;
    for ( int j = 0; j < 4; j++) { 
      for ( int k = 0; k < 4; k++) {
        cin >> temp;
        if ( j == secondRow-1 ) { 
          if ( myset.find(temp) != myset.end() ) {
            someIntersect = temp;
            numIntersection++;
          }
        }
      }
    }
    

    cout << "Case #" << i+1 << ": ";
    if ( numIntersection == 0 ) {
      cout << "Volunteer cheated!\n";
    }
    else if ( numIntersection == 1 ) {
      cout << someIntersect << endl;
    }
    else {
      cout << "Bad magician!\n";
    }

  }
}
