#include <bits/stdc++.h>

#define ll long long

using namespace std;

//int primes[70005];
ll ans[14];
ll truth[15];
ll pw[12][25];


int main(){
	freopen("C-small.txt","w",stdout);
	printf("Case #1:\n");
	
	ll now[20];
	now[0]=1;
	now[15]=1;
	
	for(ll x=2;x<=10;x++){
		pw[x][0]=1;
		for(int y=1;y<=17;y++){
			pw[x][y] = pw[x][y-1]*x;
			//cout<<x<<" "<<y<<" "<<pw[x][y]<<endl;
		}
	}
	
	int found=0;
	for(int x=0;x<=70000;x++){
		
		ll temp=x;
		for(int y=14;y>=1;y--){
			now[y]=temp%2;
			temp/=2;
		}
		
		bool g=true;
		for(int y=2;y<=10;y++){
			ll t=0;
			for(int z=0;z<=15;z++){
				t+=(long long)(now[15-z]*pw[y][z]);
				//cout<<(long long)(now[z]*pw[y][z])<<endl;
			}
			truth[y]=t;
			if(t%2==0){ans[y]=2; continue;}
			
			bool nprime=false;
			for(ll z=3;z<=sqrt(t);z++){
				if(t%z==0){
					nprime=true;
					ans[y]=z;
					break;
				}
			}
			if(nprime==false){
				g=false;
				break;
			}
		}
		
		if(g==true){
			found++;
			for(int y=0;y<=15;y++)printf("%lld",now[y]);
			for(int y=2;y<=10;y++)printf(" %lld",ans[y]);
			printf("\n");
		}
		
		
		if(found>=50)break;
	}
	
	return 0;
}
