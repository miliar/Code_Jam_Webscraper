#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

char s[6666];
int main()
{
    freopen("in.txt","r",stdin);
	freopen("out.out","w",stdout);
	int T;cin>>T;
	int cs=1;
	while(T--){
		int n;cin>>n;
		scanf("%s",s);
		int add=0,now=0;
		for(int i=0;i<n+1;i++){
			if(s[i]=='0')continue;
			if(now<i){
				add+=i-now;
				now=i;
			}else{
				;
			}
			now+=s[i]-'0';
		}
		printf("Case #%d: %d\n",cs++,add);
	}
	return 0;
}