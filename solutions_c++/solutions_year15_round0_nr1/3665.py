#include <iostream>

using namespace std;

int main(){
	int T,S_max,m=1;
	string S;
	cin >> T;

	while(T--){
		cin >> S_max >> S;
		long long ans = 0,i = 0,t =0;
		while(i<=S_max){
			if(i>t){
				int k = i-t;
				ans +=k;
				t+=k+(S[i]-'0');
			}
			else{
					t+=(S[i]-'0');
			}
			i++;
			//cout << t << endl;
		}
		cout << "Case #"<< m << ": "<< ans << endl;
		m++;
	}
}