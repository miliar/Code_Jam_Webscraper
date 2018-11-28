#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef map<int,int> mii;


int t,n,m,x,y;
string s;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout); 

	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++)
	{
		printf("Case #%d: ",tc);

		int ans=0;
		bool a=true;
		cin>>s;
		scanf("%d",&n);
		for(int i=0;i<s.size();i++)
		{
			if(s[i]=='-')
			{
				ans++;
				if(i>s.size()-n)
				{
					printf("IMPOSSIBLE\n");
					a=false;
					break;
				}
				for(int j=i;j<i+n;j++)
				{
					if(s[j]=='-')s[j]='+';
					else s[j]='-';
				}
			}
		}
		if(a)
		{
			printf("%d\n", ans);
		}
	}
	return 0;	
}