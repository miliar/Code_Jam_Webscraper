#include <bits/stdc++.h>
#include "random.h"

using namespace std;


int main () {
	freopen ("file.in", "w", stdout);
	srand (time (NULL));

   	initrand(rand ());

   	cout << "1\n";

   	int n = 10;
   	int m = 20;
   	int k = 5;
                 
    cout << n << " " << m << ' ' << k << endl ;
    cout << "1 2 3 4 5\n";

   	for (int i = 0; i < m; i++) {
   		int a = rand () % n + 1;
   		
   		int b = rand () % n + 1;
   		while (b == a)
   			b = rand () % n + 1;
   			cout << a << ' ' << b << endl;	
   	}
   	
   	return 0;
}