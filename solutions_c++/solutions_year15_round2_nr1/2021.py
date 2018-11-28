#include <iostream>
using namespace std;
 
#define lli long long int

lli rev(lli i, bool * real){
	lli ans = 0;
	*real = true;
	if(i%10 == 0){
		*real = false ;
	}
	while(i!=0){
		ans *= 10;
		ans += i%10;
		i/=10;
	}
	return ans;
}

int main(){
	lli T, N;
	cin>>T;
	lli reverseOfi;
	int* ans = new int[1000001];
	ans[0] = 0;
	for (lli i = 1; i < 1000001; ++i)
	{
		bool real  = true;
		reverseOfi = rev(i, &real);
		if(reverseOfi < i  && real == true){
			if(ans[i-1] < ans[reverseOfi]){
				ans[i] = 1 + ans[i-1];
			}else{
				ans[i]  = 1 + ans[reverseOfi];
			}
		}else{
			ans[i] = 1 + ans[i-1];
		}
		//cout<<ans[i]<<endl;
	}

	for (int i = 1; i <= T; ++i)
	{
		cin>>N;
		cout<<"Case #"<<i<< ": "<<ans[N]<<endl;	
	}
	return 0;
}