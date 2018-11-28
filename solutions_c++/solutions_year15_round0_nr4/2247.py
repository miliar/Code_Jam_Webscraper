#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<utility>
#include<cstring>
#include<cmath>
#define LL long long int
#define mod 1000000007
#define vi vector<int>
#define vvi vector < vi >
#define pii pair<int,int>
#define all(c) c.begin(),c.end()
#define sf(x) scanf("%d",&x);
#define sf2(x,y) scanf("%d%d",&x,&y);
#define mem(a,val) memset(a,val,sizeof(a))
#define nl printf("\n");
#define pb push_back
#define mp make_pair
#define f first
#define s second
using namespace std;
int main()
{	freopen("googleinput.txt","r",stdin);
    freopen("googleoutput.txt","w",stdout);
	int t,i,j,flag,tst,x,r,c;
	sf(t);
	for(tst=1;tst<=t;tst++)
	{	scanf("%d%d%d",&x,&r,&c);
		if((r%x==0||c%x==0)&&(r>(x-2)&&c>(x-2)))
			printf("Case #%d: GABRIEL\n",tst);
		else printf("Case #%d: RICHARD\n",tst);
			
	}
	return 0;
}


