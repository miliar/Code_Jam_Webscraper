#include<iostream>
#include<string>
using namespace std;
int main(){
	int n,num=1;
	cin>>n;
	while(n--){
		int x,ans=0,cnt=0;
		string s;
		cin>>x>>s;
		cnt+=s[0]-'0';
		for(int i=1;i<=x;i++){
			if(cnt>=i){
				cnt+=(int)(s[i]-'0');
			}else{
				ans+=i-cnt;
				cnt=i+(int)(s[i]-'0');
			}
		}
		
		
		cout<<"Case #"<<num<<": "<<ans<<endl;
		num++;
	}
	return 0;
}