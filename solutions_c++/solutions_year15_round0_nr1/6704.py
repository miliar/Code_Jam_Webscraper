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

int s[1001];
void runCase() {
    printf("Case #%d: ", ++counter);
    
    int maxS;
    scanf("%d ", &maxS);
    for(int i = 0; i <= maxS; ++i)
    {
       scanf("%1d", &s[i]);
    }
    int standing = s[0];
    int invited = 0;
    for(int i = 1; i <= maxS; ++i)
    {
       if(standing < i)
       {
          invited += i - standing;
          standing += i - standing;
       }
       standing += s[i];
    }
    
    printf("%d\n", invited);

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

