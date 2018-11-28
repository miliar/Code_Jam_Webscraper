#include<cstdio>
#include<cstdlib>
#include<queue>
#include<cmath> 
#include<cstring> 
#include<map> 
#include<set>
#include<algorithm>

using namespace std;

int a[10010];

typedef struct node {
    int val;
    int id;
}Node;

bool operator > (Node a, Node b)
{
    if(a.val == b.val)return a.id > b.id;
    return a.val > b.val;
}

int main()
{
	freopen("A-large (1).in", "r", stdin);
	freopen("A-large (1).out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; cas ++)
	{
        int n, c;
		scanf("%d%d", &n, &c);
		
		int i, j;
		
		set<Node, greater<Node> >::iterator Item;
		set<Node, greater<Node> > ss;
		
		for(i = 0; i < n; i ++)
		{
            scanf("%d", &a[i]);
        }
        sort(a, a+n);
        
		for(i = 0; i < n; i ++)
		{
            Node b;
            b.val = a[i];
            b.id = i;
            ss.insert(b);
        }
		
		int ans = 0;
		
		for(i = n-1; i >= 0; i --)
		{
            Node b;
            b.val = a[i];
            b.id = i;
            Item = ss.find(b);
            if(Item != ss.end())
            {
                ss.erase(Item);
            }
            else 
            {
                continue;
            }
            b.val = c-a[i];
            b.id = n;
            Item = ss.lower_bound(b);
            if(Item != ss.end())
            {
                ss.erase(Item);
            }
            ans ++;
        }

		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
