#include<bits/stdc++.h>
using namespace std;

int mult(int x, int y){
	if(x < 0) return -mult(-x, y);
	if(y < 0) return -mult(x, -y);
	if(x == 1) return y;
	if(y == 1) return x;
	if(x == y) return -1;
	if(x == 2){
		if(y == 3) return 4;
		if(y == 4) return -3;
	} 
	if(x == 3){
		if(y == 2) return -4;
		if(y == 4) return 2;
	}
	if(x == 4){
		if(y == 2) return 3;
		if(y == 3) return -2;
	}
	return 0;
}

int mymap(char c){
	if(c == 'i') return 2;
	if(c == 'j') return 3;
	if(c == 'k') return 4;
	return 0;
}

int main(){
	int T;
	cin>>T;
	for(int t=1; t<=T; t++){
		int l, X;
		cin>>l>>X;
		string L;
		cin>>L;
		int cur = 1, flag = 0;
		for(int x=0; x<l*X; x++){
			cur = mult(cur, mymap(L[x%l]));
			if(flag == 0 && cur == mymap('i')) flag++;
			if(flag == 1 && cur == mymap('k')) flag++;
		}
		cout<<"Case #"<<t<<": ";
		if(flag == 2 && cur == -1) cout<<"YES"<<endl;
		else cout<<"NO"<<endl;
	}
	return 0;
}
