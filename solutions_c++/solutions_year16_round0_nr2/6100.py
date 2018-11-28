/* ***********************************************
Author        :guanjun
Created Time  :2016/4/9 12:10:47
File Name     :codejamb.cpp
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
#define INF 0x3f3f3f3f
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
struct node{
	int x,dist;
};
bool cmp(int a,int b){
    return a>b;
}
char s[200];

int t, n;
int main()
{
    #ifndef ONLINE_JUDGE
	//freopen("B-large.in","r",stdin);
	//freopen("in.txt","r",stdin);
    #endif
	//freopen("out.txt","w",stdout);
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>s;
		n=strlen(s);
		ll ans=0;
		for(int i=1;i<n;i++){
			if(s[i]=='+'&&s[i-1]=='-')ans++;
			else if(s[i]=='-'&&s[i-1]=='+')ans++;
		}
		if(s[n-1]=='-')ans++;
		printf("Case #%d: %d\n",i,ans);
	}
    return 0;
}
