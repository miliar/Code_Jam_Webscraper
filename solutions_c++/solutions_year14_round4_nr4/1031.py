#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
using namespace std;

struct Fenwick
{
	typedef pair<int,int> PII;
	vector<PII> ACT;
	vector<int> ALL;
	Fenwick(int N){
		ALL = vector<int>(N+10);
	}
	void ins(int x,int v)
	{
		ACT.push_back(PII(x,v));
		x++;
		while(x < int(ALL.size()))
		{
			ALL[x] += v;
			x += x & -x;
		}
	}
	int get(int x)
	{
		x++;
		int ret = 0;
		while(x > 0)
		{
			ret += ALL[x];
			x -= x & -x;
		}
		return ret;
	}
	void clear()
	{
		vector<PII> C = ACT;
		for(int i = 0; i < (int)C.size(); ++i)
		{
			ins(C[i].first , -C[i].second);
		}
		ACT.clear();
	}
};
Fenwick F(2000);
void normalize(vector<int> &V)
{
	set<int> S;
	for (int i = 0; i < V.size(); ++i)
		S.insert(V[i]);
	map<int,int> M; int idx = 0;
	for(set<int>::iterator it = S.begin() ; it!=S.end(); ++it)
		M[*it] = idx++;
	for(int i = 0; i < V.size(); ++i)
		V[i] = M[V[i]];
}


int nOI(int lo,int hi, vector<int> &V)
{
	F.clear();
	int cnt = 0;
	for(int i = lo ; i <= hi; ++i)
	{
		cnt += F.get(V[i]);
		F.ins(V[i],1);
	}
	return cnt;
}

int BF(int m, vector<int> V)
{
	int cnt = 0;
	for(int i = 0; i < m; ++i)
	{
		for(int j = 0; j+1 < m; ++j)
			if(V[j] > V[j+1])
			{
				swap(V[j],V[j+1]);
				cnt++;
			}
	}
	for(int i = m; i < V.size(); ++i)
	{
		for(int j = m; j+1 < V.size(); ++j)
			if(V[j] < V[j+1])
			{
				swap(V[j],V[j+1]);
				cnt++;
			}
	}
	return cnt;
	
}


int cntNodes(int mask,vector<string> V)
{
	set<string> S;
	for(int i = 0; i < V.size(); ++i)
		if((1<<i) & mask)
		{
			for(int j = 0; j < (int)V[i].size(); ++j)
				S.insert(V[i].substr(0,j+1));
		}
	return S.size() + 1;	
}
typedef pair<int,int> PII;
PII getMax(int used , int S , vector<string> V)
{
	PII r;
	if(S == 1)
	{
		int tot = 1<<V.size();
		tot--;
		if(tot == used)return PII(-100000000,0);
		return PII(cntNodes(tot - used , V) , 1);
	}
	PII ma = PII(0,0);
	for(int i = 1; i < (1<<V.size()); ++i)
	{
		if(used & i)continue;
		PII t = getMax(used ^ i , S-1,V);
		t.first += cntNodes(i,V);
		if(ma.first == t.first)
			ma.second += t.second;
		else if(ma.first < t.first)
			ma = t;
	}
	return ma;
}

int main () 
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int TC;
	cin >> TC;
	for(int tc = 1 ; tc<=TC;  ++tc)
	{
		int M,N;
		cin >> M >> N;
		vector<string> V(M);
		for (int i = 0; i < M; ++i) {
			cin >> V[i];
		}
		PII a = getMax(0,N,V);
		cout << "Case #" << tc << ": " << a.first << " " << a.second << endl;
		
	}
}


