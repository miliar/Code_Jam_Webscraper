#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#include<math.h>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<deque>
#include<sstream>
#include<iostream>
#include<stack>
#include<list>
using namespace std;

typedef vector<vector<int> > vii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long LL;

#define sz size()
#define all(n) n.begin(),n.end()
#define clr(a,n) memset(a,n,sizeof(a))
#define pb push_back
#define fo(i,j) for(int i=0;i<j;i++)

int main()
{
    freopen ("B-small-attempt0.in","r",stdin);
    freopen ("B.out","w",stdout);
	
	int T,k=0;
	
	scanf("%d",&T);
	
	while(T--)
	{
		k++;
		int X,Y;
		scanf("%d %d",&X,&Y);
		
		printf("Case #%d: ",k);
		
		if(X>0)
		{
			while(X--)
				printf("WE");
		}
		else if(X<0)
		{
			while(X++)
				printf("EW");
		}
		if(Y>0)
		{
			while(Y--)
				printf("SN");
		}
		else if(Y<0)
		{
			while(Y++)
				printf("NS");
		}
		printf("\n");
	}
}


































