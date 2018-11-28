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
	int i,j,tst,cas=1,n,k,c,s;
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	scanf("%d",&tst);
	while(tst--){
		scanf("%d%d%d",&k,&c,&s);
		printf("Case #%d:",cas++);
		for(i=1;i<=s;i++){
			printf(" %d",i);
		}
		printf("\n");
	}
	

	//system("pause");
	return 0;
}

//freopen("input.txt","r",stdin);
//freopen("output.txt","w",stdout);