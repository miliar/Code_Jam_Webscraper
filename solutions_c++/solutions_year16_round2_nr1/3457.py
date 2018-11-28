#include <bits/stdc++.h>
using namespace std;

const int N = 1e6 + 5;

#define st first
#define nd second
#define make(a,b) make_pair(a,b)
#define count lol
typedef pair<int,int> pun;
typedef long long ll;



/*tab[0] = "ZERO"
tab[1] = "ONE"
tab[2] = "TWO";
tab[3] = "THREE"
tab[4] = "FOUR"
tab[5] = "FIVE"
tab[6] = "SIX"
tab[7] = "SEVEN"
tab[8] = "EIGHT", "NINE"
*/
char count[356];
char slo[N];

void policz(vector<int> &odp, int x, char uniq, vector<char> dec)
{
  int y = count[uniq];
  odp[x] += y;
    for(char o : dec) count[o] -= y;
  assert( count[uniq] == 0 );
    }
  
vector<int> test()
{
  scanf("%s", slo);
  int n = strlen(slo);
  for (int i=0;slo[i];i++)
    count[ slo[i] ] ++;
  vector<int> odpowiedz;
  odpowiedz.resize(10);
  policz( odpowiedz, 0, 'Z', {'Z', 'E', 'R', 'O'} );
  policz( odpowiedz, 2, 'W', {'T', 'W', 'O'} );
  policz( odpowiedz, 4, 'U', {'F', 'O', 'U', 'R'} );
  policz( odpowiedz, 5, 'F', {'F', 'I', 'V', 'E'} );
  policz( odpowiedz, 6, 'X', {'S', 'I', 'X'} );
  policz( odpowiedz, 7, 'V', {'S', 'E', 'V', 'E', 'N'} );
  policz( odpowiedz, 8, 'G', {'E', 'I', 'G', 'H', 'T'} );
  policz( odpowiedz, 9, 'I', {'N', 'I', 'N', 'E'} );
  policz( odpowiedz, 1, 'N', {'N', 'O', 'E'} );
  policz( odpowiedz, 3, 'T', {'T', 'H', 'E', 'R', 'E'} );
  return odpowiedz;
    }

void print_test()
{
  auto x = test();
  for (int i=0;i<10;i++)
    for (int j=0;j<x[i];j++)
      printf("%d", i);
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
