#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

string nik;
int cazzo[1005];
int a;
int T;
int main(){
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> T;
	
	for(int i = 1; i <= T; ++i){
		cin >> a;
		cin >> nik;
		for(int j = 0; j < (int)nik.length(); ++j)
			cazzo[j] = nik[j] - '0';
			
		int sum = 0;
		int ans = 0;
		
		for(int j = 0; j < (int)nik.length(); ++j){
			
			//cout << j <<  " " << sum << " " <<  cazzo[j] << endl;
			if(j > sum){
				ans+= j - sum;
				sum+= j - sum;
			}
			sum += cazzo[j];
		}
		
		cout << "Case #" << i << ": " << ans << endl;
	}
}

