#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main(){
	int t, f, s_size, aux; // tests, flaps, stringSize
	string s;
	while(cin >> t){
		for(int i=1; i<=t;i++){
			cin >> s;
			s_size = s.size();
			f = 0;
			while(true){
				if(s.find('-')>s.size()) break;
				else if(s.find('+')>s.size()) { f++; break; }
				else{
					for(int j=s_size-1;j>=0;j--){
						if(s[j]=='-'){
							s_size = j+1;
							break;
						}
					}
					aux = 0;
					for(int j=0; j<s_size;j++){
						if(s[j] == '-'){
							aux = j;
							break;
						}
					}

					for(int j=0; j<aux;j++){ s[j] = '-';}// flap the top e<===========errado o f++ nesse ponto
					if(aux >0) f++;
					for(int j=0;j<s_size;j++) s[j]=='+'?s[j]='-':s[j]='+';
					reverse(s.begin(),s.begin()+s_size);
					f++;
				}
			}
			cout << "Case #"<< i <<": "<< f << endl;
		}
	}
	return 0;
}