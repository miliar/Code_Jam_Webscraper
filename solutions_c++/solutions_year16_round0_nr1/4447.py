#include <iostream>
using namespace std;

int main(){
	int T;
	cin >> T;
	
	for(int z = 1; z <= T; z++){
		long long int Z;
		cin >> Z;
		
		if(Z == 0)
			cout << "Case #" << z << ": " << "INSOMNIA" << endl;
		else{
			bool t = false;
			bool bylo[10];
			for(int i = 0; i < 10; i++)
				bylo[i] = false;
				
			long long res = Z;
			while(t == false){
				long long tmp = res;
				while(tmp > 0){
					bylo[tmp % 10] = 1;
					tmp = tmp / 10;
				}
				int ile = 0;
				for(int i = 0; i < 10; i++){
					if(bylo[i] == 1){
						ile++;
					}
				}
				
				if(ile == 10){
					break;
				}
				res += Z;
			}
			
			cout << "Case #" << z << ": " << res << endl;
		}
	}
	return 0;
}
