#include<cstdio>
#include<map>
#include<algorithm>
using namespace std;
int data[1000];
int data2[1000];
int swap(int a,int b){
	int tmp=data[a];
	data[a]=data[b];
	data[b]=tmp;
}
int main(){
	int t;
	freopen("B-large.in","rt",stdin);
	freopen("B.out","wt",stdout);
	scanf("%d",&t);
	for(int _=1;_<=t;_++){
		printf("Case #%d: ",_);
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			scanf("%d",data+i);
			data2[i]=data[i];
		}
		sort(data2,data2+n);
		int st=0,ed=n-1;
		int cnt=0;
		for(int i=0;i<n;i++){
			int ok;
			for(int j=st;j<=ed;j++){
				if(data2[i]==data[j]){
					ok=j;
					break;
				}
			}
			//printf("%d %d %d\n",ok);
			if(ok-st>ed-ok){//move to ed
				for(int j=ok;j<ed;j++){
					swap(j,j+1);
					cnt++;
				}
				ed--	;
			}else{//move to st
				for(int j=ok;j>st;j--){
					swap(j,j-1);
					cnt++;
				}
				st++;
			}
			//for(int i=0;i<n;i++) printf("%d ",data[i]);
			//printf("\n");
		}
		printf("%d\n",cnt);
	}
}