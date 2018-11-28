#include<bits/stdc++.h>

using namespace std;

int main(){
	freopen("inin.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	char st[105];
	scanf("%d",&t);
	int cur = 0;
	while(t--){
		scanf("%s",st);
		
		int sz = strlen(st);
		
		char prev = st[0];
		int cnt = 0;
		
		for(int i = 1; i < sz; i++){
			if(prev!=st[i]){
				cnt++;
			} 
			prev = st[i];
		}
		
		if(prev == '-') cnt++;
		cout<<"Case #"<<++cur<<": "<<cnt<<endl;
	}
}
