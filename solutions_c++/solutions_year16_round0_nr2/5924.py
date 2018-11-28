#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
char str[110];
int main()
{
	int T;
	freopen("B-large.in","r",stdin);
	freopen("data.out","w",stdout);
	cin>>T;
	for(int t=1;t<=T;t++){
		scanf("%s",str);
		printf("Case #%d: ",t);
		int len=strlen(str);
		int ans=0;
		for(int i=len-1;i>=0;i--){
			if(str[i]=='+')continue;
			ans++;
			for(int j=i;j>=0;j--)
				if(str[j]=='+')
					str[j]='-';
				else str[j]='+';
		}
		cout<<ans<<endl;
	}
	return 0;
}

