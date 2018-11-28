#include<bits/stdc++.h>
using namespace std;
#define MAXN 5
bool adj[MAXN][MAXN];
vector<int> order;
bool usato[MAXN];
int N,delta,sol;

bool prova(int i)
{
	if(i==N)
		return true;

	int n = order[i];
	bool once = false;
	for(int j=0;j<N;++j)
		if(adj[n][j] && !usato[j])
		{
			once = true;
			usato[j] = true;
			if(!prova(i+1)) return false;
			usato[j] = false;
		}
	
	return once;
}

void genera(int i, int j)
{
	if(i==N)
	{
		order.clear();
		for(int i=0;i<N;++i)
			order.push_back(i);
		bool ok = true;

		do
		{
			for(int i=0;i<N;++i)
				usato[i]=false;
			ok = ok && prova(0);
		}while(next_permutation(order.begin(), order.end()));


		if(ok)
			sol = min(sol, delta);
		return;
	}

	int a,b;
	if(j==N-1)
		a=i+1,b=0;
	else a=i, b=j+1;

	genera(a,b);

	if(!adj[i][j])
	{
		adj[i][j] = true;
		delta++;
		genera(a,b);
		adj[i][j] = false;
		delta--;
	}
}

int foo()
{
	cin>>N;
	for(int i=0;i<N;++i)
	{
		string r;
		cin>>r;
		for(int j=0;j<N;++j)
			adj[i][j] = (r[j] == '1');
	}

	sol = 50;
	delta = 0;
	genera(0,0);
	return sol;
}

int main()
{
	int T;
	cin>>T;
	for(int i=1;i<=T; ++i)
		cout << "Case #" << i << ": " << foo() << endl;
}
