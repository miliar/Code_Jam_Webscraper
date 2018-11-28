#include <bits/stdc++.h>
using namespace std;

int main(){
	string a;
	int t, cont;
	char act;
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>a;
		cont=0;
		int it=a.length()-1;
		while(a[it]=='+') it--;
		while(it>=0){
			cont++;
			act=a[it];
			while(a[it]==act) it--;
		}
		cout<<"Case #"<<i<<": "<<cont<<"\n";
	}
}