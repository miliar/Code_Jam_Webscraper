#include <iostream>
#include <vector>
using namespace std;
#define MAXN 100
#define MAXM 100
int main()
{
	ios_base::sync_with_stdio(0);
	int T,N,M,a;
	cin >> T;
	for(int l=1; l<=T; l++)
	{
		//map<int, pair<int, int> > squares;
		cin >> N >> M;
		vector<pair<int,int> > V[100];
		int maxr[MAXN] = {0};
		int maxc[MAXM] = {0};
		bool ok = true;
		for(int i=0; i<N; i++)
			for(int j=0; j<M; j++)
			{
				cin >> a;
				V[a-1].push_back(make_pair(i,j));
				if(a-1>maxr[i])
					maxr[i] = a-1;
				if(a-1>maxc[j])
					maxc[j] = a-1;
			}
		vector<pair<int,int> >::iterator it;
		for(int i=0; i<100; i++)
		{
			it = V[i].begin();
			while(it != V[i].end() && ok)
			{
				if(maxr[it->first]>i && maxc[it->second]>i)
					ok = false;
				it++;
			}
			if(!ok)
				break;
		}
		cout <<"Case #"<<l<<": ";
		if(ok)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
	
	return 0;
}