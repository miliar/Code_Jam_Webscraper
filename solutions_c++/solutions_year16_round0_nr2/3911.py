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

char s[102];

int main()
{
    freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T, t = 0;
	scanf("%d", &T);
	while(T--)
	{
		t++;
		scanf("%s", s);
		int L = strlen(s), ch = 0;
		for(int i=1; i<=L; i++)
			if(s[i] != s[i-1])
				ch++;
		if(s[L-1] == '+') ch--;
		
		printf("Case #%d: %d\n", t, ch);
	}
}






