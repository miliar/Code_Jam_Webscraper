#include <bits/stdc++.h>
using namespace std;
#define ll long long


int main()
{
	int tt,t,i,flip,ans;
	char str[120];
	cin >>tt;
	for(t=1;t<=tt;t++) {
		cin >> str;
		printf("Case #%d: ",t);
		flip=0;ans=0;
		for(i=strlen(str)-1;i>=0;i--) {
			if(flip)
				str[i]=(str[i]=='+'?'-':'+');
			if(str[i]=='-') {
				ans++;
				flip^=1;
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}