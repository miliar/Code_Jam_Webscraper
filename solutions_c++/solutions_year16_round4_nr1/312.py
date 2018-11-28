#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<ctime>
#include<algorithm>
#include<iomanip>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<cassert>
#include<bitset>

using namespace std;
typedef long long LL;
const int N=1000000;
int a[3],b[3];
int f[N],n,m;
void build(int x,int l,int r,int t){
	if(x==n){
		f[l] = t;
	}else{
		int mid = (l+r)/2;
		build(x+1,l,mid,t);
		build(x+1,mid,r,(t+2) % 3);
	}
}
char ch[N];
void work(int l,int r){
	if(l+1==r) return;
	int mid = (l+r)/2;
	int len = mid-l;
	work(l,mid);
	work(mid,r);
	bool flag = 0;
	for(int i=0;i<len;i++){
		if(ch[l+i]<ch[mid+i]) break;
		if(ch[l+i]>ch[mid+i]){
			flag=1;
			break;
		}
	}
	if(flag){
		for(int i=0;i<len;i++)
			swap(ch[l+i],ch[mid+i]);
	}
}
int main() {
	freopen("aa.in","r",stdin);
	freopen("aa.out","w",stdout);
	int numcase;
	cin>>numcase;
	for(int ii=1;ii<=numcase;ii++){
		scanf("%d%d%d%d",&n,&a[0],&a[1],&a[2]);
		printf("Case #%d: ",ii);
		m = 1<<n;
		bool flag = 0;
		for(int k=0;k<3;k++){
			build(0,1,m + 1,k);
			b[0]=b[1]=b[2] = 0;
			for(int i=1;i<=m;i++)
				b[f[i]]++;
			if(b[0]==a[0] && b[1]==a[1] && b[2]==a[2]){
				for(int i=1;i<=m;i++){
					if(f[i]==0) ch[i] = 'R';
					if(f[i]==1) ch[i] = 'P';
					if(f[i]==2) ch[i] = 'S';
				}
				work(1,m+1);
				ch[m+1]='\0';
				puts(ch+1);
				flag=1;
				break;
			}
		}
		if(!flag) puts("IMPOSSIBLE");
	}
	return 0;
}
/*
4
1 1 1 0
1 2 0 0
2 1 1 2
2 2 0 2
*/
