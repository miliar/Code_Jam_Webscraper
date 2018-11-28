#include <iostream>
#include <cmath>
#include <cstdio>
#include <string>
#include <stack>
#include <queue>
#include <ctime>
#include <algorithm>
#include <deque>
#include <vector>
#include <map>
#include <cstdlib>
#include <fstream>

#define sqr(x)  ((x) * (x))
#define rep(i,n)  for(long long i = 0;i < (n);++i)
#define fill(x,y) memset(x,y,sizeof(x))
#define REP(v,p,k) for(long long v = p;v < k;++v)
#define sz(c) (int)c.size()
#define pb push_back

typedef long long ll; 
typedef unsigned int uint;
typedef long double ld;
typedef unsigned long long ull;
using namespace std;


int main() {
	ios_base::sync_with_stdio(0);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);	
    int tests;
    cin >> tests;
    for(int j = 0;j < tests;++j){
    	int x,r,c;
    	cin >> x >> r >> c;
    	cout << "Case #" << j + 1 << ": ";
    	if(x == 1) cout << "GABRIEL";
    	else if (x == 2){
    		if(r % 2 == 1 && c % 2 == 1){
    			cout << "RICHARD";
    		}
    		else cout << "GABRIEL";
    	}
    	else if (x == 3){
    		if((r * c) % 3 != 0){ cout << "RICHARD"; }
    		else{
				if(r < c) swap(r,c);
				if(r == 3 && c == 1){
					cout << "RICHARD";
				}
				else if(c == 2 && r == 3){
					cout << "GABRIEL";	
				}   			
				else if(c == 3 && r == 3){
					cout << "GABRIEL";
				}
				else if(r == 4 && c == 3){
					cout << "GABRIEL";	
				}
    		}
    	}
    	else if (x == 4){
    		if((r * c) % 4 != 0) {cout << "RICHARD";}
    		else{
    			if(r == 2 && c == 2) cout << "RICHARD";
    			else if(r == 4 && c == 4) cout << "GABRIEL";
    			else if((c == 4 && r == 3) || (c == 3 && r == 4)) cout << "GABRIEL";
    			else cout << "RICHARD";
    		}
    	}
    	cout << "\n";
    }
	return 0;
}