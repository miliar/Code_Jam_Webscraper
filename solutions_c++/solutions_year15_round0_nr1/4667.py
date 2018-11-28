#include <bits/stdc++.h>

using namespace std;

#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define sz(x) ((int)(x).size())
#define all(c) (c).begin(),(c).end()
#define forn(i, n) for (int i = 0; i < (n); i++)
typedef long long ll;

int main(){
    int T, k, C, S;
	string Cad;
	cin>>T;
	for(int t=0; t<T; t++){
		cin>>k>>Cad;
		C=0;S=0;
		for(int i=0; i<=k; i++){
			if(Cad[i]=='0') continue;
			if(i>S){
				C+=i-S;
				S=i;				
			}
			if(Cad[i]!='0')
				S+=(Cad[i]-'0');	
		}
		cout<<"Case #"<<t+1<<": "<<C<<"\n";
	}
    return 0;
}
