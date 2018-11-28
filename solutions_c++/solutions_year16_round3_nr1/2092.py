#include<bits/stdc++.h>
using namespace std;
#define  mp make_pair
#define  pb push_back
#define fi first
#define se second
#define inf 99999999LL
#define  M 1000000007
#define PI 3.1415926535897932
typedef long long int ll;
int tt=1;
int main()
{
	int i,j,t;
	scanf("%d",&t);
	while(t--)
	{
		int n;
		scanf("%d",&n);
		int a[n+5];
		set<pair<int,char> >s;
		int ss=0;
		for(i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			ss+=a[i];
			s.insert(mp(a[i],'A'+i));
		}
		printf("Case #%d: ",tt++);
		if(ss%2!=0)
		{
			set<pair<int,char> > ::iterator it=s.end();
			it--;
			printf("%c ",(it->second));
			if((it)->first>1)
				s.insert(mp(((it)->first)-1,(it)->second));
				s.erase(it);	
		}
		while(!s.empty())
		{
			set<pair<int,char> > ::iterator it=s.end();
			it--;
			printf("%c",(it->second));
			if((it)->first>1)
				s.insert(mp(((it)->first)-1,(it)->second));
			s.erase(it);
			if(!s.empty())
			{
				it=s.end();
				it--;
				printf("%c ",(it->second));
				if((it)->first>1)
					s.insert(mp(((it)->first)-1,(it)->second));
				s.erase(it);
			}
		}
		cout<<endl;
	}
	return 0;
}