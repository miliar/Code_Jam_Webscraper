#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
int main(){
	int cases=0,nowcase=0;
	cin>>cases;
for(nowcase=1;nowcase<=cases;nowcase++){
	int ans=0,now=0;
	string tmp;
	int s;
	int ta[10000]={0};
	cin>>s>>tmp;
	for(int i=0;i<s+1;i++)ta[i]=tmp[i]-'0';
	for(int i=1;i<=s+1;i++){
		now+=ta[i-1];
		if(now<i)now++,ans++;
	}
	cout<<"Case #"<<nowcase<<": "<<ans<<endl;
}

	return 0;
}