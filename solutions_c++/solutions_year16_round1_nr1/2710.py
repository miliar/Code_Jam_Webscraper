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

char s[1005];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
    int T, t = 0;
    scanf("%d", &T);
    
    while(T--)
	{
		deque<char> ret;
		t++;
		printf("Case #%d: ", t);
		scanf("%s", s);
		int N = strlen(s);
		for(int i=0; i<N; i++)
		{
			if(ret.empty() || s[i] >= ret.front())
				ret.push_front(s[i]);
			else ret.push_back(s[i]);
		}
		for(int i=0; i<N; i++)
			printf("%c", ret.front()), ret.pop_front();
		printf("\n");
	}
    
}






