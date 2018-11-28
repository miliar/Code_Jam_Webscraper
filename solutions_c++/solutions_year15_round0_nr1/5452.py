#include <iostream>
#include <set>
#include <vector>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <climits>
#include <utility>
#include <map>
#include <sstream>
#include <cstring>
#define fore(i,m,n) \
for(int i=m;i<n;i++)
#define fori(i,m,n) \
for(int i=m;i<=n;i++)
#define T 10005

using namespace std;
char in[T];
int main()
{
	int test,res,cant,n,caso=0;
	scanf("%d",&test);
	while(test--)
	{
		scanf("%d",&n);
		n++;
		scanf("%s",in);
		res=0;
		cant=(int)(in[0]-'0');
		fore(i,1,n)
		{
			
			if(cant<i && in[i]!='0')
			{
				res+= i-cant;
				cant +=i-cant;
			}
				
			cant+=(int)(in[i] - '0');
			
		}
		printf("Case #%d: %d\n",++caso,res);
	}
}	
