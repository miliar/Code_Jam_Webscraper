// c.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <map>
#include <utility>
#include <algorithm>
//#include <cmath>
#include <cstdlib>

using namespace std;

#define fori(i_,f_,t_) for(int i_=f_;i_<t_;++i_)
#define fore(i_,c_) for(auto i_=c_.begin();i_!=c_.end();++i_)
#define pb	push_back

typedef unsigned int ui32;
vector<ui32> mem;
vector<int> sol;
vector<int> kt;
vector<int> chk;
vector<vector<int>> chks;

int N;
bool solve(int r, ui32 cs)
{
	ui32 b = 1;
	fori(n,0,N)
	{
		if ((cs & b)==0 && kt[chk[n]]>0 && mem[cs | b]==0)
		{
			kt[chk[n]] -=1;
			fore(pk,chks[n])
			{
				kt[*pk] +=1;
			}
			if (r==(N-1) || solve(r+1,cs | b))
			{
				sol[r]=n+1;
				return true;
			}

			kt[chk[n]] +=1;
			fore(pk,chks[n])
			{
				kt[*pk] -=1;
			}
			mem[cs | b]=1;
		}
		b<<=1;
	}
	return false;
}

int main(int argc, char* argv[])
{
	int T;
	kt.resize(200);
	cin>>T;
	fori(t,0,T)
	{

		cout<<"Case #"<<t+1<<":";
		int K;
		cin>>K>>N;
		mem.resize(1<<N);
		fill(mem.begin(),mem.end(),0);
		sol.resize(N);
		fill(kt.begin(),kt.end(),0);
		chk.resize(N);
		chks.clear();
		fori(k,0,K)
		{
			int a;
			cin>>a;
			kt[a] +=1;
		}

		fori(n,0,N)
		{
			int a;
			cin>>a;
			chk[n]=a;
			int I;
			cin>>I;
			vector<int> ki(I);
			fori(i,0,I)
				cin>>ki[i];
			chks.push_back(ki);
		}

		if (solve(0,0))
		{
			fore(ci,sol)
			{
				cout<<" "<<*ci;
			}
		} else
			cout<<" IMPOSSIBLE";
        cout<<std::endl;
	}

	return 0;
}

