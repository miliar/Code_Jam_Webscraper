#include<iostream>
#include<cstring>
using namespace std;

int main(){
	int t;
	cin>>t;
	int case_no=1;
	while(t--){
		int n;
		cin>>n;
		string s;
		cin>>s;
		int sum=0,ans=0;
	
		for(int i=0;i<n+1;i++){
			sum+= s[i]-'0';
			if(sum<i+1){
				ans++;
				sum++;
			}

		}
		
		cout<<"Case #"<<case_no<<": "<<ans<<endl;

		case_no++;
	}
	return 0;
}