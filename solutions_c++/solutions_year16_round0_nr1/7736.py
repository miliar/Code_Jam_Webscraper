#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main(){
	int t;
	cin>>t;
	for (int k = 1; k<=t; k++){
		ll n;
		cin>>n;
		if (n == 0){
			cout<<"Case #"<<k<<": INSOMNIA\n";
			continue;
		}
		int arr[10];
		memset(arr,0,sizeof(arr));
		for (int i = 1; i<=1000000; i++){
			ll num = (ll)i * n;
			while (num){
				arr[num%10] = 1;
				num /= 10;
			}
			int flag = 0;
			for (int j = 0; j<10; j++)
				if (arr[j] == 0)
					flag = 1;
			if (!flag){
				cout<<"Case #"<<k<<": "<<(ll)i*n<<endl;
				break;
			}
		}
	}
	return 0;
}