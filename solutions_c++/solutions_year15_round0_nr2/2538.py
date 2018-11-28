#include <iostream>
#include <vector>

using namespace std;

int res;

int tiempo(vector<int>& v, vector<int>& part)
{
	int rs = 0;
	for(int i=0;i<part.size();i++)
		rs += part[i];
	int mx = 0;
	for(int i=0;i<v.size();i++)
		mx = max(mx,(v[i]+part[i])/(1+part[i]));	// función techo random
	return rs + mx;
}

void rec(vector<int>& v,vector<int>& part,int a)
{
	if(a==part.size())
		res = min(res,tiempo(v,part));
	else
	{
		for(int i=0;i<v[a];i++)
		{
			part[a]=i;
			rec(v,part,a+1);
		}
	}
}

int main()
{
	int T;
	cin >> T;
	for(int I=0;I<T;I++)
	{
		int d;
		cin >> d;
		vector<int> cenas(d);
		for(int i=0;i<d;i++)
			cin >> cenas[i];
		res = 0;
		vector<int> part(d);
		for(int i=0;i<d;i++)
			res = max(res,cenas[i]);
		rec(cenas,part,0);
		cout << "Case #" << I+1 << ": " << res << endl;
	}
}
