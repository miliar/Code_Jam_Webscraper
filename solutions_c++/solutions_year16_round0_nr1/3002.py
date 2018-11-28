#include<bits/stdc++.h>
#define ull  unsigned long long
 
using namespace std;

bool mark[12];

bool doneWith(){
	int c = 0;
	for(int i = 0;i < 10; i++){
		if( mark[i] )	c++;
	}
	if( c == 10 )
		return true;
	return false;
}
 
int main(){
    #ifndef ONLINE_JUDGE
            freopen("input.txt","r",stdin);  
            freopen("output.txt","w",stdout);
    #endif
    int t;
    cin >> t;
    for(int qq = 1; qq <= t; qq++){
    	ull n;
    	cin >> n;
    	for(int i = 0; i < 10; i++){
    		mark[i] = false;
    	}
    	if( n == 0 ){
    		printf("Case #%d: INSOMNIA\n",qq);
    		continue;
    	}
    	ull ans = n;
    	ull cnt = 1;
    	ull cur;
    	while(1){
    		cur = ans*cnt;
    		while(cur){
    			mark[cur%10] = true;
    			cur/=10;
    		}
    		if( doneWith() )	break;
    		cnt++;
    	}
    	printf("Case #%d: %llu\n",qq,n*cnt);
    }
    return 0;
} 