#include <iostream>
#include <cstdlib>
#include <cstdio>
#define inf (1<<30)
using namespace std;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	cin>>T;
	for (int _=1;_<=T;_++){
		int n;
		cin>>n;
		char ch=getchar();
		int ans=0,sum=0;
		for (int i=0;i<=n+1;i++){
			ch=getchar();
			ans+=max(0,i-sum);
			sum=max(sum,i);
			sum+=ch-'0';
		}
		printf("Case #%d: %d\n",_,ans);
	}
}
