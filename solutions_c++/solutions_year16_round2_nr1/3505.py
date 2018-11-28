#include<bits/stdc++.h>
using namespace std;

ifstream goo;
ofstream gle;
string s;
int tab[200], tac[200];

void solve()
{
	int a,b,c;
	for(int i=0; i<190; i++) tab[i]=tac[i]=0;
	goo>>s;
	for(int i=0; i<s.size(); i++)
	{
		a=s[i];
		tab[a]++;
	}
	a=1;
	while(a==1)
	{
		a=0;
		if(tab[88]>0)
		{
			tac[6]++;
			tab[88]--;
			tab[73]--;
			tab[83]--;
			a=1;
		}
		else if(tab[83]>0)
		{
			tac[7]++;
			tab[83]--;
			tab[69]-=2;
			tab[86]--;
			tab[78]--;
			a=1;
		}
		else if(tab[71]>0)
		{
			tac[8]++;
			tab[71]--;
			tab[69]--;
			tab[73]--;
			tab[72]--;
			tab[84]--;
			a=1;
		}
		else if(tab[86]>0)
		{
			tac[5]++;
			tab[86]--;
			tab[69]--;
			tab[70]--;
			tab[73]--;
			a=1;
		}
		else if(tab[70]>0)
		{
			tac[4]++;
			tab[70]--;
			tab[79]--;
			tab[85]--;
			tab[82]--;
			a=1;
		}
		else if(tab[90]>0)
		{
			tac[0]++;
			tab[90]--;
			tab[69]--;
			tab[79]--;
			tab[82]--;
			a=1;
		}
		else if(tab[73]>0)
		{
			tac[9]++;
			tab[73]--;
			tab[78]-=2;
			tab[69]--;
			a=1;	
		}
		else if(tab[78]>0)
		{
			tac[1]++;
			tab[78]--;
			tab[69]--;
			tab[79]--;
			a=1;
		}
		else if(tab[87]>0)
		{
			tac[2]++;
			tab[87]--;
			tab[79]--;
			tab[84]--;
			a=1;
		}
		else if(tab[84]>0)
		{
			tac[3]++;
			tab[84]--;
			tab[69]-=2;
			tab[72]--;
			tab[82]--;
		}
	}
	for(int i=0; i<=9; i++)
	{
		if(tac[i]>0)
		{
			while(tac[i]>0)
			{
				gle<<i;
				tac[i]--;
			}
		}
	}
	gle<<"\n";
	return;
}

int main()
{
	ios_base::sync_with_stdio(false);
	//goo.open("C:\\Users\\Mateusz\\Desktop\\goo.in");
	goo.open("C:\\Users\\Mateusz\\Downloads\\A-small-attempt1.in");
	gle.open("C:\\Users\\Mateusz\\Desktop\\gle.out");
	int t;
	goo>>t;
	for(int i=1; i<=t; i++)
	{
		gle<<"Case #"<<i<<": ";
		solve();
	}
	return 0;
}
