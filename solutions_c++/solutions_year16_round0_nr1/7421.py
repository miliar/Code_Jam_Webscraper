using namespace std;
#include<iostream>

int main(){
	int t;
		
	cin>>t;
	for(int i=1;i<=t;i++){
		long n, ans = -1, temp;
		int digit[10] = {0},k;
		
		cin>>n;

		if(n != 0)
		for(long j=1;j<2000;j++){
			temp = j * n;
			while(temp != 0){
				digit[temp%10] = 1;
				temp = temp/10;
			}

			for(k=0;k<10;k++){
				if(digit[k] == 0)break;
			}

			if(k == 10){
				ans = j*n;
				break;
			}
		}

		if(ans != -1)
		    cout<<"Case #"<<i<<": "<<ans<<"\n";
		else
		    cout<<"Case #"<<i<<": INSOMNIA\n";
	}

return 0;
}


