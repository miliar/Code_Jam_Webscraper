#include<iostream>
using namespace std;
int main(){
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	int k = 0 ;
	while(t--){
		++k;
		int s;
		cin>>s;
		string S ;
		cin>>S ;
		int arr[1002] = {0}; 
		arr[0] = S[0] - '0' ;
		int ans = 0 ;
		for(int i = 1 ; i <= s ; i ++ ) 
		{
			if(S[i] == '0') 
			 ;
			else if(arr[i-1] < i ) 
				{
					ans += i - arr[i-1] ;
					arr[i] += i - arr[i-1] ; 
				}
			arr[i] += arr[i-1] + S[i] -'0' ;
		}
		cout<<"Case #"<<k<<": "<<ans<<endl;
	}
}
