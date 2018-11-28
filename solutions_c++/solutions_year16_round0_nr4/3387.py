#include <iostream>
using namespace std;
int main(){
	int t;
	int k,c,s;
	while(cin >>t){
		int i = 1;
		while(t--){
			cin>>k>>c>>s;
			cout<<"Case #"<<i<<":";
			i++;
			long long b = 1;
			for(long long i =  0; i < c; i++)
				b *= k;
			long long bk = b / k;
			for(long long i = 1; i <= b; i += bk){
				cout<<" "<<i;
			}
			cout<<endl;
		}
	}
}