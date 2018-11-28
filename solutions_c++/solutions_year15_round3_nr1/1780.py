#include<bits/stdc++.h>
using namespace std;

typedef vector<vector<int> > vii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long LL;

#define sz size()
#define all(n) n.begin(),n.end()
#define clr(a,n) memset(a,n,sizeof(a))
#define pb push_back
#define fo(i,j) for(int i=0;i<j;i++)
#define foreach(it, c) for (__typeof(c.begin()) it = c.begin(); it != c.end(); ++it)

int main()
{
	freopen("A-small-attempt2.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T, k = 0;
    scanf("%d",&T);
    
    while(T--)
    {
		k++;
		int ret = 0;
		int R, C, L;
		scanf("%d %d %d",&R,&C,&L);
		ret += R*(C/L + (bool)(C%L));
		ret += L-1;
		//if(L <= 2 || L == C) ret--;
		printf("Case #%d: %d\n",k,ret);
	}
}






