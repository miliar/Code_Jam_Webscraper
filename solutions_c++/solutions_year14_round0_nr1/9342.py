#include <iostream>
#include <set>
using namespace std;

static int SIZE = 16;
static int LINE = 4;

void solve(int caseNb) {
  set<int> line1,line2;
  int i,j,n,tmp,ans = 0;
  cin >> n;
  for (i = 0 ; i < LINE ; i++) {
      for (j = 0 ; j < LINE ; j++) {
          cin >> tmp;
          if (i+1 == n) {
              line1.insert(tmp);
          }
      }
  }
  cin >> n;
  for (i = 0 ; i < LINE ; i++) {
      for (j = 0 ; j < LINE ; j++) {
          cin >> tmp;
          if (i+1 == n && line1.find(tmp) != line1.end()) {
              line2.insert(tmp);
          }
      }
  }
  cout << "Case #" << caseNb << ": ";
  if (line2.size() == 1) {
      cout << *(line2.begin()) << endl;
  } else if (line2.size() == 0) {
      cout << "Volunteer cheated!" << endl;
  } else cout << "Bad magician!" << endl;
    
}

int main()
{
   int i,n;
   cin >> n ;
   for (i = 0; i < n; i++ ) {
       solve(i+1);
   }

   return 0;
}

