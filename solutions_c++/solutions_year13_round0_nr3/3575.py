#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <cstdio>
using namespace std;

bool es_palindromo(int n){
	string s,s_rev;
	stringstream ss ;
	ss<<n;
	s=ss.str();
	s_rev=s;
	reverse(s_rev.begin(),s_rev.end());
	return (s == s_rev);
}

int count_palin(int x,int y){
//	int raizX=sqrt(x),raizY=sqrt(y);
	int cont=0;
//	if(raizX*raizX == x){
//		if(es_palindromo(raizX) && es_palindromo(x))
//			cont++;
//	}
//	if(raizY*raizY == y && x!=y){
//		if(es_palindromo(raizY) && es_palindromo(y))
//			cont++;
//	}
//	for(int j=raizX+1;j<raizY;j++){
//		if(es_palindromo(j) && es_palindromo(j*j))
//			cont++;
//	}
	if(1==x or 1==y)
		cont++;
	if(4>=x and 4<=y)
		cont++;
	if(9>=x and 9<=y)
		cont++;
	if(121>=x and 121<=y)
		cont++;
	if(484>=x and 484<=y)
		cont++;
	return cont;
}

int main(int argc, char *argv[]) {
	
	freopen ("C-small-attempt2.in","r",stdin);
	freopen ("C-small-attempt2.out","w",stdout);
	
	int n,n2,n3;
	cin>>n;
	for(int i=1;i<=n;i++){
		cin>>n2>>n3;
		cout<<"Case #"<<i<<": "<<count_palin(n2,n3)<<endl;
	}
	return 0;
}

