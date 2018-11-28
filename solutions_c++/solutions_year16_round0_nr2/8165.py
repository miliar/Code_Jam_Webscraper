#include<bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<pair<int,int> > vii;
char a[105];
int main()
{
	#ifndef ONLINE_JUDGE
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	#endif
	int t,k=1;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%s",&a);
		int n=strlen(a),ans=0,cnt=0;
		int i=0;
		while(a[i]=='-' && i<n)
		{
			cnt++;
			i++;
		}
		if(cnt>0)
		ans=1;
		for(int j=i;j<n;j++)
		if(a[j]=='-')
		{
			ans+=2;
			j++;
			while(a[j]=='-' && i<n)
			{
				j++;
			}
		}
		printf("Case #%d: %d\n",k++,ans);
	}
	return 0;
}
