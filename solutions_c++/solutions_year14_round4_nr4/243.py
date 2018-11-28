/* by Ashar Fuadi (fushar) */

#include <bits/stdc++.h>

using namespace std;

#define REP(i,n) for (int i = 0, _n = (int)n; i < _n; i++)
#define FOR(i,a,b) for (int i = (int)a, _b = (int)b; i <= _b; i++)
#define RESET(c,v) memset(c, v, sizeof(c))
#define FOREACH(i,c) for (typeof((c).end()) i = (c).begin(); i != (c).end(); ++i)

typedef long long ll;

#define pb push_back
#define mp make_pair

const int oo = 999999999;

int T;
int M, N;
char S[15][15];
int members[15][15];
int cnt[15];
int res, ways;

const int ALPH = 26;
const char OFFSET = 'A';
int NODES;

struct TrieNode
{
	TrieNode* child[ALPH];
	
	TrieNode()
	{
		NODES++;
		REP(i, ALPH)
			child[i] = NULL;
	}
	
	~TrieNode()
	{
		REP(i, ALPH)
			if (child[i])
				delete child[i];
	}
	
	void add(char* s)
	{
		if (!s[0])
			return;
		else
		{
			if (!child[s[0] - OFFSET])
				child[s[0] - OFFSET] = new TrieNode();
				
			child[s[0] - OFFSET]->add(s + 1);
		}
	}
};

void go(int i)
{
	if (i == M)
	{
		bool valid = true;
		REP(j, N)
			if (!cnt[j])
			{
				valid = false;
				break;
			}
		
		if (!valid)
			return;
		
		NODES = 0;
		
		REP(j, N)
		{
			TrieNode* root = new TrieNode();
			REP(k, cnt[j])
				root->add(S[members[j][k]]);
			
			delete root;
		}
		
		if (NODES > res)
		{
			res = NODES;
			ways = 1;
		}
		else if (NODES == res)
			ways++;
		
		return;
	}
	
	REP(j, N)
	{
		members[j][cnt[j]++] = i;
		go(i+1);
		cnt[j]--;
	}
}

int main()
{
	scanf("%d", &T);
	REP(tc, T)
	{
		scanf("%d %d", &M, &N);
		REP(i, M)
			scanf("%s", S[i]);
	
		res = 0;
		ways = 0;
		go(0);
		
		printf("Case #%d: %d %d\n", tc+1, res, ways);
	}
}
