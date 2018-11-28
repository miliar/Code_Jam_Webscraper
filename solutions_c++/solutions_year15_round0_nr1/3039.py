#include <iostream>

using namespace std;

int main() {
  int t; cin >> t;
  for (int ti = 1; ti <= t; ti++){
	  long result = 0;
	  long maxs; cin >> maxs;
	  long standing = 0;
	  char tmp;
	  cin >> tmp; standing = tmp - '0';
	  for (long si = 1; si <=maxs; si++){
		  cin >> tmp;
		  int tmpi = tmp - '0';
		  if (standing < si){
			  result += si - standing;
		  }
		  standing = max (standing, si) + tmpi;
	  }
	  printf ("Case #%d: %ld\n", ti, result); 
  }
}
