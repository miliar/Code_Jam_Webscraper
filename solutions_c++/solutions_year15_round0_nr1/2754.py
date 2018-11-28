#include<iostream>
#include<cstdio>
using namespace std;
typedef long long ll;
int main(){
	int t;
	cin>>t;
	int p=0;
	while(t--){
		p++;
		int n;
		cin>>n;
		int ans=0;
		int standing=0;
		string str;
		int s;
		cin>>str;
		for(int i=0;i<=n;i++){
			s=str[i]-'0';
			if(s==0)continue;
			if(standing>=i){
				standing+=s;
			}else{
				//cout<<"req="<<i<<"standing="<<standing<<endl;
				ans+=(i-standing);
				standing=i;
				standing+=s;
			}
		}
		printf("Case #%d: %d\n",p,ans);
	}
}
