/** Author :  Rounak Patni IIIT-H
_._._._._._._._._._._._._._._._._._._._._.*/
                                   
#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <stack>
#include <vector>
#include <cstring>
#include <set>
#include <map>
#include <bitset>
#include <string>
#include <queue>
using namespace std;
int MAX(long long int a, long long int b){if(a > b){return a;}else{return b;}}
int MIN(long long int a, long long int b){if(a < b){return a;}else{return b;}}
int gcd ( long long int a, long long int b ){long long int c;while ( a != 0 ) {c = a; a = b%a;  b = c;}return b;}
//long long int power(long long int  a, long long int  b) { long long int  x=1, y=a; while(b>0) { if(b%2==1) x=(x*y)%mod; y=(y*y)%mod; b=b/2;}     return x; }
int main()
{

	int t;
	int no=1;
	scanf("%d",&t);
	while(t--)
	{
		int a[10][10];
		int b[10][10];
		int n,m;
		int i,j;
		cin >> n;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin >> a[i][j];
			}
		}

		cin >> m;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin >> b[i][j];
			}
		}
		n--;
		m--;
		int count=0;
		int save;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[n][i]==b[m][j])
				{
					save=a[n][i];
					count++;
					break;
				}
			}

		}

		if(count==0)
		{
			printf("Case #%d: Volunteer cheated!\n",no);
		}
		if(count==1)
		{
			printf("Case #%d: %d\n",no,save);
		}
		if(count > 1)
		{
			printf("Case #%d: Bad magician!\n",no);
		}
		no++;

			
	}
	return 0;


}
