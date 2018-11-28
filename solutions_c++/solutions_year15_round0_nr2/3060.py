#include<iostream>
#include<vector>
#include<algorithm>
#include<function>
#define all(c) c.begin(),c.end()
using namespace std;
int main(){
	int t,num=1;
	cin>>t;
	while(t--){
		int d,ans=10000,cnt=0;
		cin>>d;
		vector<int> vec(d);
		for(int i=0;i<d;i++){
			cin>>vec[i];
		}
		sort(all(vec),greater<int>() );
		for(int i=1;i<=vec[0];i++){
			cnt=i;
			for(int j=0;j<d;j++){
				cnt+=vec[j]/i-1;
				if(vec[j]%i!=0){
					cnt++;
				}
			}
			ans=min(ans,cnt);
		}
		cout<<"Case #"<<num<<": "<<ans<<endl;
		num++;
	}
}