#include <bits/stdc++.h>
using namespace std;
int main(){
	int t;
	scanf("%d",&t);
	for(int tt = 1;tt <=t;tt++){
		int k;
		string j;
		int pres = 0;
		int cont = 0;
		scanf("%d",&k);	
		cin >> j;
		for(int i = 0;i < j.size();i++){
			if(cont >= i){
				cont+=j[i]-'0';
			}
			else {
				int pi = cont;
				pres+=(i-pi);
				cont +=(i-pi);
				cont+=j[i]-'0';
			}
		}
		cout << "Case #" << tt << ": " << pres << endl;
	}
	return 0;
}
