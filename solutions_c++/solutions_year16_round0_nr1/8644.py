#include <iostream>

using namespace std;

#define ll long long

int main(){
	ios_base::sync_with_stdio(false);
	int t, l=1;
	cin>>t;

	while(t--){
		int n;
		cin>>n;

		int arr[10], cnt = 10, num = 0;
		for(int i=0 ; i<10 ; i++)
			arr[i] = 0;

		ll N = n;

		cout<<"Case #"<<l++<<": ";

		if(n == 0){
			cout<<"INSOMNIA\n";
			continue;
		}

		while(num<100000){
			num++;

			ll temp = N;
			while(temp){
				int digit = temp % 10;
				if(arr[digit] == 0)
					arr[digit] = 1, cnt--;
				temp /= 10;
			}

			if(cnt == 0)
				break;
			
			N += n;
		}

		if(cnt)
			cout<<"INSOMNIA\n";
		else
			cout<<N<<"\n";
	}

	return 0;
}