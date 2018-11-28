#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
void solveFrac(int k, int c){
	
	for(int i=1;i<=k;i++)	
		cout<<" "<<i;
	cout<<endl;
}


int main() {
	int t, k, c, s;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
      cin >> k >> c >> s;

    cout << "Case #" << i << ":" ;
    solveFrac(k,c);
    
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }

}
