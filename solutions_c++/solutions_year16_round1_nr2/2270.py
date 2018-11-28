#include <bits/stdc++.h> 

using namespace std;

typedef long long ll;


int main(){
	int tc ; 
	cin>>tc;
	for(int tt = 1;tt<=tc;tt++){
		int arr[3000] ; 
		int n ; 
		cin>>n;
		memset(arr , 0 , sizeof arr);
		for(int i=0;i<(2*n-1);i++){
			for(int j=0;j<n;j++){
				int curr ;
				cin>>curr;
				arr[curr]++;
			}
		}
		printf("Case #%d:",tt );
		for(int i=1;i<2501;i++){
			if(arr[i]==0)
				continue;
			if(arr[i]%2!=0){
				cout<<" "<<i;
			}
		}
		cout<<endl;
	}
}