#include<iostream>
using namespace std;
int main()
{
	int t;
	int j=0;
	cin>>t;
	while(t--){
		j++;
		int n,i;
		int a;
		int count =0;
		int ans=0;
		cin>>n;
		getchar();
		char s[n+2];
		cin>>s;
		for(i=0;i<=n;i++){
			if(count<i){
				ans=ans+(i-count);
				count=i;
			}
			count =count+s[i]-'0';
		}
		cout<<"Case #"<<j<<": "<<ans<<endl;
	}
	return 0;
}
