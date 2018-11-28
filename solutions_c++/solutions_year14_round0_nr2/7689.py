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
	int i,j,tst,cas=1,n;
	double buff,c,f,x,t,pres,rate,same_more,next_more;
	freopen("B-large.in","r",stdin);
	freopen("output2.txt","w",stdout);
	
	scanf("%d",&tst);
	while(tst--){
		scanf("%lf%lf%lf",&c,&f,&x);
		pres=0.0;
		rate=2.0;
		t=0.0;
		while(1){
			same_more=t+(x-pres)/rate;
			buff=c/rate;
			next_more=t+buff+x/(rate+f);

			if(same_more>=next_more){
				t+=buff;
				rate+=f;
			}
			else{break;}
		}
		buff=t+x/rate;
		printf("Case #%d: %.7lf\n",cas++,buff);

	}
	
	

	//system("pause");
	return 0;
}

//freopen("input.txt","r",stdin);
//freopen("output.txt","w",stdout);