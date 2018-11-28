#include<cstdio>
#include<iostream>
#include<string>
using namespace std;

int main(){
	
	//freopen("B-large.in","r",stdin);
	//freopen("B-small-attempt0.out","w",stdout);
	string str;
	int n,ans;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		cin>>str;
		ans=0;
		for(int j=0;j<str.size();j++){
			if(str[j]=='-'){
				for(;j<str.size();j++){
					if(str[j]=='+'){
						j--;break;
					}
				}
				ans++;
			}else{
				for(;j<str.size();j++){
					if(str[j]=='-'){
						j--;break;
					}
				}
				ans++;
			}
		}
		if(str[str.size()-1]=='+')ans--;
		printf("Case #%d: %d\n",i+1,ans);
	}
	
	
	
	
	
	return 0;
}
