#include<bits/stdc++.h>

using namespace std;

#define endl '\n'
#define rep(i , n) for( int i = 0; i < (n); i++ )

typedef long long ll;
typedef pair<int, int> pii;


char s[20];
char cpy[20];
int n;

void change(char & c){
	if(c == '+')c = '-';
	else c = '+';
}

int solve(){
		
	
	int res = 1e9;
	
	for( int mask = 0; mask < (1 << n); mask++ ){
		
		for( int i = 0; i < n; i++ ){
			cpy[i] = s[i];
		}
		
		for( int i = 0;  i < n; i++ ){
			if( mask & (1 << i)){
				reverse(cpy , cpy + i + 1);
				for( int j = 0; j <= i; j++ ){
					change(cpy[j]);
				}				
			}
		}
		
		bool flag = true;
		for( int i = 0;  i < n; i++ ){
			if(flag &= (cpy[i] == '+'));
		}
		if(flag){			
			res = min(res , __builtin_popcount(mask));
		}
	}
	return res;
	
}

int main(){

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	int tc;
	cin >> tc;
	for(int cc = 1; cc <= tc; cc++ ){
		cout << "Case #" << cc << ": ";
		cin >> s;
		n = strlen(s);
		cout << solve() << endl;
	}
}
