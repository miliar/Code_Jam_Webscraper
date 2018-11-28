#include <iostream>
#include <set>
using namespace std;
int main(){
	long long n;
	int t,c;
	cin>>t;
	for(int i=1;i<=t;i++){
		set<int> x;
		cin>>n;
		c=n;
		if(n==0){
			cout<<"Case #"<<i<<": INSOMNIA\n";
			continue;
		}
		while(1){
			int temp = n;
			while(temp>0){
				x.insert(temp%10);
				temp/=10;
			}
			if(x.size()==10)
				break;
			n+=c;

		}
		cout<<"Case #"<<i<<": "<<n<<"\n";
	}
}