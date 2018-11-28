#include <iostream>
using namespace std;
int main(){
	int t;
	cin>>t;
	int i1=1;
	while(t--){
		int m;
		cin>>m;
		string str;
		cin>>str;
		int ans=0;
		int count=0;
		for(int i=0;i<=m;i++){
			if(count<i && str.at(i)-'0' != 0)
			{
			ans = ans + i - count;
			count = count + i - count;
			}
			count = count + str.at(i) - '0';
			//cout<<" i = "<<i<<"count = "<<count<<endl;
			if(count>m)
			break;
		}
		cout<<"Case #"<<i1<<": "<<ans<<endl;
		i1++;
	}
}
