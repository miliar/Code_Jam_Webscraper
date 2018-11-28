#include <iostream>
#include <string>
using namespace std;

string s="S",p="P",r="R";

string rec(int at,int n){
	if(n==0){
		if(at==1) return p;
		if(at==2) return r;
		return s;
	}
	string a=rec(at,n-1),b=rec(at%3+1,n-1);
	if(a.compare(b)<0) return a+b;
	return b+a;
}

int main(){
	int testes;
	scanf("%d",&testes);
	for(int t=1;t<=testes;t++){
		int n,p,r,s;
		scanf("%d %d %d %d",&n,&r,&p,&s);
		printf("Case #%d: ",t);
		int a=(1<<n)/3;
		if(p<a || r<a || s<a || p>(a+1) || r>(a+1) || s>(a+1)){
			printf("IMPOSSIBLE\n");
		}
		else{
			string resp;
			if(r==s) resp=rec(n%3+1,n);
			if(p==s) resp=rec((n+1)%3+1,n);
			if(p==r) resp=rec((n+2)%3+1,n);
			cout <<resp<<"\n";
		}
	}
	return 0;
}
	
