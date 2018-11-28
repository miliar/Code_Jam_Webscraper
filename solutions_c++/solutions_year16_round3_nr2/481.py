/*****************************************************/
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
const int    maxmat= 10;

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

int main(int argc, char const *argv[])
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin>>T;
	int N;
	LL M;
	for (int kase=1;kase<=T;kase++){
		cin>>N>>M;
		LL t=1;
		for (int i=1;i<=N-2;i++) t<<=1;
		printf("Case #%d:",kase);
		if (M>t) printf(" IMPOSSIBLE\n");
		else{
			printf(" POSSIBLE\n");
			cout<<0; t>>=1;
			for (int i=1;i<N-1;i++){
				// cout<<t<<endl;
				if (M>=t){
					printf("1");
					M-=t;
				}
				else      printf("0");
				t>>=1;
			}
			if (M)  cout<<1<<endl;
			else
			   	cout<<0<<endl;
			// cout<<endl;
			for (int i=1;i<N;i++){
				for (int j=0;j<N;j++)
					printf("%d",(i<j ? 1 : 0));
				printf("\n");
			}
		}
	}
	return 0;
}