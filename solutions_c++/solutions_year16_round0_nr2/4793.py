/* ***********************************************
Author        :yuan
Created Time  :2016年04月09日 星期六 10时46分51秒
File Name     :b.cpp
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

string S;
int main()
{
    //freopen("in.txt","r",stdin);
   freopen("out.txt","w",stdout);
   	int T;
   	cin>>T;
   	for(int ca=1;ca<=T;ca++)
	{
		cin>>S;
		int cnt=1;
		for(int i=1;i<S.length();i++)
		{
			if(S[i]!=S[i-1]) cnt++;
		}
		if(S[S.length()-1]=='+') cnt--;
		printf("Case #%d: %d\n",ca,cnt);
	}
    return 0;
}
