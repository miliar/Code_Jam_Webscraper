#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
using namespace std;
int main(){
	int t,s_max;
	string s;
	scanf("%d",&t);
	for(int z=1;z<=t;z++){
		long count=0,ans=0,last_ans=0;
		scanf("%d",&s_max);
		cin>>s;
		count=s[0]-'0';
		//cout<<"count: "<<count;
		for(int i=1;i<=s_max;i++){
			if((i-count)>0 && s[i]!=0){
				ans=i-count;
				count+=ans;
				last_ans+=ans;
			}
			count+=s[i]-'0';
		}
		cout<<"Case #"<<z<<": "<<last_ans<<endl;
	}
	return 0;
}
