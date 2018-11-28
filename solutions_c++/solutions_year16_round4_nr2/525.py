#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <list>
#include <map>
#include <deque>
#include <string>

using namespace std;

int t,T;

#define ULL unsigned long long


void runtestcase()
{	
	vector<double> p;
	int N, K;
	cin >> N >> K;
	for (int n=0;n<N;n++)
	{
		double pp;
		cin >> pp;
		p.push_back(pp);
	}
	sort(p.begin(),p.end());

	double pmax = 0;

	for (int ks=0;ks<=K;ks++)
	{	

	vector<double> q;
	for (int k=0;k<ks;k++)
	{
		q.push_back(p[k]);
	}
	for (int k=N-K+ks;k<=N-1;k++)
	{
		q.push_back(p[k]);
	}
	sort(q.begin(),q.end());

	vector<double> r(K+1);	
	vector<double> r0(K+1);	
	r[0] = 1;
	for (int k=0;k<K;k++)
	{
		r0 = r;
		for (int kk=0;kk<=K;kk++)
		{
			r[kk] = q[k] * (kk>=1 ?  r0[kk-1] : 0) + (1-q[k]) * r0[kk];
		}
	}
	
	pmax = max(pmax, r[K/2]);
	}

	cout << pmax;
}

void main()
{	
	cin >> T;
	for (t = 1; t <= T; t++)
	{
		cerr << t;
		cout << "Case #" << t << ": ";
		runtestcase();
		cout << endl;
	}	
}