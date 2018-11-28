#include <bits/stdc++.h>
using namespace std;

const int MX = 14;

int n, ile[5];
string wynik ;

string gene(char z, int level)
{
	if (level == n+1)
	{
		string xd;
		xd += z;
		return xd;
	}
	
	if (z == 'R')
	{
		string a = gene('R', level + 1);
		string b = gene('S', level + 1);
	
	//	printf("%c na poziomie %d\n", z, level);	
	//	cout << a << endl;
	//	cout << b << endl;
		
		if (a < b)
		{
			return a + b;
		}
		else
		{
			return b + a;
		}
	}
	
	if (z == 'S')
	{
		string a = gene('P', level + 1);
		string b = gene('S', level + 1);

	//		printf("%c na poziomie %d\n", z, level);	
	//	cout << a << endl;
	//	cout << b << endl;

		
		if (a < b)
		{
			return a + b;
		}
		else
		{
			return b + a;
		}
	}
	
	if (z == 'P')
	{
		string a = gene('R', level + 1);
		string b = gene('P', level + 1);

	//	printf("%c na poziomie %d\n", z, level);	
	//	cout << a << endl;
	//	cout << b << endl;
		
		if (a < b)
		{
			return a + b;
		}
		else
		{
			return b + a;
		}
	}
}	

void solve()
{
	int r, p, s; scanf("%d%d%d%d", &n, &r, &p, &s);
	
	string W="ZZZ";
	
	ile[0]=ile[1]=ile[2]=0;
	string w = gene('P', 1);
	for (int i = 0; i < (int) w.size(); ++ i)
	{
		if (w[i] == 'R')
		{
			ile[0] ++;	
		}
		if (w[i] == 'P')
		{
			ile[1] ++;
		}
		if (w[i] == 'S')
		{
			ile[2] ++;
		}
	}
//	cout << ile[0] << " " << ile[1] << " " << ile[2] <<endl;
	if (ile[0] == r && ile[1] == p && ile[2] == s)
	{
		W=min(w,W);	
	}
	
	ile[0]=ile[1]=ile[2]=0;
	w = gene('S', 1);
	for (int i = 0; i < (int) w.size(); ++ i)
	{
		if (w[i] == 'R')
		{
			ile[0] ++;	
		}
		if (w[i] == 'P')
		{
			ile[1] ++;
		}
		if (w[i] == 'S')
		{
			ile[2] ++;
		}
	}
	if (ile[0] == r && ile[1] == p && ile[2] == s)
	{
		W=min(w,W);	
	}
	
		ile[0]=ile[1]=ile[2]=0;
	w = gene('R', 1);
	for (int i = 0; i < (int) w.size(); ++ i)
	{
		if (w[i] == 'R')
		{
			ile[0] ++;	
		}
		if (w[i] == 'P')
		{
			ile[1] ++;
		}
		if (w[i] == 'S')
		{
			ile[2] ++;
		}
	}
	if (ile[0] == r && ile[1] == p && ile[2] == s)
	{
		W=min(w,W);	
	}
	
	
	if(W=="ZZZ")puts("IMPOSSIBLE");
	else
	 cout << W<< endl;
}

int main()
{
	int q; scanf("%d", &q);
	for (int ttt = 1; ttt <= q; ++ ttt)
	{
		printf("Case #%d: ", ttt);
		solve();
	}
	return 0;
}
