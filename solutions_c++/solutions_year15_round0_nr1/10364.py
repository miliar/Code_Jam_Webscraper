#include<iostream>

using namespace std;

int main(){
	
	char c[2005];
	int t;
	cin>>t;
	int x=1;
	gets(c);
	while(t--){
		gets(c);
		
		int n=c[0]-'0';
		int arr[1005];
		int sum[1005];
		int count=0;
		sum[0]=0;
		
		arr[0]=c[2]-'0';
		
		for(int i=1;i<=n;i++){
			arr[i]=c[i+2]-'0';			
			sum[i]=sum[i-1]+arr[i-1];
		}
		
		for(int i=1;i<=n;i++){
			//cout<<arr[i];
			if(sum[i]+count<i){
				count+=(i-(sum[i]+count));
			}
		}
		
		cout<<"Case #"<<x<<": "<<count<<"\n";
		
		x++;
	}
	
}
