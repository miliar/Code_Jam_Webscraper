#include<bits/stdc++.h>

using namespace std;

int found;

void pro(int x){
	while(x){
		int tmp = x%10;
		found|=(1<<tmp);
		x/=10;
	}
}

int main(){
	freopen("inin.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,n;
	scanf("%d",&t);
	int tc = 0;
	while(t--){
		int cur = 1;
		found = 0;
		scanf("%d",&n);
		pro(n);
		while(found != (1<<10)-1){
			cur++;
			pro(n*cur);
			if(cur==1000){
				cur=-1;
				break;
			}
		}
		cout<<"Case #"<<++tc<<": ";
		if(cur!=-1) cout<<n*cur<<endl; else cout<<"INSOMNIA\n";
	}
}
