#include <iostream>
using namespace std;

int main() {
	// your code goes here
	long long int t;
	cin>>t;
	for(long long int i = 1; i <= t; i++ ){
		cout<<"Case #"<<i<<": ";
		long long int n, ans;
		cin>>n;
		int a[11]={0};
		if(n == 0){
			cout<<"INSOMNIA"<<endl;
		}
		else{
			for(long long int j = 1; ; j++){
				int flag = 1;
				ans = j * n;
				while(ans != 0){
					int d = ans % 10;
					a[d] = 1;
					ans = ans / 10;
				}
				ans = j * n;
				for(long long int i = 0; i < 10; i++){
					flag = 0;
					if(a[i] == 0){
						flag = 1;
						break;
					}
				}
				if(flag){
					continue;
				}
				else{
					break;	
				}
			}
			cout<<ans<<endl;
		}
	}
	return 0;
}