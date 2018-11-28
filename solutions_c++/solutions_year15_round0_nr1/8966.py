#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<map>
#include<string>
#include<iostream>
#include<stack>
#include<set>
#include<vector>
#include<algorithm>
#include<queue>

using namespace std;

#define EPS (1e-7)
#define PI (acos(-1.0))
#define MAXI(a,b) ((a)>(b)?(a):(b))
#define MINI(a,b) ((a)<(b)?(a):(b))
#define mxx 1005
#define SZOF sizeof
#define SZ size
#define mem(a,b) memset((a),(b),sizeof(a))
#define clr(a) mem(a,0)
typedef long long INT;


int main(){
	int pres,i,j,tst,cas=1,n,need;
	char z[1005];
	freopen("A-large.in","r",stdin);
	freopen("largeout.txt","w",stdout);
	scanf("%d",&tst);
	while(tst--){
		scanf("%d %s",&n,z);
		pres=z[0]-'0';
		need=0;
		for(i=1;i<=n;i++){
			if(pres<i){
				need+=i-pres;
			}
			pres=MAXI(pres,i);
			pres+=z[i]-'0';
		}
		printf("Case #%d: %d\n",cas++,need);
	}
	
	

	//system("pause");
	return 0;
}

//freopen("input.txt","r",stdin);
//freopen("output.txt","w",stdout);