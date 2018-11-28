#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include<stack>
#include<vector>
#include<cstring>
#include<set>
#include<map>
typedef long long int LL;
typedef unsigned long long int ULL;
#define sf(a) read_int(a)
#define pf(a) printf("%d",a);
#define sz(a) int((a).size())
#define all(c) c.begin(),c.end() //all elements of a container
#define rall(c) c.rbegin(),c.rend() 
#define tr(container,it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) //traversing a container..works for any type of container
#define present(container, element) (container.find(element) != container.end())    //used for set...return 1 if el is ps 0 otherwise
#define cpresent(container, element) (find(all(container),element) != container.end())  //same as present...but is for vectors
using namespace std;
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ABS(x) ((x) > 0 ? (x) : -(x))
#define REP(i, n) for (int i = 0 ; i < (n) ; i ++)
#define FOR(i, s, n) for (int i = (s) ; i < (n) ; i ++)
#define SET(v, val) memset(v, val, sizeof(v))
inline void read_int (int &n)
{
	n = 0;
	int i = getchar_unlocked();
	while (i < '0' || i > '9')
		i = getchar_unlocked();

	while (i >= '0' && i <= '9')
	{
		n = (n << 3) + (n << 1) + (i - '0');
		i = getchar_unlocked();
	}

}
int main()
{
	string a,b;
	int n,t,aa=0;
	sf(t);
	while(t--)
	{
		aa++;
		cin>>a>>n;
		int x=0,flag=0,ans=0;
		for(int i=0;a[i]!='\0';i++)
		{
			for(int j=0;a[j]!='\0';j++)
			{
				x=0;
				flag=0;
				b=a.substr(i,j);
				for(int k=i;k<=j;k++)
				{
					if(a[k]!='a' && a[k]!='e' && a[k]!='i' && a[k]!='o' && a[k]!='u')
						x++;
					else x=0;
					if(x>=n)
					{
						flag=1;
						break;
					}
				}
				if(flag==1)
					ans++;
			}
		}
		printf("Case #%d: %d\n",aa,ans);
	}
	return 0;
}
