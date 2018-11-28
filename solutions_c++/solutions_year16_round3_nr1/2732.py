#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iomanip>
#include<sstream>
#include<iostream>
#include<string>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<bitset>
#define fou(i,j,k) for (int i=j;i<=k;i++)
#define fod(i,j,k) for (int i=j;i>=k;i--)
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> Pii;

const int maxn=50;
const int inf=0x3f3f3f3f;
const LL infLL=0x3f3f3f3f3f3f3f3fLL;

int a[maxn],sum,n;

void init(){
	scanf("%d",&n);
	sum=0;
	fou(i,1,n){
		scanf("%d",&a[i]);
		sum+=a[i];
	}
}

void solve(){
	int mx,p,cnt,p1,p2;
	cnt=n;
	fou(i,1,sum){
		if (cnt==2){
			fou(j,1,n){
				if (a[j]>0){
					p1=j;
					break;
				}
			}
			fou(j,p1+1,n){
				if (a[j]>0){
					p2=j;
					break;
				}
			}
			if (a[p1]>a[p2]){
				printf("%c ",'A'+p1-1);
				a[p1]--;
			}else
			if (a[p1]<a[p2]){
				printf("%c ",'A'+p2-1);
				a[p2]--;
			}
			fou(i,1,a[p1]){
				printf("%c%c",'A'+p1-1,'A'+p2-1);
				if (i!=a[p1]) printf(" ");
				else printf("\n");
			}
			return;
		}
		mx=0;
		fou(j,1,n){
			if (mx<a[j]){
				mx=a[j];
				p=j-1;
			}
		}
		a[p+1]--;
		if (a[p+1]==0) cnt--;
		printf("%c",'A'+p);
		if (i!=sum) printf(" ");
	}
	printf("\n");
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	fou(i,1,T){
//	while (scanf("",)!=EOF){
		printf("Case #%d: ",i);
		init();
		solve();
	}
	return 0;
}
