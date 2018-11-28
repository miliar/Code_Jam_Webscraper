#include <bits/stdc++.h>
using namespace std;

const int N = 1e6 + 5;

#define st first
#define nd second
#define make(a,b) make_pair(a,b)

typedef pair<int,int> pun;
typedef long long ll;

bool vis[20];
int digitcount;

void dodaj(long long int x)
{
  while( x > 0 ) 
  {
    if ( vis[x%10] == 0 )
      digitcount ++;
    vis[x%10] = 1;
    x/=10;
  }
  
}

void test()
{
  digitcount = 0;
  for (int i=0;i<10;i++) vis[i] = 0;
  long long int n;
  scanf("%lld",&n);
  if (n == 0)
  {
    printf("INSOMNIA\n");
    return;
  }
  long long int res = 0;
  while( digitcount < 10 )
  {
    res += n;
    dodaj(res);
  }
  printf("%lld\n",res);
}

int main()
{
	int t;
	scanf("%d",&t);
	for (int i=1;i<=t;i++)
	{
		printf("Case #%d: ",i)
    ; test();
	}
}
