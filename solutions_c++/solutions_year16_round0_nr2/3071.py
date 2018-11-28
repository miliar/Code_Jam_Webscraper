#include<bits/stdc++.h>
 
using namespace std;

void flip(int st , int en , string& s){
	for(int i = st; i <= en; i++){
		if( s[i] == '+' )	s[i] = '-';
		else 	s[i] = '+';
	}
	int i = st;
	int j = en;
	while(i < j){
		char temp = s[i];
		s[i] = s[j];
		s[j] = temp;
		i++;
		j--;
	}
}
 
int main(){
    #ifndef ONLINE_JUDGE
            freopen("input.txt","r",stdin);  
            freopen("output.txt","w",stdout);
    #endif
    int t;
    cin >> t;
    for(int qq = 1; qq <= t; qq++){
    	string s;
    	cin >> s;
    	char prev = '$';
    	int l = s.length();
    	string s1 = "";
    	for(int i = 0; i < l; i++){
    		if( s[i] == prev ){
    			continue;
    		}
    		s1 += s[i];
    		prev = s[i];
    	}
    	l = s1.length();
    	int ans = 0;
    	for(int i = l-1; i >= 0; i--){
    		if( s1[i] == '+' ){
    			continue;
    		}
    		else{
    			if( s1[0] == '-' ){
    				ans++;
    			}
    			else{
    				ans += 2;
    			}
    			flip(0,i,s1);
    		}
    	}
    	printf("Case #%d: %d\n",qq,ans);
    }
    return 0;
} 