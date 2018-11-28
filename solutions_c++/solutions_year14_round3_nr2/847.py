/*
 * totoroXD
 *
 */
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <limits>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <stack>
using namespace std;
typedef long long LL;
const int INF = 1011110000, MOD=1000000000;
const int dx[]={1,0,-1,0}, dy[]={0,1,0,-1};
const double EPS = 1e-6;
typedef long long LL;
int n, per[15], kase=1;
char car[16][111], str[111111];

bool input(){
	scanf("%d",&n);
	for(int i=0; i<n; i++)
		scanf("%s",car[i]);
	return 1;
}
void solve(){
	printf("Case #%d: ",kase++);
	for(int i=0; i<n; i++)
		per[i]=i;
	static bool ap[33];
	int res=0;
	do{
		int k=0, len;
		bool ok=1;

		for(int i=0; i<n; i++){
			len=strlen(car[per[i]]);
			for(int j=0; j<len; j++)
				str[k++] = car[per[i]][j];
		}
		str[k]='\0';
		len = k;

		memset(ap, 0, sizeof(ap));
		for(int i=0; i<k; i++){
			int a=str[i]-'a';
			if(!ap[a]){
				ap[a]=1;
			}else if(str[i-1]!=str[i]){
				ok=0;
				//printf("i=%d\n",i);
				break;
			}
		}
		//printf("%s: %d\n",str, ok);
		if(ok)res++;
	}while(next_permutation(per,per+n));
	printf("%d\n",res);
}
void pre(){
}
int main(){
	pre();
    int zz=1;
    cin>>zz;
    while(zz--){
    	input();
    	solve();
    }
    return 0;
}

/*

3
3
ab bbbc cd
4
aa aa bc c
2
abc bcd

*/

