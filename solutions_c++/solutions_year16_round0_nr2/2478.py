#include <iostream>
#include <string>

using namespace std;

int main(){
	int t,i,j;
	int res;
	string slowo;
	cin >> t;
	for(i=0; i<t; i++){
		cin >> slowo;
		slowo += '+';
		res = 0;
		for(j=0; j+1<slowo.size(); j++) if(slowo[j] != slowo[j+1]) res++;
		cout << "Case #" << i+1 << ": " << res << "\n"; 
	}
	return 0;
}
