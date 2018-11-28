#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cmath>
#include <string>
#include <vector>
#include <cstdio>
#include <cctype>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;
#define   maxnode       15
#define   sigma_size    26
#define   lson          l,m,v<<1
#define   rson          m+1,r,v<<1|1
#define   LL            long long
#define   ull           unsigned long long
#define   mem(x,v)      memset(x,v,sizeof(x))
#define   lowbit(x)     (x&-x)
#define   mk            make_pair

const int    INF   = 0x3f3f3f3f;
const LL     INFF  = 1e18;
const double pi    = 3.141592653589793;
const double inf   = 1e18;
const double eps   = 1e-9;
const LL     mod   = 1e9+7;

/*****************************************************/
inline int RI(){
    int ret=0;
    char tmp;
    while(!isdigit(tmp=getchar()));
    do{
        ret=(ret<<3)+(ret<<1)+tmp-'0';
    }
    while(isdigit(tmp=getchar()));
    return ret;
}
/*****************************************************/

const int MAX = 1e3+5;
char res[MAX<<1],s[MAX];
int comp(int p,int q,int i){
	// cout<<res[p]<<" "<<s[i]<<endl;
	if (res[p]==s[i]){
		// cout<<1<<endl;
		if (p<q)
			return comp(p+1,q,i);
		else
			return 0;
	}
	return (res[p]<s[i] ? 1 : -1);
}
int main(int argc, char const *argv[])
{
	freopen("A-large.in","r",stdin);
	freopen("o.out","w",stdout);
	int T,kase=1;
	scanf("%d",&T);
	while (T--){
		int p=MAX,q=MAX;
		mem(res,0);
		scanf("%s",s);
		int len=strlen(s);
		for (int i=0;i<len;i++){
			if (p==q)
				res[--p]=s[i];
			else{
				if (comp(p,q-1,i)==0)
					res[q++]=s[i];
				else if (comp(p,q-1,i)==-1)
					res[q++]=s[i];
				else
					res[--p]=s[i];
			}
			// cout<<p<<" "<<q<<" "<<res[p]<<" "<<s[i+1]<<endl;
			// cout<<comp(p,q-1,i+1)<<endl;
		}
		int k=0;
		while (!res[k]) k++;
		printf("Case #%d: %s\n",kase++,res+k);
	}
	return 0;
}