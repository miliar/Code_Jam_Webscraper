#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<queue>
#include<cmath>
#define LL long long
using namespace std;
int t,n,b[15],a,c,d;
int main(){
	scanf("%d",&t);
	for (int I=1;I<=t;I++){
		scanf("%d",&n);
		if (!n)
			printf("Case #%d: INSOMNIA\n",I);
		else{
			memset(b,0,sizeof(b));
			d=0;
			c=0;
			while (c!=10){
				d+=n;
				a=d;
				while (a){
					b[a%10]++;
					if (b[a%10]==1) c++;
					a/=10;
				}
			}
			printf("Case #%d: %d\n",I,d);
		}
	}
    return 0;
}

