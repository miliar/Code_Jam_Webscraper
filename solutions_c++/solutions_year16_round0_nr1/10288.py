#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	unsigned long long int temp,t,n,tt=0;
	cin>>t;
	while(t--){
		cin>>n;
		set<int>s;
		int i=1;
		while(i<=200 && s.size()<10){
			temp = n*i;
			while(temp){
				s.insert(temp%10);
				temp=temp/10;
			}
			i++;
		}
		if(s.size()==10)cout<<"Case #"<<++tt<<": "<<(i-1)*n<<endl;
		else cout<<"Case #"<<++tt<<": "<<"INSOMNIA\n";
	}
	return 0;
}
