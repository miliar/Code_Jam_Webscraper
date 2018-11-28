#include <cstdio>
#include <set>
using namespace std;
set<int> s;
int t[20][20];
int ch,a,r;
int ans=0;
int cnt=1;
void solve(){
	scanf("%d",&r);
	while(r--){
		s.clear();
		scanf("%d",&a);
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				scanf("%d",&t[i][j]);
				if(i==a) s.insert(t[i][j]);
			}
		}
		ch=0;
		ans=0;
		scanf("%d",&a);
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				scanf("%d",&t[i][j]);
				if(i==a){
					//printf("%d\n",t[i][j]);
					if(s.find(t[i][j])!=s.end()){
						ch++;
						//printf("found\n");
						ans=t[i][j];
					}
				}
			}
		}
		//printf("%d\n",ch);
		printf("Case #%d: ",cnt++);
		if(ch==0) printf("Volunteer cheated!\n");
		else if(ch==1) printf("%d\n",ans);
		else printf("Bad magician!\n");
	}
	return;
}
int main(){
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	solve();
	return 0;
}