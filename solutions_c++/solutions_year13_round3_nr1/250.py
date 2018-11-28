#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;

const int SIZE = 1000001;
char s[SIZE];

bool good(char c){
    return (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u');
}

int main(){
	freopen("A-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
    
	int T;
	scanf("%d", &T);
    
	for (int t = 0; t < T; t++){
		scanf("%s", s);
        
        int slen = (int)strlen(s);
        
        int n;
        scanf("%d", &n);
        
        long long cnt = 0;
        
        int j = 0;
        for (int i = 0; i < slen; i++){
            int len = min(j - i, n);
            
            while (j < slen && len < n){
                if (good(s[j])){
                    len++;
                }
                else{
                    len = 0;
                }
                j++;
            }
            
            if (len == n){
                cnt += slen - j + 1;
            }
            else{
                break;
            }
        }
        
		cout << "Case #" << t + 1 << ": ";
		
		cout << cnt << endl;
	}
}
