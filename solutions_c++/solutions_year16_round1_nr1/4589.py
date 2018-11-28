#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

string solve(string a){
	if( a.length()<=1) return a;
	string eval, best=a;
	for( int i=0;i<a.length()-1;i++ ){
		//eval =a.substr(i+1,1) + solve( a.substr(0,i) ) + a.substr(i+2, a.length()-i-2);
		eval =a.substr(i+1,1) + solve( a.substr(0,i+1) ) + a.substr(i+2);
		//cout<<"eval = "<<eval<<endl;
		//cout<<"eval = "<<a.substr(0,i+1) <<" + "<< a.substr(i+1, a.length()-i-1)<<endl;
		//cout<< "eval = "<<a.substr(i+1,1)<<" + "<< a.substr(0,i) << " + "<< a.substr(i+2, a.length()-i-1)<<endl;
		//cout<<eval<<endl;
		if ( eval>best  ){
			best = eval; 
		}
	}
	return best;
}


int main(){
	using namespace std;

	freopen("A-small-attempt0.in","r", stdin);
	freopen("A-small-attempt0.out","w", stdout);

	int T, sol;
	string cad, d;	
	scanf("%d\n", &T);
	for(int i=0;i<T;i++){
		getline (cin, cad);
		printf("Case #%d: ", i+1);
		//cout<<cad<<endl;
		cout<<solve( cad )<<endl;
	}
	return 0;
}

