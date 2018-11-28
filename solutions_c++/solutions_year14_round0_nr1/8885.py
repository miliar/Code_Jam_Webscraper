#include <iostream>
#include <string>
#include <sstream>

using namespace std;


string intToString(int i)
{
    stringstream ss;
    string s;
    ss << i;
    s = ss.str();

    return s;
}

int intersect_rows( int* row1, int* row2 , int length){
  int result = 0;

  for(int i = 0; i < length; i++ ){
    for( int j = 0; j < length; j++ ){
      if(row1[i] == row2[j]){
          if(result > 0)
              return -1;
          result = row1[i];
      }
    }
  }

  return result;  
}

string process_testcase() {
  int n1;
  int arrangement1[4][4];
  cin >> n1;
  for(int i = 0; i < 4; i++)
    for(int j = 0; j < 4; j++)
      cin >> arrangement1[i][j];

  int n2;
  int arrangement2[4][4];
  cin >> n2;
  for(int i = 0; i < 4; i++)
    for(int j = 0; j < 4; j++)
      cin >> arrangement2[i][j];

  int diff = intersect_rows(arrangement1[n1 - 1], arrangement2[n2 - 1], 4);

  if( diff < 0 )
    return "Bad magician!";
  
  if( diff == 0 )
    return "Volunteer cheated!";
  
  return intToString(diff);
}


int main( int argc, char* argv[] ) {
  int T;
  cin >> T;
  for(int i = 1; i <= T; i++)
    cout << "Case #" << i << ": " << process_testcase() << endl;

  return 0;
}