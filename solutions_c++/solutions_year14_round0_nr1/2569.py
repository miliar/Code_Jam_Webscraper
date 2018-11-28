#include <iostream>
#include <cstdio>

using namespace std;

int main ()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("t1.out","w",stdout);
	
	int i,j,n,m,t,tt;
	int s[17],a[5][5],b[5][5];
	cin >> t;
	for (tt=1; tt<=t; tt++)
	{
		for (i=1; i<=16; i++) s[i]=0;
		cin >> n;
		for (i=1; i<=4; i++)
		for (j=1; j<=4; j++) cin >> a[i][j];
		cin >> m;
		for (i=1; i<=4; i++)
		for (j=1; j<=4; j++) cin >> b[i][j];
		for (i=1; i<=4; i++)
		{
			s[a[n][i]]++;
			s[b[m][i]]++;
		}
		int cnt=0,ans;
		for (i=1; i<=16; i++)
		{
			if (s[i]>=2)
			{
				cnt++;
				ans=i;
			}
		}
		cout << "Case #" << tt << ": ";
		if (cnt==1) cout << ans << endl;
		if (cnt<1) cout << "Volunteer cheated!" << endl;
		if (cnt>1) cout << "Bad magician!" << endl; 
	} 
	
	return 0;
}
