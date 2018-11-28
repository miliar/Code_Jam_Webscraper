#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cctype>
using namespace std;

int main(){
 long long int Case(0);
 long long int N;
 cin >> N;
 for (; Case < N; ++Case){
  long long int Smax;
  cin >> Smax;
  long long int tmp;
  long long int sum(0);
  int people_standing(0);
  for (long long int i = 0; i <= Smax; ++i){
   char c;
   cin >> c;
   tmp = c-'0';
   if (people_standing < i){
    sum += i - people_standing;
    people_standing = i;
   }
   people_standing += tmp;
  }
  cout << "Case #" << Case+1 << ": " << sum << endl;
 }
 return 0;
}
