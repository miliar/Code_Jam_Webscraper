#include<iostream>
#include<string>
#include<algorithm>
#include<bitset>
#include<cassert>
#include<cstring>
#include<cmath>
#include<cstdio>
#include<queue>
#include<stack>
#include<vector>
#include<ctime>
#include<map>
#include<set> 
#include<cctype>
#include<cstdlib>
using namespace std;
const int INF = 0x3f3f3f3f;
const double eps = 1e-6;
const int maxn = 1000010;
const int maxe = 2*maxn*maxn;
typedef unsigned long long ULL;
///////////////////////////////////////////////////////////////////////////////////
int T,n;
char str[maxn];
bool inline isu(char c){
	if(c == 'a' || c == 'e' || c =='i' || c=='o' || c=='u') return true;
	return false;
}
int main(){
	//freopen("in.txt","r",stdin);
	freopen("A-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(int cs=1; cs <=T; ++cs){
		printf("Case #%d: ",cs);
		scanf("%s %d",str,&n);
		int pre = -1,p = 0,q = 0,len = strlen(str);
		int ans = 0;
		while(p + n <= len){
			for(;q < p + n; ++q){
				if(isu(str[q])) break;
			}
			if(q == p + n){
				ans += (p + 1)*(len - q + 1);
				if(pre != -1){
					ans -= pre * (len - (q-1));
				}
				pre = p + 1;
				p = p + 1;
			}else{
				p = q = q + 1;
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}