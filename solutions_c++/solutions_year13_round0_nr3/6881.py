#include <iostream>
#include <cstdlib>
#include <cmath>

using namespace std;
bool is_palindrome(unsigned long long int n){
	unsigned long long int rev=0;
	unsigned long long int t=n;
	while(n!=0){
		rev = rev*10+n%10;
		n/=10;
	}
	if(rev==t) {
		return true;
	}
	else return false;
}

int main(){
		int T;
		cin>>T;
		int j=1;
		while(T--){
			unsigned long long int a;
			unsigned long long int b;
			unsigned long long int p;
			unsigned long long int q;
			cin>>a>>b;
			p=sqrt(a);
			q=sqrt(b);
			int c=0;
			for(int i=p;i<=q;i++){
				unsigned long long int r=i*i;
				if(is_palindrome(i)&&is_palindrome(r)&&r>=a&&r<=b) c++;
			}
			cout<<"Case #"<<j<<": "<<c<<endl;
			j++;
		}
		return 0;
}
