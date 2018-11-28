#include <iostream>
using namespace std;


bool checkAll(bool dig[]){
	for (long long int i = 0; i < 10; ++i)
	{
		if(dig[i] == false){
			return true;
		}
	}
	return false;
}

void updateDigs(bool dig[], long long int N){
	while(N>0){
		long long int r = N%10;
		N/=10;
		dig[r] = true;
	}
}

int main(){
	long long int T;
	cin>>T;
	for (long long int i = 0; i < T; ++i)
	{
		long long int N;
		cin>>N;
		cout<<"Case #"<<i+1<<": ";
		if(N==0){
			cout<<"INSOMNIA"<<endl;
		}else{
			bool dig[10];
			for (long long int d = 0; d < 10; ++d)
			{
				dig[d] = false;
			}
			long long int count = 1;
			long long int ans = N;
			updateDigs(dig, ans);
			while(checkAll(dig)){
				
				ans = N*(count++);
			//	cout<<ans<<endl;
				updateDigs(dig, ans);
			}
			cout<<ans<<endl;
		}

	}
	return 0;
}