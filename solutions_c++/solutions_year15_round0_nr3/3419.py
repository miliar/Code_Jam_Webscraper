#include <iostream>
#include <cstring>
using namespace std;

int a[5][5] = 
{
	{0, 1, 2, 3, 4},
	{1, 1, 2, 3, 4},
	{2, 2, -1, 4, -3},
	{3, 3, -4, -1, 2},
	{4, 4, 3, -2, -1}
};
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	scanf("%d\n", &T);
	for (int tt = 1; tt <= T; tt++)
	{
		bool fl = 0;
		int q, p, ans;
		int r, X, L;
		scanf("%d %d\n", &X, &L);
		int idi = 2*X + 1,  idk = 0, idmi = 2*X + 1, idmk = 0;
		char c[10010];
		gets(c);
		p =  (int)(c[0] - 'g');
		ans = p;
		if(p == 2)
			idi = 1ll;
		else if (p == 4)
			idk = 1ll;

		for(int i = 1; i<X; i++)
		{
			q = (int)(c[i] - 'g');
			ans = (ans > 0 ? a[p][q] : - a[p][q]);
			r = (long long)(i+1);

			if(ans == 2 && r < idi)
				idi = r;
			else if (ans == -2 && r < idmi)
				idmi = r;
			else if (ans == 4 && r > idk)
				idk = r;
			else if (ans == -4 && r > idmk)
				idmk = r;
			p = abs(ans);
		}
		scanf("\n");
		if (ans == 1 || (ans == -1 && !(L%2)) || (ans != -1 && L%4 != 2))
			fl = 0;
		else 
		{
			if(ans != -1)
			{
				for(int i = 0; i<X; i++)
				{
					q = (int)(c[i] - 'g');
					ans = (ans > 0 ? a[p][q] : - a[p][q]);
					r = (long long)(i+1);

					if(ans == 2 && r < idi)
						idi = r;
					else if (ans == -2 && r < idmi)
						idmi = r;
					else if (ans == 4 && r > idk)
						idk = r;
					else if (ans == -4 && r > idmk)
						idmk = r;
					p = abs(ans);
				}
			}
			if ((idk == 0 && idmk == 0) || (idi == 2*X + 1 && idmi == 2*X + 1))
				fl = 0;
			else
			{
				if((ans == -1 && L == 1) || L == 2)
				{
					fl = (idi < idk);
				}
				else if((idi < idk) || (idi < idmk) || (idmi < idk) || (idmi < idmk))
					fl = 1;
				else {
					if(idi < 2*X + 1)
						fl = 1;
					else if (idk > 0)
						fl = 1;
					else
						fl = 0;
				}
			}
		}
		if(fl)
			printf("Case #%d: YES\n", tt);
		else
			printf("Case #%d: NO\n", tt);
	}
	return 0;
}