#include <stdio.h>

void input();
void proc();
void output();

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test,Case=1;
	scanf ("%d",&Test); while (Test--){
		input();
		proc();
		printf ("Case #%d: ",Case++);
		output();
	}

	return 0;
}

int N; long long A,P;

void input()
{
	scanf ("%d %lld",&N,&P);
}

long long gar,can;

long long up(long long m)
{
	long long win,lose,p=A;
	win = m; lose = A - win - 1;

	while (lose){
		p /= 2;
		lose = (lose - 1) / 2;
		win = (win + 1) / 2;
	}

	return p;
}

long long down(long long m)
{
	long long win,lose,p=A,r=1;
	win = m; lose = A - win - 1;

	while (win){
		p /= 2;
		r += p;
		win--;
		win = win / 2;
		lose = (lose + 1) / 2;
	}

	return r;
}

void proc()
{
	long long l,r,m,u;
	
	A = (1ll << N);
	l = 0, r = A - 1; can = l;
	while (l < r){
		m = (l + r) / 2;
		u = up(m);
		if (u <= P){
			if (can < m) can = m;
			l = m + 1;
		}
		else r = m - 1;
	}
	while (up(m) > P){
		m--;
	}
	while (up(m) <= P){
		if (can < m) can = m;
		m++;
		if (m >= A) break;
	}

	l = 0, r = A - 1; gar = l;
	while (l < r){
		m = (l + r) / 2;
		u = down(m);
		if (u <= P){
			if (gar < m) gar = m;
			l = m + 1;
		}
		else r = m - 1;
	}
	while (down(m) > P){
		m--;
	}
	while (down(m) <= P){
		if (gar < m) gar = m;
		m++;
		if (m >= A) break;
	}
}

void output()
{
	printf ("%lld %lld\n",gar,can);
}
