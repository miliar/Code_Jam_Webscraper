#include <bits/stdc++.h>
using namespace std;
std::set< pair<int,int> > V;
set< pair<int,int> > :: iterator it1,it2,it,it3;
int Ans[1010][1010];
#define inf (1<<30)
void Generate()
{
	int cnt = 0;
	V.insert(make_pair(0,1));
	V.insert(make_pair(1,1));
	Ans[1][1] = 0;
	Ans[0][1] = inf;
	while(1)
	{
		int l = V.size();
		int i = 0, j = 0;
		for(i = 0,it1 = V.begin();i<l;i++,it1++)
		{
			for(j = i,it2 = it1;j<l;j++,it2++)
			{
				int v1 = it1->first;
				int v2 = it1->second;
				int v3 = it2->first;
				int v4 = it2->second;
				int val1 = it1->first*it2->second + it1->second*it2->first;
				int val2 = it1->second*it2->second*2;
				int g = __gcd(val1,val2);
				val1/=g;
				val2/=g;
				int val = min(Ans[v1][v2],Ans[v3][v4]) + 1;
				if(val2>1000)
					continue;
				V.insert(make_pair(val1,val2));
				if(Ans[val1][val2]==-1)
					Ans[val1][val2] = val;
				Ans[val1][val2] = min(Ans[val1][val2],val);
			}
		}
		if(l==V.size())
			break;
	}
}
int main()
{
	int Testcases;
	memset(Ans,-1,sizeof(Ans));
	Generate();
	ios_base::sync_with_stdio(false);
	cin>>Testcases;
	int N = Testcases;
	while(Testcases--)
	{
		cout<<"Case #"<<N - Testcases<<": ";
		string str,res;
		cin>>str;
		int found = str.find("/");
		res = str.substr(0,found);
		str = str.substr(found+1);
		int P = atoi(res.c_str());
		int Q = atoi(str.c_str());
		int g = __gcd(P,Q);
		P/=g;
		Q/=g;
		if((Q&(Q-1))!=0)
			cout<<"impossible"<<endl;
		else
		{
			int F = 0;
			if(Ans[P][Q]==-1||Ans[P][Q]==inf)
				cout<<"impossible"<<endl;
			else
				cout<<Ans[P][Q]<<endl;
		}
	}
	return 0;
}