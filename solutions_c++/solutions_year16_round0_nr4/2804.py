#include <iostream>
using namespace std;
long long T, K, C, S;
long long pw(int x, int y){
	long long num = 1;
	for (int t = 0; t < y; t++){
		num*=x;
	}
	return num;
}

int main(){
	
	cin >> T;
	for(int i=1; i<=T; i++){
		cin >> K >> C >> S;
		cout << "Case #" << i << ":";
	/*	if(S*2 < K) cout << "IMPOSSIBLE\n";
		else{
			if(C==1){
				if(S < K) cout << "IMPOSSIBLE\n";
				else{
					for(int j=1; j<=K-1; j++) cout << j << " ";
					cout << K << "\n";
				}	
				
			}
			else{
			
				if(K==1) cout << "1";
				else cout << "2";
			
				if(K%2 == 0){
					long long interval = pw(K,C)/K;
						for (int j=3; j<=K; j+=2){
							cout << " " << interval*(j-1) + (j+1);
						}
					cout << "\n";
				}
				
				else{
					long long interval = pw(K,C)/K;
						for (int j=3; j+2<=K; j+=2){
							cout << " " << interval*(j-1) + (j+1);
						}
						cout << " " << interval*(K-1) + K << "\n";
					
					
				}
				
			}
		}
		
	*/
	for(int i=1; i<=K; i++) cout << " " << i;
	cout << endl;
	}
}
	
//If the G is in the first tile, then it must be in the first time regardless of the complexity

//If the G is in the second tile, then you just need to check 
/*
LGLL
LGLL GGGG LGLL LGLL
LGLL GGGG LGLL LGLL GGGG GGGG GGGG GGGG  LGLL LGLL LGLL LGLL LGLL LGLL LGLL LGLL
^                   ^*                   ^                     ^*

K^C / K
find in intervals of N^C divided by N

JUST FIND THE FIRST N LOL

If there's a G in the first, it will appear everywhere in the first and all of the ones %4

How to "save" moves:

^* helps to check both the first and the second tile
^* helps to check both the third and the fourth tile

save it by two

*/	
	


