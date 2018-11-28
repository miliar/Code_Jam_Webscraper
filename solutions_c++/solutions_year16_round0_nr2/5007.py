#include <bits/stdc++.h>

using namespace std;

int main(){
	int T,N;
	cin>>T;

	for(int K=1; K<=T; K++){
		long long ans = 0;
		string s;
		cin>>s;

		for(int i=s.size()-1; i>=0; i--){
			if(s[i] == '-'){
				for(int j=i; j>=0; j--){
					if(s[j] == '-')
						s[j] = '+';
					else if(s[j] == '+')
						s[j] = '-';
				}
				ans++;
			}
		}

		printf("Case #%d: %ld\n", K, ans); 
	}

	return 0;
}