#include <bits/stdc++.h>

using namespace std;

int main(){
	
	freopen("A-large.in","r",stdin);
	freopen("A-large-out.txt","w",stdout);
	int teskes;
	scanf("%d",&teskes);
	
	for(int tc=1;tc<=teskes;tc++){
		int n;
		scanf("%d",&n);
		
		bool g=false;
		int ans;
		bool found[15];
		memset(found,false,sizeof found);
		
		for(int x=1;x<=100;x++){
			int now=n*x;
			while(now>0){
				int digit = now%10;
				now/=10;
				found[digit]=true;
			}
			bool temp=true;
			for(int y=0;y<=9;y++){
				if(found[y]==false)temp=false;
			}
			
			if(temp==true){
				ans=n*x;
				g=true;
				break;
			}
		}
		
		if(g==true)printf("Case #%d: %d\n",tc,ans);
		else printf("Case #%d: INSOMNIA\n",tc);
	}
	
	return 0;
}
