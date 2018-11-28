//problem 1

#include <vector>
#include <iostream>
#include <string>
using namespace std;

int main(){
  
  int n;
  cin >> n;

  int cap;
  string s;
  int total, added;

  for(int i = 1; i <= n; ++i){
	cin >> cap >> s;
	added = 0;
	total = s[0] - '0';
	for(int j = 1; j <= cap; ++j){
		if(j > total){
			added += (j - total);
			total += (j - total);
		}
		total += (s[j] - '0');
	}
	
	cout << "Case #" << i << ": " << added << endl;

  }



  return (0);
}
