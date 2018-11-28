#include <stdio.h>
#include <memory.h>

using namespace std;


char S[3000];


void solve()
{
	int c[30];
	int i,j,k;
	int res[10];
	int dt;
	for(i=0;i<26;i++)
		c[i] = 0;
	for(i=0;i<10;i++)
		res[i] = 0;
	for(i=0;S[i] != '\0';i++)
		c[ S[i] - 'A' ] ++;
	
	
	if(c['Z' - 'A']>0)
	{
		dt = c['Z' - 'A'];
		res[0] += dt;
		c['Z' - 'A'] -= dt;
		c['E' - 'A'] -= dt;
		c['R' - 'A'] -= dt;
		c['O' - 'A'] -= dt;
	}
	
	if(c['X' - 'A']>0)
	{
		dt = c['X' - 'A'];
		res[6] += dt;
		c['S' - 'A'] -= dt;
		c['I' - 'A'] -= dt;
		c['X' - 'A'] -= dt;
	}
	
	if(c['W' - 'A']>0)
	{
		dt = c['W' - 'A'];
		res[2] += dt;
		c['W' - 'A'] -= dt;
		c['T' - 'A'] -= dt;
		c['O' - 'A'] -= dt;
	}
	
	if(c['U' - 'A']>0)
	{
		dt = c['U' - 'A'];
		res[4] += dt;
		c['F' - 'A'] -= dt;
		c['O' - 'A'] -= dt;
		c['U' - 'A'] -= dt;
		c['R' - 'A'] -= dt;
	}
	
	if(c['G' - 'A']>0)
	{
		dt = c['G' - 'A'];
		res[8] += dt;
		c['E' - 'A'] -= dt;
		c['I' - 'A'] -= dt;
		c['G' - 'A'] -= dt;
		c['H' - 'A'] -= dt;
		c['T' - 'A'] -= dt;
	}
	
	if(c['T' - 'A']>0)
	{
		dt = c['T' - 'A'];
		res[3] += dt;
		c['T' - 'A'] -= dt;
		c['H' - 'A'] -= dt;
		c['R' - 'A'] -= dt;
		c['E' - 'A'] -= 2*dt;
	}
	
	if(c['F' - 'A']>0)
	{
		dt = c['F' - 'A'];
		res[5] += dt;
		c['F' - 'A'] -= dt;
		c['I' - 'A'] -= dt;
		c['V' - 'A'] -= dt;
		c['E' - 'A'] -= dt;
	}
	
	if(c['I' - 'A']>0)
	{
		dt = c['I' - 'A'];
		res[9] += dt;
		c['N' - 'A'] -= 2*dt;
		c['I' - 'A'] -= dt;
		c['E' - 'A'] -= dt;
	}
	
	if(c['O' - 'A']>0)
	{
		dt = c['O' - 'A'];
		res[1] += dt;
		c['O' - 'A'] -= dt;
		c['N' - 'A'] -= dt;
		c['E' - 'A'] -= dt;
	}
	
	if(c['V' - 'A']>0)
	{
		dt = c['V' - 'A'];
		res[7] += dt;
		c['E' - 'A'] -= 2*dt;
		c['S' - 'A'] -= dt;
		c['V' - 'A'] -= dt;
		c['N' - 'A'] -= dt;
	}
	
	for(i=0;i<10;i++)
		for(j=0;j<res[i];j++)
			printf("%d",i);
	
	printf("\n");
}

int main()
{
	int i, j, k;
	int T, x;

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("A-small-attempt0.out","w",stdout);
	scanf("%d",&T);
	x=1;
	while(T--)
	{
		scanf("%s",&S);
		printf("Case #%d: ",x++);
		solve();
		//printf("%d\n",solve());

	}
	return 0;
}
