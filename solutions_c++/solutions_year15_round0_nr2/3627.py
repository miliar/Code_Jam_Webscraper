#include <bits/stdc++.h>

using namespace std;

vector<long long int> cara;


int main(){
	int t;
	cin >> t;
	for(int tt = 1;tt <= t;tt++){
		cara.clear();
		long long int n;
		cin >> n;
		long long int maior = 0;
		for(int i = 0;i < n;i++){
			long long int pi;
			cin >> pi;
			maior = max(maior,pi);
			cara.push_back(pi);
		}
		long long int tot = 10000000000;
		long long int cont = 0;
		for(int maxi = maior;maxi >=1;maxi--){
			cont = 0;
			for(int i = 0;i < cara.size();i++){
				
					if (maxi < cara[i]){
								if(maxi == 1){
								cont+=cara[i]-1;
								continue;
							}
							long long temp = cara[i];
						if(temp%maxi)cont++;		
							temp-=temp%maxi;
							cont+=(temp/maxi)-1;
					}
			}
			tot = min(tot,cont+maxi);
		}
		cout << "Case #" << tt << ": " << tot << endl;
	}
}
