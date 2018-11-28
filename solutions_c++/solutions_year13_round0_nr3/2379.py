#include <iostream>
#include <cstring>
#include <cmath>

using namespace std;

typedef unsigned long long int ul;

bool palindromo(ul palin){
		//cout<<palin<<endl;
		ul aux = palin;
		ul res = 0;
		while(aux > 0){
			res*=10;
			res+=aux%10;
			aux/=10;
		}
		return palin==res;
}


int main()
{
    int t, c = 1;
    cin >> t;
    while (t--) {
		cout << "Case #" << c++ << ": ";
		ul a, b;
		cin>>a>>b;
		long long resp = 0;
		for(ul i = ceil(sqrt(a));i<=floor(sqrt(b));++i){
			if(palindromo(i) && palindromo(i*i)){resp++;}
			
		}
		cout<<resp<<endl;
    }


    return 0;
}
