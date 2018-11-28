#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for (int asd=1;asd<=t;asd++){
		string s;
		int k;
		cin>>s;
		scanf("%d",&k);
		int ans=0;
		for (int i=0;i<=s.size()-k;i++)
			if (s[i]=='-'){
				for (int j=i;j<i+k;j++)
					if (s[j]=='-') s[j]='+';
					else s[j]='-';
				ans++;
			}
		bool ok=1;
		for (int i=0;i<s.size();i++)
			if (s[i]=='-') ok=0;
		if (!ok) printf("Case #%d: IMPOSSIBLE\n",asd);
		else printf("Case #%d: %d\n",asd,ans);
	}
}