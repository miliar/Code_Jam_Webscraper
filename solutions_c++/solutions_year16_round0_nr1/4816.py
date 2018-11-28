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
	int j,tst,cas=1,flag;
	INT n,m,i;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&tst);
	bool visi[10];
	while(tst--){
		scanf("%lld",&n);
		if(n==0){
			printf("Case #%d: INSOMNIA\n",cas++);
			continue;
		}
		clr(visi);
		i=1;
		while(1){
			m=n*i;
			while(m){
				visi[m%10]=1;
				m/=10;
			}
			flag=0;
			for(j=0;j<10;j++){
				if(!visi[j]){flag=1;break;}
			}
			if(j==10){
				break;
			} 
			i++;
		}
		printf("Case #%d: %lld\n",cas++,n*i);
	}
	

	//system("pause");
	return 0;
}

//freopen("input.txt","r",stdin);
//freopen("output.txt","w",stdout);