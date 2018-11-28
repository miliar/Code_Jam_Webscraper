#include <iostream>
#include <set>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int T=1 ; T<=t; T++){
		long long n;
		cin>>n;
		long long cpy=n;
		if(n==0){
			cout<<"Case #"<<T<<": INSOMNIA\n";
			continue;
		}
		set<int> s;
		while(true){
			long long temp = n;
			//cout<<s.size()<<" "<<n<<"\n";
			while(temp){
				s.insert(temp%10);
				temp/=10;
			}
			if(s.size()==10)
				break;
			n+=cpy;
		}
		cout<<"Case #"<<T<<": "<<n<<"\n";
	}
	return 0;
}