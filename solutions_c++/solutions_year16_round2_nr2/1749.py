#include <bits/stdc++.h>
using namespace std;

const int N = 1e6 + 5;

#define st first
#define nd second
#define make(a,b) make_pair(a,b)

typedef pair<int,int> pun;
typedef long long ll;

char odp1[20], odp2[30];
char sza1[20], sza2[20];
char pom1[20], pom2[20];

void wpisz(int x,int y)
{
  for(int i=0;i<3;i++) pom1[i] = pom2[i] = '0';
  int i = strlen(sza1) - 1;
  while( x > 0 || y > 0)
  {
    pom1[i] = '0' + x % 10;
    pom2[i] = '0' + y % 10;
    x /= 10;
    y /= 10;
    i--;
  }
//  printf("wpisuj %d %d -- %s %s\n",x,y,pom1, pom2);
}

bool OK()
{
  for (int i=0;i<strlen(sza1);i++)
  {
    if ( sza1[i] != '?' && sza1[i] != pom1[i] ) return false;
    if ( sza2[i] != '?' && sza2[i] != pom2[i] ) return false;
  }
  return true;
}

int test()
{ 
  scanf("%s%s",sza1, sza2);
  int MAX = 10;
  if( strlen(sza1) == 2 ) MAX = 100;
  if ( strlen(sza1) == 3 ) MAX = 1000;
  int diff = 2 * MAX;
  int x = 0, y = 0;
  for (int i=0;i<MAX;i++)
    for (int j=0;j<MAX;j++)
    {
      wpisz(i,j);
      if ( OK() &&( abs(i-j) < diff || ( abs(i-j) == diff && i < x ) ||
                                       ( abs(i-j) == diff && i == x && j < y ) ) )
      {
//        printf("wpisz %d %d\n",i,j);
        diff = abs(i-j);
        x = i;
        y = j;
      }
    }
  wpisz(x,y);
  for (int i=0;i<strlen(sza1);i++)
  {
    odp1[i] = pom1[i];
    odp2[i] = pom2[i];
  }
  odp1[strlen(sza1)] = odp2[strlen(sza2)] = 0;
  return 0;
}

void print_test()
{
  auto x = test();
  printf("%s %s", odp1, odp2);
}

int main()
{
	int t;
	scanf("%d",&t);
	for (int i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
    print_test();
    printf("\n");
	}
}
