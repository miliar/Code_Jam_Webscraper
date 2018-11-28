#include <fstream>
#include <cstring>
#include <iostream>

using namespace std;

#define MAXN 100
#define MAXM 100
#define MAXA 100

int a[MAXN+1][MAXM+1];
bool show[MAXA+1];

int main(int argc, char const *argv[])
{
	ifstream in("B-large.in");
	ofstream out("B-large.out");

	int T, N, M, t, i, j, k;
	bool yes;
	in>>T;
	for (t = 1; t <= T; t++)
	{
		in>>N>>M;
		memset(a[0], 0, (M+1)*sizeof(int));
		memset(show, 0, (MAXA+1)*sizeof(bool));
		for (i = 1; i <= N; i++)
		{
			a[i][0] = 0;
			for (j = 1; j <= M; j++)
			{
				in>>a[i][j];
				a[i][0] += a[i][j];
				a[0][j] += a[i][j];
				show[a[i][j]] = true;
			}
		}
		yes = true;
		k = 1;
		int pre;
		while(!show[k]) k++;
		// cout<<"ini k="<<k<<endl;
		while(k <= MAXA && yes)
		{
			for (i = 1; i <= N && yes; i++)
			{
				for (j = 1; j <= M && yes; j++)
				{
					// cout<<"k="<<k<<",a["<<i<<"]["<<j<<"]="<<a[i][j]<<endl;
					if (k == a[i][j] && M*k != a[i][0] && N*k != a[0][j])
					{
						yes = false;
					}
				}
			}
			pre = k++;
			while(k <= MAXA && !show[k]) k++;
			if (yes && k <= MAXA)
			{
				
				for (i = 1; i <= N; i++)
				{
					for (j = 1; j <= M; j++)
					{
						if (pre == a[i][j])
						{
							a[i][j] = k;
							a[i][0] += k - pre;
							a[0][j] += k - pre;
						}
					}
				}
			}
		}
		
		out<<"Case #"<<t<<": "<<(yes ? "YES" : "NO")<<endl;
	}
	in.close();
	out.close();
	return 0;
}