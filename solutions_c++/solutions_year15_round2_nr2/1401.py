#include <iostream>
#include <vector>
using namespace std;

bool a[16][16]={0};
int n,r,c;

pair<int, int> NextNode(int row, int col)
{
	pair<int, int> ret ;
	ret.first = row;
	ret.second = col;
	ret.second ++;
	if(ret.second == c)
	{
		ret.first++;
		ret.second = 0;
	}
	return ret;
}

int f(int row, int col, int m)
{
	if(row == r )
		if(m==n) return 0;
		else return (1<<30);
	pair<int, int> nextNode = NextNode(row, col);
	a[row][col] = 0;
	int ret = f(nextNode.first, nextNode.second, m);
	if(m < n)
	{
		a[row][col] = 1;
		int cnt = 0;
		if(row > 0 && a[row-1][col] == 1) cnt++;
		if(col > 0 && a[row][col-1] == 1) cnt++;
		ret = min(ret, f(nextNode.first, nextNode.second, m+1) + cnt);
	}
	return ret;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tnum;
	cin>>tnum;
	for(int q=1;q <= tnum;q++)
	{
		cin>> r >> c >> n;

		cout << "Case #" << q << ": " << f(0,0,0) << endl;
	}
}