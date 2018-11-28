#include <iostream>
#include <string>
#include <cmath>
using namespace std;

string s; 
const int MAXN = 4; 
char ch; 
int tests, test, n, res;
double C, F, X; 

bool appear[10]; 

int main(){
    freopen("2.in","r",stdin); 
    freopen("2.out","w",stdout);

    scanf("%d", &tests);
    
    for (test = 1; test <= tests; ++test){
    	int n; 
        scanf("%d", &n); 
        
        if (n == 0) {
        	printf("Case #%d: INSOMNIA\n");
        	continue; 
        }
        
        for (int i = 0; i < 10; ++i) appear[i] = false; 
        
        int ans = 0; 
        int cnt = 0; 
        
        while (true) {
        	++ans; 
        	int x = n * ans; 
        	res = x; 
        	// cout << x << "\t";
			while (x != 0) {
        		int y = x % 10; 
        		appear[y] = true; 
				x /= 10; 
        	}
        	bool allAppear = true; 
        	for (int i = 0; i < 10; ++i) if (!appear[i]) {
        		allAppear = false; 
        		break; 
        	}
        	if (allAppear) {
        		break; 
        	} 
        	//for (int i = 0; i < 10; ++i) cout << appear[i]; cout << endl; 
        }
        
        printf("Case #%d: %d\n", test, res);    
    }   
     
    return 0;  
}
