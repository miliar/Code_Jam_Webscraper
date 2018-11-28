#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<iostream>
#define fi first
#define se second
#define MP make_pair
#define PB push_back
#define PII pair<int,int>
typedef long long LL;
using namespace std;
char s[1010];
int n,K,T;
template<class T>
void read(T&x)
{
	char ch=getchar();int mk=1;x=0;for(;ch!='-'&&(ch<'0'||ch>'9');ch=getchar());
	if (ch=='-') mk=-1,ch=getchar();for(;ch>='0'&&ch<='9';ch=getchar()) x=x*10+ch-48;x*=mk;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	read(T);
	for(int _=1;_<=T;_++)
	{
		printf("Case #%d: ",_);
		scanf("%s",s);
		n=strlen(s);read(K);
		int ans=0;
		for(int i=0;i+K-1<n;i++)
			if (s[i]=='-')
			{
				for(int j=0;j<K;j++)
					if (s[i+j]=='-') s[i+j]='+';
					else s[i+j]='-';
				ans++;
			}
		bool flag=1;
		for(int i=0;i<n;i++)
			if (s[i]=='-')
			{
				flag=0;break;
			}
		if (flag) printf("%d\n",ans);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
