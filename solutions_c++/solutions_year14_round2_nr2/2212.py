#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <list>
#include <set>
#include <numeric>
#include <queue>
#include <stack>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
using namespace std;

int counter = 0;

void runCase() {
    printf("Case #%d: ", ++counter);
    long int a, b, k; scanf("%ld %ld %ld", &a, &b, &k);
    
    int answer = 0;
    for(int i = 0; i < a; ++i) {
       for(int j = 0; j < b; ++j)
       {
          if((i&j) < k) {
             answer++;
          }
       }
    }
    
    printf("%d\n", answer);

    return;
}

void preprocess() {
   
}

int main() {
   preprocess();
    int t; scanf("%d", &t);
    while(t--) {
        runCase();
    }
    return 0;
}

/*
    string s;
    getline(cin, s);
    for(int i = 0; i < s.length(); i++) {
    	char c = s.at(i);

//  n, m, 2 numbers per line
//    int n, m; scanf("%d %d", &n, &m);


// GRID - N x M  
int n, m; scanf("%d %d", &n, &m);
 for (int i=0; i<n; ++i) {
     for (int j=0; j<m; ++j) {
         scanf("%d", &t[i][j]);
     }
 }


#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <list>
#include <set>
#include <numeric>
#include <queue>
#include <stack>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
*/

