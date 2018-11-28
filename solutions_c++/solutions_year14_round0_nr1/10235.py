#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>
#include<climits>
#include<utility>
#define II(x) scanf("%d",&x)
#define OL(x) printf("%lld\n",x)
#define IL(x) scanf("%lld",&x)
#define OI(x) printf("%d\n",x)
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define LL long long
#define INF INT_MAX
#define NINF INT_MIN
#define getcx getchar_unlocked
using namespace std;
int main(){
	int t,n,c,i,j,r;
	LL a1,a2;;
	II(t);
	for(c=1;c<=t;c++){
		a1=a2=0;
		II(r);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++){
				II(n);
				if(i==r){
					a1|=(1<<n);
				}
			}
		II(r);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++){
				II(n);
				if(i==r){
					a2|=(1<<n);
				}
			}
			//cout<<a1<<" "<<a2<<" ";
		a1&=a2;
		//cout<<a1<<endl;
		if(a1==0)
			printf("Case #%d: Volunteer cheated!\n",c);
		else if((a1&(a1-1))==0){
			i=0;
			while(a1>1){
				a1/=2;
				i++;
			}
			printf("Case #%d: %d\n",c,i);
		}
		else
			printf("Case #%d: Bad magician!\n",c);
	}
	return 0;
}