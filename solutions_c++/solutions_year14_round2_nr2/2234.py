#include <iostream>
using namespace std;

int main (int argc, char *argv[])
{
	int TC;
	cin >> TC;
	for(int c = 1; c <= TC; c++){
		int A, B, K;
		cin >> A >> B >> K;
		
		int ans = 0;
		for(int i = 0; i < A; i++){
			for(int j = 0; j < B; j++){
				if((i & j) < K){
					ans++;
				}
			}
		}
		
		cout << "Case #" << c << ": " << ans << endl;
	}
	
	return 0;
}

