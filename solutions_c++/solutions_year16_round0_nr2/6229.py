#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
	int t;
	char ant;
	string x;
	int cse=1;
	cin>>t;
	while(t--){
		cout<<"Case #"<<cse++<<": ";
		cin>>x;
		ant=x[0];
		int c=0;
		x+='+';
		for(int i=0;i<x.size();i++){
			if(x[i]!=ant)c++;
			ant=x[i];
		}
		cout<<c<<"\n";
	}
	return 0;
}
