/*ckpeteryu*/
#include<iostream>
#include<iomanip>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<climits>
#include<cmath>
#include<bitset>
#include<string>
#include<ctime>
#include<functional>
#include<map>
#include<set>
#include<vector>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define FOD(i,s,e) for(int i=(s);i>=(int)(e);i--)
#define FORVEC(i,a) for(int i=0;i<(int)((a).size());i++)
#define pb push_back
#define mp make_pair
#define CLR(s,x) memset(s,x,sizeof(s))
#define LL long long int
#define L long int

int nt,mx,cnt,ret;
char s[1005];

int main(int argc, char **argv){
	//ios_base::sync_with_stdio(false);	
	#ifndef GCJ
		//freopen("a1.txt","w",stdout);
		freopen("a2.txt","w",stdout);
	#endif
	
	scanf("%d",&nt);
	FOE(k,1,nt){
		scanf("%d %s",&mx,s);
		ret=cnt=0;
		FOE(i,0,mx){
			if(s[i]>'0'){
				int t=max(0,i-cnt);
				ret+=t;
				cnt+=t;
			}
			cnt+=s[i]-'0';
		}
		printf("Case #%d: %d\n",k,ret);
	}
	return 0;
}