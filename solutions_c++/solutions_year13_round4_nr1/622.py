#include<iostream>
#include<algorithm>
#include<stack>
using namespace std;

#define MOD 1000002013

struct Node
{
	int pos;
	int type;
	long long cnt;
};

Node node[2010];
int nodeindex;

bool cmp(Node a, Node b)
{
	if(a.pos == b.pos)
	    return a.type < b.type;
	return a.pos < b.pos;
}

long long calprice(long long stations, long long dist)
{
	if(dist == 0)
	    return 0;
	long long a = stations + stations-dist+1;
	long long b = dist;
	if(a % 2 == 0)
	    a /= 2;
	else
	    b /= 2;
	    
	return (a % MOD) * (b % MOD);
}

int main()
{
	freopen("c:\\1.txt","r",stdin);
    freopen("c:\\1-out.txt","w",stdout);
    int T;
    cin>>T;
    for(int caseIndex =1; caseIndex <= T; ++caseIndex)
    {
    	nodeindex = 1;
    	long long stations, stops;
    	cin>>stations>>stops;
    	long long shouldpay = 0;
    	for(int i = 0; i < stops; ++i)
    	{
    		long long start, end, people;
    		cin>>start>>end>>people;
    		shouldpay = (shouldpay + ((calprice(stations, end-start) % MOD) * people) % MOD ) % MOD;
    		node[nodeindex].pos = start;
    		node[nodeindex].type = 0;
    		node[nodeindex++].cnt = people;
    		node[nodeindex].pos = end;
    		node[nodeindex].type = 1;
    		node[nodeindex++].cnt = people;
    	}
    	
    	sort(node, node + nodeindex, cmp);
    	long long reallypay = 0;
    	stack<Node> s;
		for(int i = 0; i < nodeindex; ++i)
    	{
    		if(node[i].type == 0)
    		    s.push(node[i]);
    		if(node[i].type == 1)
    		{
    			long long remain = node[i].cnt;
    			while(remain > 0)
    			{
    				Node cur = s.top();
    				s.pop();
    				long long use = min(remain, cur.cnt);
    				reallypay = (reallypay + (((calprice(stations, node[i].pos - cur.pos) % MOD) * use) % MOD ))%MOD;
    				remain -= use;
    				cur.cnt -= use;
    				if(cur.cnt > 0)
    				    s.push(cur);
    			}
    		}
    	}
    	cout<<"Case #"<<caseIndex<<": ";
    	cout<<(shouldpay-reallypay + MOD) % MOD<<endl;
    }
    return 0;
} 
