#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define rep(i,n) for(int i=0;i<n;i++)
#define MOD 1000002013

using namespace std;

int T;

long long N;
long long M;

struct pass
{
	long long o, e;
	long long num;
	pass(long long io = 0, long long ie = 0, long long p = 0):o(io), e(ie), num(p) { }
};

vector<pass> ps;
vector<pass> confi;

vector< pair<long long, int> > origs;
vector< pair<long long, int> > ees;

long long ret = 0;



void go()
{
	confi.resize(0);
	map<long long, long long> out;
	map<long long, long long> crds;
	out.clear();
	crds.clear();
	int st1 = 0, st2 = 0;
	std::map<long long, long long>::reverse_iterator rit;
	while(!(st1==M && st2==M))
	{
		if (st1!=M && (st2==M || origs[st1].first<=ees[st2].first))
		//if (st2!=N && (st1==N || origs[st1]>ees[st2]))
		{
			if (crds.count(origs[st1].first)>0) crds[origs[st1].first] += ps[origs[st1].second].num;
			else crds[origs[st1].first] = ps[origs[st1].second].num;
			if (out.count(ps[origs[st1].second].e)>0) out[ps[origs[st1].second].e] += ps[origs[st1].second].num;
			else out[ps[origs[st1].second].e] = ps[origs[st1].second].num;
			st1++;
		}
		else
		{
			long long outtime = ees[st2].first;
			for (rit=crds.rbegin(); rit!=crds.rend(); ++rit)
			{
				if (out[outtime]==0) break;
				if (out[outtime]>=(*rit).second)
				{
					confi.push_back(pass((*rit).first, outtime, (*rit).second));
					out[outtime] -= (*rit).second;
					(*rit).second = 0;
				}
				else
				{
					confi.push_back(pass((*rit).first, outtime, out[outtime]));
					(*rit).second -= out[outtime];
					out[outtime] = 0;
				}
			}
			st2++;
		}
	}
}

int main()
{
    fstream fin("A-large.in",ifstream::in);
    fstream fout("A-large.out",ofstream::out);
    fin >> T;
	for(int tc=1;tc<=T;tc++)
    {
        cout << tc << "\n";
		fin >> N;
		fin >> M;
		long long t1 = 0, t2 = 0, t3 = 0;
		ps.resize(0);
		origs.resize(0);
		ees.resize(0);
		rep(i,M)
		{
			fin >> t1 >> t2 >> t3;
			ps.push_back(pass(t1, t2, t3));
			origs.push_back(make_pair(t1, i));
			ees.push_back(make_pair(t2, i));
		}
		sort(origs.begin(), origs.end());
		sort(ees.begin(), ees.end());
		ret = 0;
		go();
		long long ret1 = 0, ret2 = 0;
		long long tn1 = 0, tn2 = 0, tn3 = 0;
		rep(i, ps.size())
		{
			if (ps[i].e!=ps[i].o)
			{
				tn1 = N + (N-(ps[i].e-ps[i].o+1));
				tn2 = ps[i].e-ps[i].o;
				if (tn1 & 1ll) tn2 /= 2;
				else tn1 /= 2;
				tn3 = ((tn1%MOD)*(tn2%MOD))%MOD;
				tn3 *= ps[i].num;
				tn3 %= MOD;
				ret1 = (ret1 + tn3)%MOD;
			}
		}
		rep(i,confi.size())
		{
			if (confi[i].e!=confi[i].o)
			{
				tn1 = N + (N-(confi[i].e-confi[i].o+1));
				tn2 = confi[i].e-confi[i].o;
				if (tn1 & 1ll) tn2 /= 2;
				else tn1 /= 2;
				tn3 = ((tn1%MOD)*(tn2%MOD))%MOD;
				tn3 *= confi[i].num;
				tn3 %= MOD;
				ret2 = (ret2 + tn3)%MOD;
				//ret1 = (ret1 + ((tn1%MOD)*(tn2%MOD))%MOD)%MOD;
			}
		}
		long long ret = ret1 - ret2;
		if (ret<0) ret += MOD;
		fout << "Case #" << tc << ": " << ret << "\n";
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC << "\n";
    //system("PAUSE");
    return 0;
}
