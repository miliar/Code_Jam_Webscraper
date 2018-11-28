#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

char str[1005];
int main()
{
	freopen("A-small-attemp0.out","w",stdout);
	int T;
	int n;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++){
		scanf("%d",&n);
		scanf("%s",str);
		int stand = str[0]-'0';
		int ans=0;
		for(int i=1;i<=n;i++){
			if(stand<i){
				ans+=i-stand;
				stand=i;
				stand+=str[i]-'0';
			}
			else {
				stand+=str[i]-'0';
			}
		}
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}
