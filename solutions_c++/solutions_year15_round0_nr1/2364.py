#include <bits/stdc++.h>
using namespace std;
bool verificar(string cad, int x){
	int n=cad.length();
	for(int i=0;i<n;i++){
		if(x>=i)
			x+=int(cad[i]-'0');
		else return false;
	}

	return true;
}
int main(){
	int n;
	string cad;
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>n>>cad;

		int max=(n+1)*9+100;
		int x;
		//soy un trulssss :v :v :v :v
		//code jam suck my dick
		for(x=0;x<=max;x++){
			if(verificar(cad,x))
				break;			
		}
		printf("Case #%d: %d\n",i,x);
	}
	return 0;
}