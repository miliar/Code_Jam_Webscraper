#include <iostream>
#include <vector>
using namespace std;

int count(vector<vector<int> >& md,vector<int>& sal, int bs, int ts, int n)
{
	if(sal[n]<bs || sal[n]>ts) return 0;
	int resp=1;
	for(int i=0;i<md[n].size();++i)
		resp+=count(md,sal,bs,ts,md[n][i]);
	return resp;
}

int main()
{
	int tt; cin >> tt;
	for(int ta=1;ta<=tt;++ta)
	{
		cout << "Case #" << ta << ": ";
		
		int n, d;
		cin >> n >> d;
		vector<vector<int> > md(n);
		vector<int> sal(n);
		int si,as,cs,rs;
		int mi,am,cm,rm;
		cin >> si >> as >> cs >> rs;
		cin >> mi >> am >> cm >> rm;
		sal[0]=si;
		for(int i=1;i<n;++i)
		{
			si = (si*as+cs)%rs;
			mi = (mi*am+cm)%rm;
			md[mi%i].push_back(i);
			sal[i] = si;
		}
		
		int best=0;
		for(int bs=sal[0]-d;bs<=sal[0];++bs)
		{
			int c=count(md,sal,bs,bs+d,0);
			best = max(c,best);
		}
		cout << best << endl;
	}
}
