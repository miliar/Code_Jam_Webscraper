#include <bits/stdc++.h>
#define endl '\n'

using namespace std;

string cad;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int t;
	int u = 1;
	cin>>t;
	
	while(t--){
		cin>>cad;
		
		int i = 0;
		int a = 0 , b = 0;
		
		while(i<cad.size()){
		
			int f = 0;
			while(i<cad.size() && cad[i]=='+'){
				i++;
				f = 1;
			}
			if(f) a++;
			
			f = 0;
			while(i<cad.size() && cad[i]=='-'){
				i++;
				f = 1;
			}
			
			if(f) b++;
		
		}
		
		int cont;
		if(a && !b) cont = 0;
		else if(b && !a) cont = 1;
		else if(cad[0]=='+') cont = b + b;
		else cont = b + b - 1;
		
		cout<<"Case #"<<u++<<": "<<cont<<endl;
	}
	return 0;
}
