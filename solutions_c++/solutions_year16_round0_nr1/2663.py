#include<bits/stdc++.h>

#define LL long long
#define MP make_pair
#define PB push_back
#define MAXN 1000000
using namespace std;
int n;
int t;
int v,ans;
bool f[33];

bool cek(){
	for(int i=0;i<10;i++)
		if(f[i]==0)	return 0;
	return 1;
}
void update(int v){
	while(v>0){
		f[v%10]=1;
		v/=10;
	}
}
int main(){
	scanf("%d",&t);
	for(int z=1;z<=t;z++){
		ans = 0;
		printf("Case #%d: ",z);
		scanf("%d",&n);
		ans = 0;
		memset(f,0,sizeof(f));
		if(n==0){
			printf("INSOMNIA\n");
			continue;
		}
		for(int i=n,j=0;j<1000;i+=n,j++){
			update(i);
			if(cek()){
				ans = i;
				break;
			}
			if(j==999){
				ans = -1;
			}
		}
		if(ans==-1)	printf("INSOMNIA\n");
		else	printf("%d\n",ans);
	}
	return 0;
}