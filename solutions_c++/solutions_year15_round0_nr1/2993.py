/*********************************************************
  file name: A.cpp
  author : kereo
  create time:  2015年04月11日 星期六 08时40分13秒
*********************************************************/
#include<iostream>
#include<cstdio>
#include<cstring>
#include<queue>
#include<set>
#include<map>
#include<vector>
#include<stack>
#include<cmath>
#include<string>
#include<algorithm>
using namespace std;
typedef long long ll;
const int sigma_size=26;
const int N=100+50;
const int MAXN=100000+50;
const int inf=0x3fffffff;
const double eps=1e-8;
const int mod=1000000000+7;
#define L(x) (x<<1)
#define R(x) (x<<1|1)
#define PII pair<int, int>
#define mk(x,y) make_pair((x),(y))
int n;
char str[N];
int main(){
	int T,kase=0;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	while(T--){
		scanf("%d%s",&n,str);
		int num=0,ans=0;
		int len=strlen(str);
		for(int i=0;i<len;i++){
			if(num>=i){
				num+=str[i]-'0';
				continue;
			}
			ans+=i-num; num=i+(str[i]-'0');
		}
		printf("Case #%d: %d\n",++kase,ans);
	}
	return 0;
}
