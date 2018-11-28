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
#define pb push_back 
#define vvi vector <vi>
#define rep(x,a,b,c) for(int x=a;x<=b;x+=c)
#define repp(x,a,b) rep(x,a,b,1)
#define rev(x,a,b,c) for(int x=a;x>=b;x-=c)
#define revv(x,a,b) rev(x,a,b,1)
#define OO (int)2e9
#define INF (ll)9e18
 
using namespace std;

int tc,str,n;
char temp[5000];
int list[30];
vi hasil;

int main()
{
	freopen("A-large.in","r",stdin); 
 	freopen("A-large.out","w",stdout);
	scanf("%d",&tc);
	repp(t,1,tc)
	{
		scanf("%s",temp);
		memset(list,0,sizeof(list));
		hasil.clear();
		n=0;
		str=strlen(temp);
		repp(x,0,str-1)
		{
			list[temp[x]-'A'+1]++;
		}
		printf("Case #%d: ",t);
		while(list[26]--)
		{
			hasil.pb(0);
			list[5]--;
			list[18]--;
			list[15]--;
			n++;
		}
		while(list[23]--)
		{
			hasil.pb(2);
			list[20]--;
			list[15]--;
			n++;
		}
		while(list[24]--)
		{
			hasil.pb(6);
			list[19]--;
			list[9]--;
			n++;
		}
		while(list[7]--)
		{
			hasil.pb(8);
			list[20]--;
			list[5]--;
			list[8]--;
			list[9]--;
			n++;
		}
		while(list[19]--)
		{
			hasil.pb(7);
			list[21]--;
			list[5]-=2;
			list[14]--;
			n++;
		}
		while(list[20]--)
		{
			hasil.pb(3);
			list[5]-=2;
			list[8]--;
			list[18]--;
			n++;
		}
		while(list[18]--)
		{
			hasil.pb(4);
			list[6]--;
			list[15]--;
			list[21]--;
			n++;
		}
		while(list[15]--)
		{
			hasil.pb(1);
			list[5]--;
			list[14]--;
			n++;
		}
		while(list[14]>1)
		{
			hasil.pb(9);
			list[14]-=2;
			list[5]--;
			list[9]--;
			n++;
		}
		while(list[6]--)
		{
			hasil.pb(5);
			list[5]--;
			list[9]--;
			list[22]--;
			n++;
		}
		sort(hasil.begin(),hasil.end());
		repp(x,0,n-1)
		{
			printf("%d",hasil[x]);
		}
		printf("\n");
	}
	return 0;
}
