#include <bits/stdc++.h>
 
using namespace std;
 
#define      pii               std::pair<int,int>
#define      vi                std::vector<int>
#define      mp(a,b)           std::make_pair(a,b)
#define      X                 first
#define      Y                 second
#define      pb(x)             push_back(x)

typedef long long LL;
LL MOD = 1000000007;
struct fuck
{
	int sign;
	char c;
};
char A[4][4]= {{'h','i','j','k'},
			   {'i','h','k','j'},
			   {'j','k','h','i'},
			   {'k','j','i','h'}};
int sgn[4][4] = {{0,0,0,0},
				 {0,1,0,1},
				 {0,1,1,0},
				 {0,0,1,1}};

fuck cacl(char x , char y)
{
	return (fuck){sgn[x-'h'][y-'h'],A[x-'h'][y-'h']};
}
int main()
{
	
	int t;
	scanf("%d",&t);
	char s[100000];
	for(int tc = 1;tc <= t;tc++)
	{
		int n , l;
		scanf("%d%d",&n,&l);
		scanf("%s",s);
		string S = "",S1=s;
		for(int i=0;i<l;i++)
		{
			S += S1;
		}
		for(int i=0;i<S.size();i++)
		{
			s[i] = S[i];
		}
		n = n*l;
		int i = 0;
		int cur_sgn = 0;
		char cur_char = s[0];
		for(i=1;i<n;i++)
		{
			if(cur_char=='i' && (cur_sgn%2==0)) break;
			fuck x = cacl(cur_char,s[i]);
			cur_sgn += x.sign;
			cur_char = x.c;
		}
		int k = n-2;
		cur_sgn = 0;
		cur_char = s[n-1];
		for(k=n-2;k>=0;k--)
		{
			if(cur_char=='k' && (cur_sgn%2==0)) break;
			fuck x = cacl(s[k],cur_char);
			cur_sgn += x.sign;
			cur_char = x.c;
		}
		cur_sgn = 0;
		cur_char = s[i];
		for(int j = i+1; j<=k ;j++)
		{
			fuck x = cacl(cur_char,s[j]);
			cur_sgn += x.sign;
			cur_char = x.c;
		}
		if(i<=k && (cur_sgn%2 ==0) && cur_char =='j') printf("Case #%d: YES\n", tc);
		else printf("Case #%d: NO\n", tc);
	}	
	return 0;
}
