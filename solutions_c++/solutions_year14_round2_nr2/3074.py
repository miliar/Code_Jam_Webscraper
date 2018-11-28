#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

#define D(x) cout << #x " is " << x << endl
#define ll long long

using namespace std;

int main(){
    int cases; cin >> cases;
    for(int d=1; d<=cases; d++){
        int a,b,k; cin >> a>>b>>k;
        ll ans=0;
        for(int i=0; i<max(a,b); i++){
            for(int j=0; j<min(a,b); j++){
                if((i&j)<k)ans++;   
            }   
        }
        printf("Case #%d: %d\n",d, ans);  
    }

	return 0;
}
