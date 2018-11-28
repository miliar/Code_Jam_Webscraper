#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<utility>
#include<vector>
#include<stack>
#include<queue>
#include<deque>
#include<map>
#include<set>
#include<list>
#include<cstring>
#include<string>
#define mp make_pair
#define ff first
#define ss second
#define pb push_back
#define pf push_front
#define pob pop_back
#define pof pop_front
#define OO (int)2e9
#define INF (ll)9e18
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define atasx(x,a,b,c) for(int x=a;x<=b;x+=c)
#define atas1(x,a,b) atasx(x,a,b,1)
#define bawahx(x,a,b,c) for(int x=a;x>=b;x-=c)
#define bawah1(x,a,b) bawahx(x,a,b,1)
using namespace std;
deque<char> urut;
int tc,a;
char input[1010],out[1010];
int main()
{	
	scanf("%d",&tc);
	atas1(i,1,tc){
		scanf("%s",&input);
	a=strlen(input);
	urut.empty();
	atas1(j,0,a){
		if(j==0)urut.pb(input[j]);
		else if(input[j]>=urut.front())urut.pf(input[j]);
		else urut.pb(input[j]);
		
	}
		for(int k=0;k<=a;k++){
		out[k]=urut.front();
		urut.pof();
		}
	printf("Case #%d: ",i);
	atas1(l,0,a-1)printf("%c",out[l]);
	printf("\n");
	
		
	}
	
	return 0;
}
