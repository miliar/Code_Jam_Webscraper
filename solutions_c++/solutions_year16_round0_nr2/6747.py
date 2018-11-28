#include <iostream>
#include <string>
#include <cstdio>
using namespace std;

int main() {
	    
	char pre;
	int t,i,j,l,ans;
	string s;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		cin>>s;
		ans=0; l=s.size();
		pre=s[0];
		for(j=1;j<l;j++)
			if(s[j]!=pre) {ans++; pre=s[j];}
		if(s[l-1]=='-') ans++;
	printf("Case #%d: %d\n",i,ans);	
	}
	return 0;
}
