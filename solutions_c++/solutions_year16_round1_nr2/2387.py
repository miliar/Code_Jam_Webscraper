#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int> > mapa, mapb, lis;
int n;
vector<int> zero, ansv;
int check(const vector<vector<int> >& map, int c, int k)
{
	for(int i = 0; i < n; i++) if(map[i][c])
	{
		if(map[i][c] != lis[k][i])
			return map[i][c] - lis[k][i];
	}
	return 0;
}
void print()
{
	cout << "-----------map A------------\n";
	for(int i = 0; i < n; i++, cout << endl)
		for(int j = 0; j < n; j++)
			cout << mapa[i][j] << ' ';
	cout << "-----------map B------------\n";
	for(int i = 0; i < n; i++, cout << endl)
		for(int j = 0; j < n; j++)
			cout << mapb[j][i] << ' ';
}
bool search(int k, int aa, int bb, bool skip)
{
	int res;
	if(k == lis.size())
	{
		bool flag = false;
		for(int i = 0; i < n; i++)
			if(!mapa[i][0])
			{
				flag = true;
				for(int j = 0; j < n; j++)
					ansv[j] = mapb[j][i];
				break;
			}
		if(!flag)
		for(int i = 0; i < n; i++)
			if(!mapb[i][0])
			{
				for(int j = 0; j < n; j++)
					ansv[j] = mapa[j][i];
				break;
			}
		return true;
	}
	// cout << k;
	// print();
	if(bb < n){
		if((res = check(mapa, bb, k)) == 0){
			swap(mapb[bb], lis[k]);
			// mapb[bb] = lis[k];
			if(search(k+1, aa, bb + 1, skip)) return true;
			swap(mapb[bb], lis[k]);
			// mapb[bb] = zero;
			// cout << res<<endl;
		}
		if(res < 0 && !skip && bb + 1 < n){
			if(!check(mapa, bb + 1, k)){
				swap(mapb[bb+1], lis[k]);
				// mapb[bb+1] = lis[k];
				if(search(k+1, aa, bb + 2, true)) return true;
				swap(mapb[bb+1], lis[k]);
				// mapb[bb+1] = zero;
			}
		}
	}
	if(aa < n){
		if((res = check(mapb, aa, k)) == 0){
			swap(mapa[aa], lis[k]);
			// mapa[aa] = lis[k];
			if(search(k+1, aa + 1, bb, skip)) return true;
			swap(mapa[aa], lis[k]);
			// mapa[aa] = zero;
		}
		if(res < 0 && !skip && aa + 1 < n){
			if(!check(mapb, aa + 1, k)){
				swap(mapa[aa+1], lis[k]);
				// mapa[aa+1] = lis[k];
				if(search(k+1, aa + 2, bb, true)) return true;
				swap(mapa[aa+1], lis[k]);
				// mapa[aa+1] = zero;
			}
		}
	}
	return false;
}

int main()
{
	int T, start;
	cin >> T;
	for(int kase = 1; kase <= T; kase++)
	{
		cin >> n;
		int nn = n*2 -1;
		lis.clear();
		lis.resize(nn);
		for(int i = 0; i < nn; i++)
		{
			lis[i].resize(n, 0);
			for(int j = 0; j < n; j++)
				cin >>lis[i][j];
		}
		mapa.clear();
		mapb.clear();
		zero.resize(n, 0);
		ansv = zero;
		mapa.resize(n, zero);
		mapb.resize(n, zero);
		sort(lis.begin(), lis.end(),
		[](const vector<int>& a, const vector<int>& b) -> bool{
			for(int i = 0; i < a.size(); i++)
				if(a[i] != b[i])
					return a[i] < b[i];
		});
		swap(mapa[0], lis[0]);
		start = 1;
		if(mapa[0][0] == lis[1][0]){
			swap(mapb[0], lis[1]);
			start = 2;
		}
		search(start, 1, start - 1, false);
		// print();
		cout<<"Case #" << kase << ": ";
		for(int i = 0; i < n; i++)
			cout << ansv[i] << ' ';
		cout << endl;
	}
	return 0;
}