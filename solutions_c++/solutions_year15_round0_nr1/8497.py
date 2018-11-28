#include <cstdio>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){

	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);

	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		int a;
		string b;
		cin>>a>>b;
		int s=0,ans=0;
		s+=b[0]-'0';
		for(int j=1;j<=a;j++){
			if(s<j) {
				ans+=j-s;
				s+=j-s;
			}
			s+=b[j]-'0';
		}
		printf("Case #%d: %d\n",i,ans);
	}

}
