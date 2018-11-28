#include <bits/stdc++.h>
using namespace std;

long N, T, i, x;
set <long> s;
int main(){
	cin>>T;
	for(int c=1; c<=T; c++){
		s.clear();
		cin>>N;
		int i =1;
		if(N!=0)
			while(s.size() < 10) {
				x = N*(i++);
				while(x) {
					s.insert(x%10);
					x/=10;
				}
			}

		if(N!=0)
			cout<<"Case #"<<c<<": "<<N*(i-1)<<endl;
		else
			cout<<"Case #"<<c<<": INSOMNIA"<<endl;
	}
}