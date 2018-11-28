#include<bits/stdc++.h>

#define repi(n) for(int i=0;i<(n);++i)
#define repj(n) for(int j=0;j<(n);++j)
#define repr(i,m,n) for(int i=(m);i<=(n);++i)
#define rep1i(n) for(int i=1;i<=(n);++i)
#define sz(a) int((a).size)
#define pb(v) push_back(v)
#define mp(a,b)	make_pair((a),(b))
#define all(v) (v).begin(),(v).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i!=(c).end();++i)
#define pre(c,v) ((c).find()!=(c).end)
#define vpre(c,v) (find(all(c))!=(c).end())
#define nl cout<<endl

#define fi first
#define sec second

using namespace std;

typedef long long int ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vii;
typedef vector<vl> vll;
typedef pair<int,int> ii;

string a;

void call(string& s,string tmp,int id)
{
	string tmp1 = tmp + s.substr(id,1);
	string tmp2 = s.substr(id,1) + tmp;
	string val;
	if(s[id]>tmp[0])
	{
		val = tmp2;
	}
	else if(s[id]<tmp[0])
	{
		val = tmp1;
	}
	else
	{
		int idx = 0;
		while(idx<tmp.size() && tmp[idx]==s[id])
		{
			++idx;	
		}
		if(idx==tmp.size())
			val = tmp1;
		else
		{
			if(s[id]>tmp[idx])
			{
				val = tmp2;
			}
			else
			{
				val = tmp1;
			}
		}
	}
//	cout << id << " " << val <<" "<< s.size()-1  << endl;
	if(id==(s.size()-1))
	{
		a = val;
		return;
	}
	call(s,val,id+1);
}

string fun(string& s)
{
	if(s.size()==1)
		return s;
	string tmp(s.substr(0,1));
	call(s,tmp,1);
//	sort(all(a));
	return a;
}

int main()
{
	
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int test;
	cin >> test;
	for(int cs=1;cs<=test;++cs)
	{
//		a.clear();
		string s;		
		cin >> s;
		cout << "Case #" << cs <<": " << fun(s) << endl;
	}

  	return 0;
}

