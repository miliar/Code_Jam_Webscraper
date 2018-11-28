#include <iostream>
using namespace std;
typedef long long ll;
int main(){
	int t;
	cin >> t;
	for(int ddd=1;ddd<=t;ddd++){
		ll n,p,tmp,ntmp;
		cin >> n >> p;
								cout << "Case #" << ddd <<": ";
		ll n_2=1;
		for(int i=0;i<n;i++){
			n_2*=2;
		}
		tmp=n_2/2;
		ntmp=tmp;
		if(p==n_2) cout << n_2-1 << " ";
		else{
			for(int i=0;i<n;i++){
				if(p<=tmp){
					ll ans=1;
					for(int j=0;j<i+1;j++){
						ans*=2;
					}
					cout << ans-2 << " ";
					break;
				}
				ntmp/=2;
				tmp+=ntmp;
			}
		}
		tmp=n_2;
		ntmp=tmp;
		if(p==1) cout << 0 << endl;
		else{
			for(int i=0;i<n;i++){
				if(tmp<=p){
					ll ans=1;
					for(int j=0;j<i;j++){
						ans*=2;
					}
					cout << n_2-ans << endl;
					break;
				}
				tmp/=2;
			}
		}
	}
	return 0;
}