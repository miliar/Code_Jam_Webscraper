#include <bits/stdc++.h>
using namespace std;

const int N = 1e6 + 5;

#define st first
#define nd second
#define make(a,b) make_pair(a,b)

typedef pair<int,int> pun;
typedef long long ll;

char pan[N];
bool tab[N];

void flip(int x)
{
  for (int i=0;i<=x;i++) tab[i] = ! tab[i];
}

int test()
{
  scanf("%s",pan);
  int n = strlen(pan);
  for (int i=0;i<n;i++)
    tab[i] = ( pan[i] == '+' );
  int wynik = 0;
  for (int x=n-1;x>=0;x--)
   {
    if ( tab[x] == 0 )
    {
      wynik ++;
      flip(x);
      }
   }
 return wynik;
}

int main()
{
	int t;
	scanf("%d",&t);
	for (int i=1;i<=t;i++)
	{
		printf("Case #%d: %d\n",i,test() );
	}
}
