#include<bits/stdc++.h>

using namespace std;

void ulta(int st , int en , string& str){
	for(int i = st; i <= en; i++){
		if( str[i] == '+' )	str[i] = '-';
		else 	str[i] = '+';
	}
	int i = st;
	int j = en;
	while(i < j){
		char temp = str[i];
		str[i] = str[j];
		str[j] = temp;
		i++;
		j--;
	}
}

int main(){
    #ifndef ONLINE_JUDGE
            freopen("B-small-attempt0.in","r",stdin);
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
    			ulta(0,i,s1);
    		}
    	}
    	printf("Case #%d: %d\n",qq,ans);
    }
    return 0;
}
