#include <iostream>
#include <map>
using namespace std;
typedef unsigned long long int LL;

map<int,int> mp;

int main() {
	int T;
	cin>>T;
	int cs = 1;
	while(T--) {
		int n;
		cin>>n;
		mp.clear();
		LL num;
		int k=1;
		int ct = 0;
		while(ct<=9 && n!=0) {
			num = n*k;
			k++;
			LL t=num;
			while(t) {
				int x = t%10;
				t/= 10;
				if(!mp[x]) {
					mp[x] = 1;
					ct++;
				}
			}
		}
		cout<<"Case #"<<cs++<<": ";
		if(n==0) cout<<"INSOMNIA"<<endl;
		else cout<<num<<endl;
	}
	// your code goes here
	return 0;
}