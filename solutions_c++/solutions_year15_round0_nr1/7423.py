
#include <stdlib.h>
#include <string.h>

#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char ** argv) {
  int n;
  cin >> n;

  for(int z = 0; z < n; z++){
    int len, sum, people;
    string list;
    cin >> len >> list;
    sum = 0;
    people = 0;
    for(int i = 0; i <= len; i++) {
      int k = list[i] - '0';
      if(k != 0) {
	if (sum + people < i) 
	  people += i - sum - people;
	sum += k;
      }
    }
    cout << "Case #" << z+1 << ": " << people << endl;
  }

  return EXIT_SUCCESS;
}
