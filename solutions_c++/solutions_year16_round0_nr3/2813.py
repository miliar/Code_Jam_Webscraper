#include<fstream>
#include<vector>
#include<string>
#include<map>
using namespace std;

int N, J, total;
map<vector<int>, vector<long long> > mp;

long long get_from_base(const vector<int>& v, int base)
{
	int len = v.size();
	long long nr = 0;	
	long long pw = 1;
	
	for(int i = len - 1;i >= 0;--i)
	{
		nr += v[i] * pw;
		pw *= base;
	}
	
	return nr;
}

long long get_div(long long nr)
{
	for(long long i = 2;i * i <= nr;++i)
	{
		if(nr % i == 0)
		{
			return i;
		}
	}
	
	return -1;
}

void eval(const vector<int>& v)
{
	vector<long long> divs;
	
	for(int i = 2;i <= 10;++i)
	{
		long long nr = get_from_base(v, i);
		long long div = get_div(nr);
		
		if(div == -1)
		{
			return;
		}
		else
		{
			divs.push_back(div);
		}
	}
	
	mp[v] = divs;
	++total;
}

bool gen(int k, vector<int>& v)
{
	if(k == N)
	{
		v.push_back(1);
		eval(v);
		v.pop_back();
		if(total == J)
		{
			return true;
		}
		return false;
	}
	
	v.push_back(0);
	bool rez = gen(k + 1, v);
	if(rez)
	{
		return true;
	}
	v.pop_back();
	v.push_back(1);
	
	rez = gen(k + 1, v);
	if(rez)
	{
		return true;
	}
	v.pop_back();
	
	return false;
}

int main()
{
	ifstream in("C.in");
	ofstream out("C.out");
	
	int t;
	
	in >> t;
	in >> N >> J;
	
	N -= 2;
	vector<int> v;
	v.push_back(1);
	
	gen(0, v);
	map<vector<int>, vector<long long> >::iterator it = mp.begin();
	
	out<<"Case #1: \n";
	for(;it != mp.end();++it)
	{
		vector<int> v1 = it->first;
		
		for(int i = 0;i < (int) v1.size();++i)
		{
			out<<v1[i];
		}
		out<<" ";
		vector<long long> v2 = it->second;
		
		for(int i = 0;i < (int) v2.size();++i)
		{
			out<<v2[i]<<" ";
		}
		out<<"\n";
	}
	
	in.close();
	out.close();
}
