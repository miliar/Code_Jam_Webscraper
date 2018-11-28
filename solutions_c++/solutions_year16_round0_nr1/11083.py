#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

unsigned long long int getSleep(unsigned long long int input){
	// store digits found as true else false
	int map[11]={0};
	unsigned long long int _output = input, output = 0;
	int i = 0, rem = 0, counter = 1;
	
	if (0 == input)
	   return 0;
       
	while(1){
	  output = _output * counter;
	  while(0 != output){
	    	rem = output % 10;
		map[rem] = 1;
		output /= 10;
	  }       


	  for(i = 0; i < 10; i++){
	    if(1 != map[i])
		break;
	  }

	  if( i >= 10 )
	    return counter*_output;

	  counter++;
	}
}

int main() {
  int t;
  unsigned long long int n, m;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
//  cout << t;
  for (int i = 1; i <= t; ++i) {
    cin >> n ;  // read number
    m = getSleep(n);
    if (0 == m)
      cout << "Case #" << i << ": " << "INSOMNIA" << endl;
    else
      cout << "Case #" << i << ": " << m << endl;
 //   cout << n;
  }
  return 0;
}
