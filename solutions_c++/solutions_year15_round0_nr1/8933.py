#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define forsn(i,s,n) for(int i=(s); i<(int)(n); i++)
#define forn(i,n) forsn(i,0,n)

int main(){
	int T; cin >> T;
	forn(t,T){
		int n; cin >> n;
		n++;
		vector<int> audiencia(n);
		forn(i,n){
			char c; cin >> c;
			audiencia[i] = c - '0';
		}
		int cont = 0;
		forsn(i,1,n){
			audiencia[i] = audiencia[i] + audiencia[i-1];
			int dif = i - (audiencia[i-1] + cont);
			//cout << audiencia[i-1] << " " << cont << " " << dif << endl;
			
			if(dif > 0){
				cont+=dif;
			}
		}
		cout << "Case #" << t+1 << ": " << cont << endl;
	}
}
