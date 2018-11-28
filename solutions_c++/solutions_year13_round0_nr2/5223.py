#include <iostream>
#include <cstring>
using namespace std;
const int MAXN=100+5;
int n,m,a[MAXN][MAXN],tsts;
int satr[MAXN],soton[MAXN];
int main()
{
	cin >> tsts;
	for(int qq=1;qq<=tsts;qq++)
	{
		cin >> n >> m;
		bool flag=true;
		memset(soton,0,sizeof soton);
		memset(satr,0,sizeof satr);
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
			{
				cin >> a[i][j];
				satr[i]=max(satr[i],a[i][j]);
				soton[j]=max(soton[j],a[i][j]);
			}
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				if(a[i][j]!=satr[i] && a[i][j]!=soton[j])
					flag=false;
		cout << "Case #" << qq << ": " << (flag ? "YES" : "NO") << "\n";
	}
	return 0;
}
