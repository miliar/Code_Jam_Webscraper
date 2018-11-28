#include <bits/stdc++.h>

using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n,i,t,j,d,k,p;
	int x = 0;
	cin>>t;
	while(t--){
		int array[10001];
		long long int result = 9999999;
		long long int sum = 0;
		cin>>n;
		for(i = 0; i < n; i++){
			cin>>array[i];
		}
		sort(array,array + n);
		for(i = 1; i < 1001; i++){
			sum = 0;
			if(i <= array[n - 1]){
				for(j = n - 1; j >= 0; j--){
					if(array[j] >= i){
						p = array[j]/i;
						if(array[j]%i == 0){
							p--;
						}
						sum = sum + p;
					}
				}
				d = sum + i;
				if(d < result){
					result = d;
				}		
			}else{
				break;
			}
			
		}
		x++;
		cout<<"Case #"<<x<<":"<<" "<<result<<endl;
	}
}
