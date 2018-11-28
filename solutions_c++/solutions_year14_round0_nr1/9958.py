#include <iostream>
using namespace std;

const int maxn = 4;

int main()
{
	int n,m,l,i,j,k,p,q;
	int a[maxn+1][maxn+1],b[maxn+1][maxn+1];
	cin >> n;
	for (i=1; i<=n; i++)
	{
		cin >> p;
		for (j=1; j<=maxn; j++)
			for (k=1; k<=maxn; k++)
				cin >> a[j][k];
		cin >> q;
		for (j=1; j<=maxn; j++)
			for (k=1; k<=maxn; k++)
				cin >> b[j][k];
		l=0;
		for (j=1; j<=maxn; j++)
			for (k=1; k<=maxn; k++)
				if (a[p][j]==b[q][k])
				{
					l++;
					m=a[p][j];
					break;
				}
		cout << "Case #" << i << ": ";
		if (l==0) cout << "Volunteer cheated!\n";
		else if (l==1) cout << m << endl;
		else cout << "Bad magician!\n";
	}
}