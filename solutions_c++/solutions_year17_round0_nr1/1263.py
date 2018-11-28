/*===============================================================
*  Filename£ºa.cpp
*  Author£ºzhuyutian
*  Date£º2017Äê04ÔÂ08ÈÕ
================================================================*/
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
const int maxn = 1005;

int T,n,k;
char s[maxn],num[maxn];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	cin>>T;
	for(int kase = 1; kase <= T; kase ++)
	{
		cin>>s>>k;
		n = strlen(s);
		for(int i = 0 ; i < n; i++) num[i] = (s[i] == '+');
		int ans = 0;
		bool p = true;
		for(int i = 0 ; i < n && p; i++)
		{
			if(num[i]) continue;
			ans++;
			for(int j = i; j < i + k; j++)
			{
				if(j >= n) { p = false; break;}
			   	num[j] ^= 1;	
			}
		}
		printf("Case #%d: ",kase);
		if(p) cout<<ans<<endl;
		else puts("IMPOSSIBLE");
	}
    return 0;
}
