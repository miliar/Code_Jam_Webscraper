#include <cstdio>
#include <cmath>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

double getTimeTaken( double C, double F, double X ) {
  double timeTaken = 0;
  double prev = 2;
  while ( X / prev > ( C / prev + X / (prev + F) ) ) {
    timeTaken += C / prev;
    prev += F;
  }
  return timeTaken + X / prev;
}

int canDoMagic( int r1[], int r2[] ) {
  vector<int> v1(4);
  vector<int>::iterator it;

  sort(r1, r1 + 4);
  sort(r2, r2 + 4);
  it = set_intersection(r1, r1 + 4, r2, r2 + 4, v1.begin());
  if (it - v1.begin() == 1)
    return v1[0];
  if (it - v1.begin() > 1)
    return -1;
  return 0;
}

void readInput( int row[]) {
  int id;
  cin >> id;
  id = id - 1;
  int temp;
  for (int i = 0; i < 4; i++ ) {
    for (int j = 0; j < 4; j++ ) {
      cin >> temp;
      if (id == i)
	row[j] = temp;
    }
  }
  return ;
}
int main() {
  int T;
  
  cin >> T;
  int row1[4], row2[4];
  for (int i = 0; i < T; i++) {
    readInput( row1 );
    readInput( row2 );    
    int ans = canDoMagic( row1, row2 );
    cout << "Case #" << ( i + 1 ) << ": ";
    if (ans < 0)
      cout << "Bad magician!";
    else if (ans == 0)
      cout << "Volunteer cheated!";
    else cout << ans;
    cout << endl;
    
  }
}
