//coder: handa.vikalp
#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<string> vs;

#define st          first
#define se          second
#define all(x)      (x).begin(), (x).end()
#define ini(a, v)   memset(a, v, sizeof(a))
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define fr(i,n)     re(i,0,n)
#define tr(i,x)     for(typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define pu          push_back
#define mp          make_pair
#define sz(x)       (int)(x.size())

int c[4][4];
int d[4][4];
int in;
int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int cardFound(int a[], int b[])
{
	int i = 0, j = 0, count=0;
	int k;
	/*
    printf("\nArray A\n");
    for(k=0; k<4; k++)
        printf("%d ", a[k]);

    printf("\nArray B\n");
    for(k=0; k<4; k++)
        printf("%d ", b[k]);
    printf("\n");
    */
	qsort(a,4,sizeof(int), compare);
	qsort(b,4,sizeof(int), compare);

	while(i < 4 && j < 4)
	{
		if(a[i] < b[j])
			i++;
		else if(b[j] < a[i])
			j++;
    else /* if a[i] == b[j] */
		{
			//printf(" %d ", b[j++]);
			in = b[j++];
			count++;
			i++;
		}
	}
	return count;
}

int main(int argc, char const *argv[])
{
	FILE *input = freopen("A-small-attempt0.in","r", stdin);
	FILE *output = freopen("A-small-0.out", "w", stdout);

	int T, retVal,i,j;
	scanf("%d",&T);
	for(int t = 1; t<=T; ++t)
	{
		int r1,r2, count;
		scanf("%d", &r1);
		for(i=0;i<4;i++)
		{
            for(j=0;j<4;j++)
                scanf("%d", &c[i][j]);
		}

		scanf("%d", &r2);
		for(i=0;i<4;i++)
		{
            for(j=0;j<4;j++)
                scanf("%d", &d[i][j]);
		}

		retVal = cardFound(c[--r1], d[--r2]);
		if(retVal == 1)
			printf("Case #%d: %d\n", t, in);
		else if(retVal == 0)
			printf("Case #%d: %s\n", t, "Volunteer cheated!");
		else
			printf("Case #%d: %s\n", t, "Bad magician!");
	}
	fclose(input);
	fclose(output);
	return 0;
}
