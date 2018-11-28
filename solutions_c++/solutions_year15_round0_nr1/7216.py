#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
	ll casos, tam, qtdp, contador = 1, i, resp;
	string s1;
	//0100661
	
	cin >> casos;
	while(casos--){
		cin >> tam;
		cin >> s1;
		
		qtdp = 0;
		resp = 0;
		for(i=0; i<s1.size(); i++){
			if(s1[i] == '0')
				continue;
			if(qtdp >= i)
				qtdp += s1[i] - '0';
			else{
				resp += i - qtdp;
				qtdp += i - qtdp;
				qtdp += s1[i] - '0';
				//cout << "tenho: " << qtdp << endl;
			}
		}
		
		cout << "Case #" << contador++ << ": " << resp << "\n";
	}
	
	return 0;
}
			
		
