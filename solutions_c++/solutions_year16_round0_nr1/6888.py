#include <bits/stdc++.h>
using namespace std;

#define LL long long int

bool mark[12];

int main(){
	
	freopen("aain", "r", stdin);
	freopen("aaout", "w", stdout);
	
	LL tc, n, t=0;
	
	cin>>tc;
	
	while(tc--){
		t++;
		cin>>n;
		for(int i=0;i<10;i++){
			mark[i]= false;
		}
		if(n==0)
			cout<< "Case #"<<t<<": "<<"INSOMNIA\n";
		else{
			LL k= 1, nn;
			while(true){
				nn= k*n;
				while(nn){
					LL m= nn%10;
					mark[m]= true;
					nn /= 10;
				}
				int cnt= 0;
				for(int i=0;i<10;i++){
					if(mark[i]){
						cnt++;
					}
				}
				if(cnt==10) break;
				k+=1;
			}
			cout<< "Case #"<<t<<": "<<(k*n)<<"\n";
		}	
	}
}
