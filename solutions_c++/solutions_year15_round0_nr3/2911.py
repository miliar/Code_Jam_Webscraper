#include <cstdio>
#include <cstring>
#include <algorithm>
#define ABS(x) ((x) < 0 ? -1*(x) : (x))
#define MAX(x,y) ((x) > (y) ? (x) : (y))
#define MIN(x,y) ((x) < (y) ? (x) : (y))
#define mp make_pair
#define MOD 1000000007

using namespace std;
typedef long long ll;
typedef pair<ll,ll> pl;

char lstr[10010];
int str[1000010];
char str1[1000010];

int multmat[9][9] = {{-1,-2,3,4,0,-4,-3,2,1},
					 {2,-1,-4,3,0,-3,4,1,-2},
					 {-3,4,-1,2,0,-2,1,-4,3},
					 {4,3,2,1,0,-1,-2,-3,-4},
					 {0,0,0,0,0,0,0,0,0},
					 {-4,-3,-2,-1,0,1,2,3,4},
					 {3,-4,1,-2,0,2,-1,4,-3},
					 {-2,1,4,-3,0,3,-4,-1,2},
					 {1,2,-3,-4,0,4,3,-2,-1}};

void print(int num)
{
	if(num < 0)
	{
	 	printf("-");
	 	num *= -1;
	}
	
	if(num == 1) printf("1\n");
    else if(num == 2) printf("i\n");
    else if(num == 3) printf("j\n");
    else printf("k\n");
}

int main()
{
	int T,i,j,L,X,mult,sind,eind,len,l,f;
	scanf("%d",&T);
	for(l = 1; l <= T; ++l)
	{
		scanf("%d", &L);
		scanf("%d", &X);

		scanf("%s", lstr);
		str1[0] = '\0';

		while(X > 0)
		{
			strcat(str1, lstr);
			--X;
		}

		f = 0;
		for(i = 0; str1[i]; ++i)
		{
			//printf("%c", str1[i]);
			str[i] = str1[i] - 'g';
		}
		len = strlen(str1);

		if(len < 3)
		{
			printf("Case #%d: NO\n", l);
			continue;
		}
		/*printf("\n");
		for(i = 0; str[i]; ++i)
			printf("%d", str[i]);
		printf("\n");*/

		mult = str[0];
		//print(mult);
		for(i = 1; str1[i]; ++i)
		{
			if(mult == 2)
			{
				f = 1;
				break;
			} 				
			mult = multmat[mult+4][str[i]+4];
			//print(mult);
		}

		if(!f)
		{
			printf("Case #%d: NO\n", l);
			continue;
		}

		sind = i;
		//printf("%d\n", sind);

		mult = str[len-1];
		for(i = len-2; i >= sind; --i)
		{
			if(mult == 4)
			{
				f = 2;
				break;				
			}
			mult = multmat[str[i]+4][mult+4];
			//print(mult);
		}

		if(f == 1)
		{
			printf("Case #%d: NO\n", l);
			continue;
		}

		eind = i;
		//printf("%d\n", eind );
		mult = str[sind];

		for(i = sind+1; i <= eind; ++i)
			mult = multmat[mult+4][str[i]+4];
		
		if(mult == 3)
			printf("Case #%d: YES\n", l);
		else
			printf("Case #%d: NO\n", l);
	}

	return 0;
}
