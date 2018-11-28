#include <iostream>
#include <string>
#include <cmath>
using namespace std;

string s; 
const int MAXN = 4; 
char ch; 
int tests, test, n, m, x, y; 
int a[MAXN][MAXN], b[MAXN][MAXN]; 


int main(){
    freopen("1.in","r",stdin); 
    freopen("1.out","w",stdout);

    scanf("%d\n", &tests);
	string s; 
	
    for (test = 1; test <= tests; ++test){
        getline(cin, s);
        int ans = 0; 
        s = s + "+"; 
		char c = s[0];  
    	for (int i = 1; i < s.length(); ++i) {
    		if (c != s[i]) {
    			++ans;
    			c = s[i]; 
    		}
    	}    
        printf("Case #%d: %d\n", test, ans);    
    }   
     
    return 0;  
}
