#include<iostream>
#include<cstdio> 
#define rep(i,j,k) for(i=j;i<=k;i++) 

using namespace std;

//FILE *fp1=fopen("input.txt","r");
//FILE *fp2=fopen("A.txt","w");

int a[2000],T,o,i,n,sum,ans;
char ch;
char* s[10000];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	rep(o,1,T){
		printf("Case #%d: ",o);
		scanf("%d",&n);
		rep(i,0,n){
			scanf("%c",&ch);
			while ((ch<'0')||(ch>'9')) 
				scanf("%c",&ch);
			a[i]=ch-'0';
		}
		sum=0;
		ans=0;
		rep(i,0,n){
			if (i>sum){
				ans+=(i-sum);
				sum=i;
			} 
			sum+=a[i];
		}
		printf("%d\n",ans);
	}
} 
