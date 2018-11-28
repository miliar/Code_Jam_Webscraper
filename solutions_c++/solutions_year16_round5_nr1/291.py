#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;
char s[33333];
void solve(){
	scanf("%s",s);
	vector<char>V;
	int ans=0;
	for(int i=0;s[i];i++){
		if(V.size()&&V.back()==s[i]){
			ans+=10;
			V.pop_back();
		}
		else V.push_back(s[i]);
	}
	ans+=(int)V.size()/2*5;
	printf("%d\n",ans);
}
int main(){
	freopen("A-large.in.txt","r",stdin);
	freopen("A-large.out.txt","w",stdout);
	int cas=1;
	int _;scanf("%d",&_);
	while(_--){
		printf("Case #%d: ",cas++);
		solve();
	}
}
