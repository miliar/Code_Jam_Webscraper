#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <functional>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <stdio.h>
#include <string.h>
using namespace std;

int A, B, K;

void solve() {
	cin >> A >> B >> K;
	
    int cont = 0;
    for (int m=0; m<K; m++){
	    for (int i=0; i<A; i++){
	    	for (int j=0; j<B; j++){
	    		int x = i & j;	    		
			    if (x == m){			    
	    		  cont++;
	    		}
	    	}		
	    }    	
    }    
    cout << cont << endl;
}

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas=1; cas<=T ;cas++) {
        printf("Case #%d: ", cas);
        solve();
    }
}
