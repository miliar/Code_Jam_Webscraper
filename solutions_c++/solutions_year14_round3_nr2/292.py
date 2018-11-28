#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define MP make_pair
#define pb push_back
#define inf 1000000000
#define   M 1000000007

typedef long long  LL;
typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

LL gcd(LL a,LL b)
{
	if(b==0) return a;
	return gcd(b,a%b);
}

LL modexp(LL a,LL b)
{
	if(b==0) return 1;
	if(b%2) return ((a%M)*modexp(a,b-1))%M;
	LL q=modexp(a,b/2);
	return (q*q)%M;
}

LL fact[105];
string cars[105];

int same[30];


int isvalid(string s,int x)
{
	int i,oc=0,n=s.size();
	int a=s[0]-'a', b=s[n-1]-'a';

	for(i=0;i<s.size();i++)
	{
		int d=s[i]-'a';
		if( i && s[i]!=s[i-1] && (oc&(1<<d))) return 0;
		oc|=(1<<d);
	}
	if(a==b && x)
	{
		same[a]++;
		return 2;

	}
	
	return 1;
}

int solve(int n)
{
	int arr[14],i,ans=0;

	for(i=0;i<n;i++) arr[i]=i;
	do
	{

		string s;
		for(i=0;i<n;i++) s+=cars[arr[i]];
		if(isvalid(s,0)) ans++;
	}while(next_permutation(arr,arr+n));
	return ans;
}

int main()
{
	int n,m,i,j,k,tests,cs=0;

	 freopen("D:\\GCJ2\\B-small-attempt2.in","r",stdin);
	 freopen("D:\\GCJ2\\B-small-attempt2.txt","w",stdout);

	fact[0]=1;
	for(i=1;i<=100;i++) fact[i]=(fact[i-1]*i)%M;

	scanf("%d",&tests);
	while(tests--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			cin>>cars[i];
		LL ans=0;

	
		//LL res=solve(n);printf("Case #%d: %lld\n",++cs,res);

		//puts("h");continue;
		int ok=1;

		//printf("%d %s\n",n,cars[i].c_str());

		vector<string> now;

		MEM(same,0);
		for(i=0;i<n;i++)
		{
			int q=isvalid(cars[i],1);
			if(q==0) ok=0;
			if(q==1)
			{
				now.pb(cars[i]);
				//cout<<cars[i]<<endl;
			}
			else
			{

			}
		}
		//continue;

		while(ok)
		{	
			int a=-1,b=-1;
			for(i=0;i<now.size() && a<0;i++)
				for(j=i+1;j<now.size() && a<0;j++)
				{
					int l1=now[i].size();
					int l2=now[j].size();

					if(now[i][l1-1]==now[j][0])
					{
						a=i;
						b=j;
					}
					else if(now[i][0]==now[j][l2-1])
					{
						a=j;
						b=i;
					}
				}

			if(a<0) break;
			vector<string> tmp;

			for(i=0;i<now.size();i++)
			{
				if(i==a || i==b) continue;
				tmp.pb(now[i]);
			}
			tmp.pb(now[a]+now[b]);
			now=tmp;
			//printf("==%s\n",now[a]+now[b]);
		}
		

		string str;


		for(i=0;i<now.size();i++)
			str+=now[i];

		int oc=0;
		for(i=0;i<str.size();i++)
		{
			int d=str[i]-'a';
			oc|=(1<<d);
		}
		
		//printf("%d\n",now.size());

		int cnt=0;
		LL q=1;

		for(i=0;i<26;i++)
		{
			if(same[i]==0) continue;
			int has=0;

			q=(q*fact[same[i]])%M;

		
/*			for(j=0;j<now.size();j++)
			{
				int l=now[j].size();
				//printf("=%c %c %c\n",now[j][0],now[j][l-1],i+'a');
				if(now[j][0]==i+'a' || now[j][l-1]==i+'a')
					has=1;
			}*/
			

			if(!(oc&(1<<i)))
			{
				str+=(char)(i+'a');
				//printf("%c\n",i+'a');
				cnt++;
			}
				
		}
		
		//printf("=%s %d\n",str.c_str(),ok);
		
		if(str.size() && !isvalid(str,0)) ok=0;
		//printf("=%d\n",ok);

		//printf("=%s\n",str.c_str());
		int tot=(int)now.size() + cnt;

		q=(q*fact[tot])%M;

		ans = ok ? q : 0;

		printf("Case #%d: %lld\n",++cs,ans);

	}
	return 0;
}