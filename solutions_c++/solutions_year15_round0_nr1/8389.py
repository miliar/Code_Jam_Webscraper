#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

#define icin(x) scanf("%d",&x)


int main(){
	int T;
	icin(T);
	int N,n,ans,member_clapped;
	string s;
	for(int t=1;t<=T;t++){
		ans=0;
		member_clapped=0;
		icin(N);
		cin>>s;
		for(int i=0;i<s.size();i++){
			n=s[i]-'0';
			if(n==0)
				continue;
			if(member_clapped<i)
			{
				ans += (i-member_clapped);
				member_clapped = i + n;
			}
			else
			{
				member_clapped += n;
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}