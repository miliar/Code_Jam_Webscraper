#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("inp.txt","r",stdin);
	freopen("outpl.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int tst = 1;tst <=t; tst++) {
		int sum=0;
		int ans=0;
		int n;
		string s;
		scanf("%d",&n);
		cin >> s;
		int l = s.length();
		for (int i = 0; i < l; i++) {
			if(sum >= i) {
				sum+=s[i]-'0';
			}
			else {
				ans += (i-sum);
				sum=i;
				sum+=s[i]-'0';
			}
		}
		printf("Case #%d: %d\n",tst,ans);
		//cout << ans << endl;
	}
}
