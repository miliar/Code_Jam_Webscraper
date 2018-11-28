#include <bits/stdc++.h>
int a[1001];
using namespace std;
int main()
{
	freopen("input.in","r",stdin);
	freopen("out.in","w",stdout);
	int n,i,t,j,div,k,p;
	int u = 1;
	cin>>t;
	while(t--){
		long long int ans = 9999999;
		long long int sum = 0;
		cin>>n;
		for(i = 0; i < n; i++){
			cin>>a[i];
		}
		sort(a,a + n);
		for(i = 1; i < 1001; i++){
			sum = 0;
			if(i <= a[n - 1]){
				for(j = n - 1; j >= 0; j--){
					if(a[j] >= i){
						p = a[j]/i;
						if(a[j]%i == 0){
							p--;
						}
						sum = sum + p;
					}
				}
				div = sum + i;
				if(div < ans){
					ans = div;
				}		
			}else{
				break;
			}
			
		}
		cout<<"Case #"<<u++<<":" <<" "<<ans<<endl;
	}
}
