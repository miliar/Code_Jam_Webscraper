#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

typedef long long int lli;

int main()
{
	int tt; cin >> tt;
	for(int ta=1;ta<=tt;++ta)
	{
		cout << "Case #" << ta << ":";
		
		int p; cin >> p;
		vector<lli> inp(p), ic(p);
		for(int i=0;i<p;++i)
			cin >> inp[i];
		for(int i=0;i<p;++i)
			cin >> ic[i];
		lli inpsum=0;
		for(int i=0;i<p;++i)
			inpsum+=ic[i];
		
		map<lli,lli> m;
		for(int i=0;i<p;++i)
			m[inp[i]-inp[0]]=ic[i];
		
		vector<lli> resp;
		map<lli,lli> curset;
		curset[0]=1; m[0]--; if(m[0]==0) m.erase(0);
		while(!m.empty())
		{
			int next=m.begin()->first;
			resp.push_back(next);
			for(map<lli,lli>::iterator it=curset.begin();it!=curset.end();++it)
			{
				m[next+it->first]-=it->second;
				if(m[next+it->first]==0)
					m.erase(next+it->first);
			}
			for(map<lli,lli>::reverse_iterator it=curset.rbegin();it!=curset.rend();++it)
			{
				curset[next+it->first]+=it->second;
			}
		}
		
		vector<lli> negs;
		lli negsum=-inp[0];
		for(int i=resp.size()-1;negsum>0;--i)
		{
			if(curset[negsum-resp[i]]>0)
			{
				negs.push_back(resp[i]);
				negsum-=resp[i];
			}
		}
		
		for(int i=0;i<negs.size();++i)
			cout << ' ' << -negs[i];
		int ri=0,ni=negs.size()-1;
		while(ri<resp.size())
		{
			if(ni>=0 && resp[ri]==negs[ni])
			{
				ri++; ni--;
			}
			else
			{
				cout << ' ' << resp[ri];
				ri++;
			}
		}		
		cout << endl;
	}
}
