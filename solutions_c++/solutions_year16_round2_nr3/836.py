#include <iostream>
#include <set>
#include <vector>
#define parka pair<string, string>
#define st first
#define nd second
using namespace std;
void process(vector<parka > v);
bool dasie(vector<parka> v, int k);
int sumBits(int k);
int main()
{
	ios_base::sync_with_stdio(0);
	int ilez;
	cin>>ilez;
	for(int aa=0; aa<ilez; aa++)
	{
		cout<<"Case #"<<aa+1<<": ";
		
		int n;
		cin>>n;
		vector<parka> vec;
		string tmpa, tmpb;
		for(int i=0; i<n; i++)
		{
			cin>>tmpa>>tmpb;
			vec.push_back(make_pair(tmpa, tmpb));
		}
		process(vec);
		
		cout<<endl;
	}
}
void process(vector<parka> v)
{
	int wynik=0;
	for(int k=0; k<(1<<v.size()); k++)
	{
		if(dasie(v, k))
		{
			wynik=max(wynik, sumBits(k));
		}
	}
	cout<<wynik;
}
bool dasie(vector<parka> v, int k)
{
	set<string> a;
	set<string> b;
	for(int i=0; i<v.size(); i++)
	{
		if(!(k&(1<<i)))
		{
			a.insert(v[i].st);
			b.insert(v[i].nd);
		}
	}
	for(int i=0; i<v.size(); i++)
	{
		if((k&(1<<i)))
		{
			if(a.count(v[i].st)==0)
				return 0;
			if(b.count(v[i].nd)==0)
				return 0;
		}
	}
	return 1;
}
int sumBits(int k)
{
	int ret=0;
	for(int i=0; i<20; i++)
	{
		if(k&(1<<i))
			ret++;
	}
	return ret;
}
