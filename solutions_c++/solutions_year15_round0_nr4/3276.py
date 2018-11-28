#include<bits/stdc++.h>
using namespace std;
int pp(int i){
	return i*((i+1)/2);
}

int main(){
	int t,x,r,c,i;
	cin >> t;
	for(i=1;i<=t;++i){
		cin >> x >> r >> c;
		 if(((r*c)%x!=0) || (x-1>r||x-1>c)) cout << "Case #"<<i<<": " << "RICHARD" << endl;
		 else cout << "Case #"<<i<<": " << "GABRIEL" << endl;
	}
}
