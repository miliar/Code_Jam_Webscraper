#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <stdlib.h>
#include <algorithm>

using namespace std;

int main(){
    int t, ans;
    string s;
    cin >> t;
    for(int i = 1; i <= t; i++){
    	ans = 0;
    	cin >> s;
    	int x = s.size() - 1;
    	while(1){
    		int flag = 0;
    		while(x >= 0){
    			if(s[x] == '-')
    				break;
  		  		x--;
    		}
    		if(s[x] == '-'){
    			ans++;
    			for(int j = 0; j <= x; j++){
    				if(s[j] == '+')
    					s[j] = '-';
    				else
    					s[j] = '+';
    			}
    			for(int j = 0; j < s.size(); j++)
    				if(s[j] == '+')
    					flag++;
    			if(flag == s.size())
    				break;
    		}
    		else
    			break;
    	}
    	cout << "Case #" << i << ": " << ans << endl;
    }
	return 0;
}
