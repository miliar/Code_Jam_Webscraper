#include <bits/stdc++.h>
using namespace std;

const int N = 1e2 + 5;

#define st first
#define nd second
#define make(a,b) make_paiir(a,b)

typedef pair<int,int> pun;
typedef long long ll;

long double  x;
int n;
pair<long double, long double> tab[N];

bool mozna(long double s)
{
	long double suma = 0;
	long double obj = -x;
	long double tmp;
//	printf("mozna %Lf\n",s);
	for (int i=0;i<n;i++)
	{
		tmp = tab[i].st * tab[i].nd * s;
//		printf("tmp %Lf\n",tmp);
		if ( suma + tmp > 0 )
		{
			obj += s*tab[i].nd - ( tmp + suma ) / ( tab[i].st );
//			printf("ojc %Lf\n",obj);
			return obj > 0;
		}
		suma += tmp;
		obj += tab[i].nd * s;
//		printf("suma %Lf obj %Lf\n",suma,obj);
	}
	if ( suma < 0 )
	{
		for (int i=0;i<n;i++)
			tab[i].st *= -1;
		sort( tab, tab+n );
		return mozna(s);
	}
	return obj > 0;
}

void test()
{
	long double c;
	scanf("%d%Lf%Lf",&n,&x,&c);
	for (int i=0;i<n;i++)
		scanf("%Lf%Lf",&tab[i].nd, &tab[i].st);
	for (int i=0;i<n;i++)
		tab[i].st -= c;
	sort( tab, tab+n );
	int p = 0, k = ceil( 10000 * x + 20 );
	while( p < k )
	{
		if ( mozna( (p+k)/2 ) ) k = (p+k)/2;
		else p = (p+k)/2+1;
	}
	if ( k == ceil( 10000 * x + 20 ) )
	{
		printf("IMPOSSIBLE");
		return;
	}
	long double p2 = 1, wynik = p;
	for (int i=0;i<30;i++)
	{
		p2/=2;
		if ( mozna( wynik-p2 ) ) wynik -= p2;
	}
	printf("%.9Lf",wynik);
}

int main()
{
	int t;
	scanf("%d",&t);
	for (int i=1;i<=t;i++)
	{
		printf("Case #%d: ",i );
		test();
		printf("\n");
	}
}
