#include <iostream>
#include <string>
using namespace std;

int T, K, t, flipCount;
string S;

int main()
{
	ios::sync_with_stdio(false);
	
	cin >> T;
	for(t=1; t<=T; t++)
	{
		cin >> S >> K;
		
		flipCount = 0;
		for(int i=0; i<S.length()-K+1; i++) {
			if(S[i] == '-') {
				flipCount++;
				for(int j=i; j<i+K; j++) {
					S[j] = (S[j] == '-') ? '+' : '-';
				}
			}
		}
		
		for(int i=S.length()-K+1; i<S.length(); i++) {
			if(S[i] == '-') {
				flipCount = -1;
				break;
			}
		}
		
		cout << "Case #" << t << ": ";
		if(flipCount == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << flipCount << endl;
	}
	
	return 0;
}
