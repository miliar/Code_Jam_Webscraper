#include <iostream>
#include <vector>
using namespace std;

vector<int> seen(10);
int seencount;

void flagdigits(int n) {
    int i = n;
    while (i) {
        if (seen[i%10] == 0) {
     		seen[i%10] = 1;
		seencount++;
 	}
	i /= 10;
    }
}

void newproblem(int c, int n) {
    seencount = 0;
    for (int i = 0; i < 10; i++) {
	seen[i] = 0;
    }

    if (n == 0){
	cout << "Case #" << c << ": " << "INSOMNIA" << endl;
	return;
    }

    int mult = 1;
    int lastn = n;
    while (seencount < 10) {
        lastn = n * mult;
	flagdigits(lastn);
	mult++;
    }
   
    cout << "Case #" << c << ": " << lastn << endl;    
}

void main() {
  int n, t;
  cin >> t;  
  for (int i = 1; i <= t; ++i) {
    cin >> n; 
    newproblem(i, n);    
  }        
}