#include<iostream>
#include<string>
using namespace std;

int main()
{
//	freopen("b.in","r",stdin);
//	freopen("b.out","w",stdout);
	int T;
	cin>>T;
	string str;
	for(int i=1;i<=T;i++){
		cin>>str;
		cout<<"Case #"<<i<<": ";
		int minus=0;
		bool flag=false;
		for(int i=0;i<str.length();i++){
			if(str[i]=='-'){
				if(!flag) minus++;
				flag=true;
			}else{
				flag=false;
			}
		}
		int ans=0;
		if(str[0]=='+') ans++;
		ans+=2*minus-1;
		cout<<ans<<endl;
		
	}
	return 0;
}
