/* ***********************************************
Author        :yuan
Created Time  :2016年04月09日 星期六 10时15分08秒
File Name     :a.cpp
************************************************ */

#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <stdlib.h>
#include <time.h>
#include <queue>
#include <utility>
using namespace std;
#define rep(i,a,b) for(int i=a;i<b;i++)
#define per(i,a,b) for(int i=a-1;i>=b;i--)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define mp make_pair
#define mem0(x) memset(x,0,sizeof(x))
#define memff(x) memset(x,0xff,sizeof(x))
#define fi first
#define se second
#define SZ(x) ((int)(x).size())
typedef long long ll;
typedef vector<int> Vi;
typedef pair<int,int> Pii;
const ll mod=1e9+7;
const double PI=acos(-1);
long long solve(int n)
{
	bool vis[10];
	memset(vis,false,sizeof(vis));
	int cnt=0;
	for(int i=1;;i++)
	{
		long long t=i*n;
		while(t>0)
		{
			if(!vis[t%10])
				{
					cnt++;
					vis[t%10]=true;
				}
			t/=10;
		}
		if(cnt>=10) return (long long)i*n;
	}
}
int T;
int n;
int main()
{
    //freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    /*
   	for(int i=1;i<=500000;i++)
   		cout<<solve(i)<<endl;
   		*/
   	cin>>T;
   	for(int ca=1;ca<=T;ca++)
	{
		cin>>n;	
		
		printf("Case #%d: ",ca);
		if(n==0) cout<<"INSOMNIA"<<endl;
		else cout<<solve(n)<<endl;
	}
    return 0;
}
