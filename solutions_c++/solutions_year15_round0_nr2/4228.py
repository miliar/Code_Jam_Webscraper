#include<bits/stdc++.h>
#define ft first
#define sd second
#define pb push_back
#define mp make_pair
#define ll long long
#define rep(i,j,k) for(int i=j;i<k;i++)
#define wez(n) int (n); scanf("%d",&(n));
#define TESTS wez(ltestow)while(ltestow--)
using namespace std;

const int N=1011;
const ll P=1e9+7, INF=2*1e9;

int t,n,a[N],wyn,k;

int main(){
	scanf("%d",&t);
	for(int test=1;test<=t;test++){
		scanf("%d",&n);
		for(int i=0;i<n;i++) scanf("%d",&a[i]);
		wyn=10000;
		for(int i=1;i<=1000;i++){
			k=0;
			for(int j=0;j<n;j++) k+=a[j]/i-(a[j]%i==0);
			wyn=min(wyn,k+i);
		}
		printf("Case  #%d: %d\n",test,wyn);
	}

}

