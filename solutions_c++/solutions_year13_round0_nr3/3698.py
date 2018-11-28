#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>
#include <functional>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <cassert>
#include <map>
#include <deque>
#include <queue>
#include <set>
#include <stack>

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef pair<int,ii> iii;
typedef unsigned long long uint;

#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define MAX_DISTANCE (300000)

inline int is_palindrome(uint orig) {
    uint reversed = 0, n = orig;
    
    while (n > 0) {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }
    
    return (orig == reversed);
}

int main(void) {
	
	int x, y, z;
	int numCases;
	unsigned int i, j, k;
	
	scanf("%d", &numCases);
	for (int T = 1; T <= numCases; T++) {
		uint A, B;
        scanf("%lld %lld", &A, &B);
        
        uint sqrtA = (uint) sqrt(A);
        uint sqrtB = (uint) sqrt(B);
        uint count = 0;
        for (int x = sqrtA; x <= sqrtB; x++) {
            if (is_palindrome(x)) {
                uint x2 = x*x;
                if (is_palindrome(x2) && x2 >= A && x2 <= B) {
                    //cout << "palidrome " << x << endl;
                    count += 1;
                }
            }
        }
        
        printf("Case #%d: %lld\n", T, count);
	}

	return 0;
}