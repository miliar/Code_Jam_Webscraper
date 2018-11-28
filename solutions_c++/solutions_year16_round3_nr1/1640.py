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
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
    int T, t = 0;
    scanf("%d", &T);
    
    while(T--)
	{
		t++;
		set<pair<int, int> > S;
		int N;
		
		scanf("%d", &N);
		for(int i=0; i<N; i++)
		{
			int x;
			scanf("%d", &x);
			S.insert(make_pair(-x, i));
		}
		printf("Case #%d:", t);
		while(!S.empty())
		{
			pair<int, int> first, second;
			set<pair<int, int> >::iterator it = S.begin();
			first = *it;
			
			it++;
			second = *it;
			if(S.size() == 2 && second.first == first.first)
			{
				int x = -first.first;
				while(x--)
					printf(" %c%c", first.second+'A', second.second+'A');
				break;
			}
			else
			{
				printf(" %c", first.second+'A');
				S.erase(S.begin());
				first.first++;
				if(first.first)
					S.insert(first);
			}
		}
		printf("\n");
	}
    
}






