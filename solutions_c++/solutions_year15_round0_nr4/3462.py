#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

int T,R,C,X;

int main(){
	
	
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> T;
	
	for(int t = 1; t <= T; ++t){
		
		cin >> X >> R >> C;
		if(R > C) swap(R,C);
		int ans = 0;
		if(X == 1){ ans = 1; }
		
		if( X == 2){
			if(R == 1){
				if( C == 2 || C == 4)
					ans = 1;
				else ans = 2;
			}
			
			if(R == 2)
				ans = 1;
				
			if(R == 3){
				if(C == 4)
					ans = 1;
				else ans = 2;
			}
			
			if(R == 4)
				ans = 1;
			
			
		}
		
		if(X == 3){
			ans = 2;
			if(R == 3 && C == 4)
				ans = 1;
			if(R == 2 && C == 3)
				ans = 1;
			if(R == 3 && C == 3)
				ans = 1;
		}
		
		if(X == 4){
			ans = 2;
			if( R == 4 && C == 4)
				ans = 1;
			if( R == 3 && C == 4)
				ans = 1;	
		}
		
			
		
		if(ans == 1)
			cout << "Case #" << t << ": GABRIEL" << endl;
		else if(ans == 2) cout << "Case #" << t << ": RICHARD" << endl;
	
	}
	
}
