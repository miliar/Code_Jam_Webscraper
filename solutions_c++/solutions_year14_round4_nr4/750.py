#include <cstdio>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <functional>
#include <limits>
#include <cassert>
#include <sstream>
#include <cmath>
#include <string>
#include <fstream>

using namespace std;
typedef long long ll;

const int max_n=10;

int m,n,T;
string s[max_n];
vector<string> SA[10];
bool b[10];
int res=0;
int cnt[100000];
map<vector<string>,int> M;

struct node
{
	node *nxt[26];
	node(){}
	~node()
	{
		for(int i=0; i<26; i++)
			nxt[i]=NULL;
	}
};

void del(node *tmp)
{
	cout<<"D\n";
	for(int i=0; i<26; i++)
		if(tmp->nxt[i]!=NULL)
			del(tmp->nxt[i]);
	cout<<"del\n";
	if(tmp!=NULL)
		delete tmp;
}

void cal()
{
	//cout<<"1\n";
	int ret=0;
	for(int i=0; i<n; i++)
	{
		if(SA[i].size() and !M[SA[i]])
		{
			node *root=new node();
			int c=1;
			//ret++;
			for(int j=0; j<SA[i].size(); j++)
			{
				string X=SA[i][j];
				//cout<<i<<" "<<j<<" "<<X<<endl;
				node *tmp=root;
				for(int k=0; k<X.size(); k++)
				{
					//cout<<i<<" "<<j<<" "<<k<<" "<<X<<endl;
					int x=((char)X[k]-'A');
					if(tmp->nxt[x]==NULL)
					{
						node *newnode=new node();
						tmp->nxt[x]=newnode;
						//ret++;
						c++;
					}
					tmp=tmp->nxt[x];
				}
			}
			M[SA[i]]=c;
			//del(root);
		}
		ret+=M[SA[i]];
	}
	//cout<<ret<<"\n";
	cnt[ret]++;
	res=max(res,ret);
}

void rec(int i, int j)
{
	//cout<<i<<" "<<j<<endl;
	if(i==n-1)
	{
		for(int k=0; k<m; k++)
			if(!b[k])
				SA[i].push_back(s[k]);
		cal();
		for(int k=0; k<m; k++)
			if(!b[k])
				SA[i].pop_back();
		return;
	}

	if(j==m)
	{
		rec(i+1,0);
		return;
	}

	if(!b[j])
	{
		b[j]=1;
		SA[i].push_back(s[j]);
		//cout<<i<<" "
		rec(i,j+1);
		SA[i].pop_back();
		b[j]=0;
		//if(k<m-1)
	}
	rec(i,j+1);
}

int main()
{
	scanf("%d",&T);

	for(int z=0; z<T; z++)
	{
		scanf("%d%d",&m,&n);
		for(int i=0; i<m; i++)
			cin>>s[i];

		fill(cnt,cnt+100000,0);
		fill(b,b+m,0);
		res=0;
		for(int i=0; i<n; i++)
			SA[i].clear();
		rec(0,0);

		printf("Case #%d: %d %d\n",z+1,res,cnt[res]);
	}

	return 0;
}