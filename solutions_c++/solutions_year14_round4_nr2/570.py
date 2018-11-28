#include<algorithm>
#include<iostream>
using namespace std;

int T, N, a[1111];

int main(){

	freopen("B-large.in","r",stdin);
	freopen("Bout","w",stdout);
	
	cin>>T;
	for(int tc=1;tc<=T; tc++){
		cout<<"Case #"<<tc<<": ";

		cin>>N;
		for(int i=0; i<N; i++) cin>>a[i];

		int l=0, r=N;
		int ans=0;

		while(l!=r){
			int* ma = min_element(a+l,a+r);
			int pos = ma-a;
			int ldis = ma-(a+l), rdis = (a+r-1)-ma;

			if(ldis<=rdis){ // go left
				ans += ldis;
				for(int i=pos; i>l; i--){
					swap(a[i], a[i-1]);
				}
				l++;
			}

			else{ // go right;
				ans += rdis;
				for(int i=pos; i<r-1; i++){
					swap(a[i],a[i+1]);
				}
				r--;
			}
		}

		cout<<ans<<endl;
	}
}