//  g++ a.cpp - a -std=c++11 && ./a < a.in > a.out
#include <iostream>
#include <string>
using namespace std;

int main(){
	int t = 1;
	cin >> t;
	string s, resp, aux, aux2;
	for (int i=1;i<=t;i++){
		resp = "";
		cin >> s;
		aux = s[0];
		resp.insert(0,aux);
		for(int j=1;j<s.size();j++){
			aux2 = s[j];
			if(s[j]<aux[0]) resp.insert(resp.size(), aux2);
			else{
				resp.insert(0,aux2);
				aux = aux2;
			}
		}

		cout << "Case #"<< i << ": " << resp << endl;
	}

}