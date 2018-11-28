/* ***********************************************
Author        :guanjun
Created Time  :2016/4/9 13:18:39
File Name     :codejama.cpp
************************************************ */
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <iomanip>
#include <list>
#include <deque>
#include <stack>
#define ull unsigned long long
#define ll long long
#define mod 90001
#define INF 1ll<<60
#define maxn 10010
#define cle(a) memset(a,0,sizeof(a))
const ull inf = 1LL << 61;
const double eps=1e-5;
using namespace std;
priority_queue<int,vector<int>,greater<int> >pq;
struct Node{
	int x,y;
};
struct cmp{
    bool operator()(Node a,Node b){
        if(a.x==b.x) return a.y> b.y;
        return a.x>b.x;
	}
};

bool cmp(int a,int b){
    return a>b;
}
int vis[10];
int check(ll a){
	while(a>0){
		vis[a%10]=1;
		a/=10;
	}
	for(int i=0;i<10;i++)if(vis[i]==0)return 0;
	return 1;
}
int main()
{
    #ifndef ONLINE_JUDGE
    //freopen("A-large.in","r",stdin);
    #endif
	//freopen("out.txt","w",stdout);
    int t;
	ll n,x,ans;
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>n;
		cle(vis);
		ans=0;
		ll j=1;
		x=n;
		while(x<=INF){
			x=j*n;
			if(check(x)||x==0){
				ans=x;break;
			}
			j++;
		}
		if(ans==0){
			printf("Case #%d: INSOMNIA\n",i);
		}
		else printf("Case #%d: %lld\n",i,ans);
	}
    return 0;
}
