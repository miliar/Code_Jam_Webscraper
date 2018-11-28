#include<bits/stdc++.h>

using namespace std;

int cnt[20];
int x,r,T;

int main(){
	scanf("%d",&T);
	int caso=0;
	while(T--){
		scanf("%d",&r);
		r--;
		memset(cnt,0,sizeof(cnt));
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&x);
				if(i==r)cnt[x]++;
			}
		}
		scanf("%d",&r);
		r--;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&x);
				if(i==r)cnt[x]++;
			}
		}
		int ans=-1;
		bool ch=0;
		for(int i=1;i<=16;i++){
			if(cnt[i]==2){
				if(ans!=-1)ch=1;
				ans=i;
			}
		}
		printf("Case #%d: ",++caso);
		if(ch)puts("Bad magician!");
		else{
			if(ans==-1)puts("Volunteer cheated!");
			else cout<<ans<<"\n";
		}
	}
}