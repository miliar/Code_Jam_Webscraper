#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string.h>
#include <bitset>
#include <queue>
#include <map>
#include <string>
#include <stack>
#include <utility>
#include <queue>
#include <cmath>
#define mp make_pair
#define pii pair<int,int> 
#define ff first
#define ss second
#define ll long long 
#define ull unsigned long long
#define vi vector<int>
#define vii vector<pii>
#define vvi vector <vi>
#define atasx(x,a,b,c) for(int x=a;x<=b;x+=c)
#define atas1(x,a,b) atasx(x,a,b,1)
#define bawahx(x,a,b,c) for(int x=a;x>=b;x-=c)
#define bawah1(x,a,b) bawahx(x,a,b,1)
#define OO (int)2e9
#define INF (ll)9e18
 
using namespace std;

char panecake[200];
int panjang,list[200],tc,posisi,hasil;

int main()
{
	scanf("%d",&tc);
	atas1(t,1,tc)
	{
		scanf("%s",panecake);
		panjang=strlen(panecake);
		hasil=0;
		bawah1(y,panjang-1,0)
		{
			if(panecake[y]=='-')
			{
				hasil++;
				posisi=0;
				if(panecake[0]=='+')
				{
					atas1(x,0,panjang)
					{
						if(panecake[x]=='-')
						{
							//printf("beep%s\n",tmp);
							break;
						}
						
						else
						{
							panecake[x]='-';
						}
					}
					hasil++;
				}
				bawah1(z,y,0)
				{
					if(panecake[z]=='-')
					{
						list[z]=1;
					}
					else
					{
						list[z]=0;
					}
				}
				
				bawah1(z,y,0)
				{
					if(list[posisi]==0)
					{
						panecake[z]='-';
					}
					else 
					{
						panecake[z]='+';
					}
					posisi++;
				}
				
			}
			//printf("%s\n",tmp);
		}
		printf("Case #%d: %d\n",t,hasil);
	}
	return 0;
}
