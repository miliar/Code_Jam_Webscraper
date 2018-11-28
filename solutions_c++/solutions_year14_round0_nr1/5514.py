#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cctype>
#include <ctime>
#pragma comment(linker,"/STACK:102400000,102400000")
#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <stack>

#define SQR(x) ((x)*(x))
#define rep(i, n) for (int i=0; i<(n); ++i)
#define repd(i,n)  for(int i=1;i<=(n);++i)
#define repf(i, a, b) for (int i=(a); i<=(b); ++i)
#define reps(i, a, b) for (int i=(a); i>=(b); --i)
#define PB push_back
#define MP(A, B) make_pair(A, B)
#define pow2(n) (1<<(n))
#define pi acos(-1)
#define eps 0.00000001
#define lg(n) log10((n)*1.0)
#define MaxN  500010
#define mod 1000000007
#define mod2 1000000009
#define mod3 1000007
#define inf 1000100000
#define inf2 0x7fffffffffffffff
#define ll __int64
#define typed int
using namespace std;
void data(){
   freopen("data.in","r",stdin);
   freopen("data.out","w",stdout);
}
int RES[17];

int main(){
	//data();
	int T,t=1;
	cin>>T;
	while(T--){
		memset(RES,0,sizeof(RES));	   
        int a,ch,cnt=0,cur=-1;
		for(int k=0;k<2;k++){
	        scanf("%d",&ch);
			for(int i=1;i<=4;i++){
 		        for(int j=0;j<4;j++){
		    	    scanf("%d",&a);
					if(i==ch) RES[a]++;	
			    }
			}	
		}
		for(int i=1;i<=16;i++){if(RES[i]==2){cnt++;cur=i;}}
		printf("Case #%d: ",t++);
		if(cnt==0) printf("Volunteer cheated!\n");
		else if(cnt==1) printf("%d\n",cur);
		else printf("Bad magician!\n");	   
	}
	return 0;
}
