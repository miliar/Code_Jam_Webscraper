#include<bits/stdc++.h>

using namespace std;

string s;
int f[91],fn[10];

int main()
{
	int nt;
	scanf(" %d",&nt);
	for(int t=1; t<=nt; t++)
	{
		memset(f,0,sizeof(f));
		memset(fn,0,sizeof(fn));
		cin >> s;
		for(int i=0; s[i]; i++)
			f[s[i]]++;
		printf("Case #%d: ",t);
		while(f['Z']) { fn[0]++; f['Z']--; f['E']--; f['R']--; f['O']--; }
		while(f['W']) { fn[2]++; f['T']--; f['W']--; f['O']--; }
		while(f['X']) { fn[6]++; f['S']--; f['I']--; f['X']--; }
		while(f['G']) { fn[8]++; f['E']--; f['I']--; f['G']--; f['H']--; f['T']--; }
		while(f['T']) { fn[3]++; f['T']--; f['H']--; f['R']--; f['E']-=2; }
		while(f['U']) { fn[4]++; f['F']--; f['O']--; f['U']--; f['R']--; }
		while(f['O']) { fn[1]++; f['O']--; f['N']--; f['E']--; }
		while(f['F']) { fn[5]++; f['F']--; f['I']--; f['V']--; f['E']--; }
		while(f['S']) { fn[7]++; f['S']--; f['E']--; f['V']--; f['E']--; f['N']--; }
		while(f['N']) { fn[9]++; f['N']--; f['I']--; f['N']--; f['E']--; }
		for(int i=0; i<10; i++) while(fn[i]) { printf("%d",i); fn[i]--; }
		printf("\n");
	}
	return 0;
}
