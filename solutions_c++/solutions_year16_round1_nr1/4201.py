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
#define rep(x,a,b,c) for(int x=a;x<=b;x+=c)
#define repp(x,a,b) rep(x,a,b,1)
#define rev(x,a,b,c) for(int x=a;x>=b;x-=c)
#define revv(x,a,b) rev(x,a,b,1)
#define OO (int)2e9
#define INF (ll)9e18
 
using namespace std;


int tc,b,n;

char list[2000];

deque<char>tmp;

int main(){
	freopen("A-large(1).in","r",stdin);
	freopen("Alarge.out","w",stdout);
	scanf("%d",&tc);
	for(int b=1;b<=tc;b++)
	{
		scanf("%s",list);
		n=strlen(list);
		repp(x,0,n-1)
		{
			if(x==0)
			{
				tmp.push_back(list[x]);
			}
			else if(list[x]>=tmp.front())
			{
				tmp.push_front(list[x]);
			}
			else
			{
				tmp.push_back(list[x]);
			}
		}
		printf("Case #%d: ",b);
		repp(x,0,n-1)
		{
			printf("%c",tmp.front());
			tmp.pop_front();
		}
		printf("\n");
	}
}
