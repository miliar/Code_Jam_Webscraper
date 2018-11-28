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
#define mxx 10000005
#define SZOF sizeof
#define SZ size
typedef long long INT;



bool check_pali(INT i){
	INT a=0,b=i;
	while(b){
		a*=10;
		a+=(b%10);
		b/=10;
	}
	if(a==i){return 1;}
	return 0;
}

vector < INT > myv;

void pre(){
	int i;
	INT j;
	for(i=1;i<mxx;i++){
		if(check_pali((INT)i)){
			j=i;
			j*=j;
			if(check_pali(j)){
				myv.push_back(j);
			}
		}
		
	}
	
}

int main(){
	int i,j,tst,cas=1,cnt;
	INT n,m;
	freopen("C-large-1.in","r",stdin);
	freopen("output.txt","w",stdout);

	myv.clear();
	pre();
	scanf("%d",&tst);
	while(tst--){
		scanf("%lld%lld",&n,&m);
		cnt=0;
		for(i=0;i<myv.SZ();i++){
			if(myv[i]>=n&&myv[i]<=m){cnt++;}
		}
		printf("Case #%d: %d\n",cas++,cnt);
	}
	
	

	//system("pause");
	return 0;
}

//freopen("input.txt","r",stdin);
//freopen("output.txt","w",stdout);