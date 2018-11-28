#include <bits/stdc++.h>
#define fi first
#define sc second
#define mp make_pair
using namespace std;
typedef long long ll;
typedef pair<int,int> pi;
typedef pair<pi,int> ppi;

char d[109][109];
int dx[4]={0,0,-1,1};
int dy[4]={-1,1,0,0};
bool sp[109][109][4];
vector<ppi> d2;//pos,dir

int main(){
	freopen("A-large.in","r",stdin);
	freopen("out2.txt","w",stdout);
	int tc;scanf("%d",&tc);
	for(int tcno=1;tcno<=tc;tcno++){
		d2.clear();
		int r,c;scanf("%d%d",&r,&c);
				for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				for(int k=0;k<4;k++){
					sp[i][j][k]=0;
				}
			}
		}
		for(int i=0;i<r;i++)scanf("%s",d[i]);
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				if(d[i][j]=='^'){
					d2.push_back(mp(mp(i,j),0));
				}
				else if(d[i][j]=='v'){
					d2.push_back(mp(mp(i,j),1));
				}
				else if(d[i][j]=='<'){
					d2.push_back(mp(mp(i,j),2));
				}
				else if(d[i][j]=='>'){
					d2.push_back(mp(mp(i,j),3));
				}
			}
		}
		//for(int i=0;i<r;i++)printf("%s\n",d[i]);
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				if(j==0){
					sp[i][j][2]=0;
				}
				else{
					if(d[i][j-1]!='.')sp[i][j][2]=1;
					else sp[i][j][2]=sp[i][j-1][2];
				}
			}
			for(int j=c-1;j>=0;j--){
				if(j==c-1){
					sp[i][j][3]=0;
				}
				else{
					if(d[i][j+1]!='.')sp[i][j][3]=1;
					else sp[i][j][3]=sp[i][j+1][3];
				}
			}
		}
		for(int j=0;j<c;j++){
			for(int i=0;i<r;i++){
				if(i==0){
					sp[i][j][0]=0;
				}
				else{
					if(d[i-1][j]!='.')sp[i][j][0]=1;
					else sp[i][j][0]=sp[i-1][j][0];
				}
			}
			for(int i=r-1;i>=0;i--){
				if(i==r-1){
					sp[i][j][1]=0;
				}
				else{
					if(d[i+1][j]!='.')sp[i][j][1]=1;
					else sp[i][j][1]=sp[i+1][j][1];
				}
			}
		}
		/*for(int x=0;x<4;x++){
			for(int i=0;i<r;i++){
				for(int j=0;j<c;j++){
					printf("%d",sp[i][j][x]);
				}
				printf("\n");
			}printf("\n");
		}*/
		int ans=0;
		for(int i=0;i<(int)d2.size();i++){
			int cx=d2[i].fi.sc;
			int cy=d2[i].fi.fi;
			int cd=d2[i].sc;
			if(sp[cy][cx][cd]==1)continue;
			bool legit=false;
			for(int i=0;i<4;i++){
				if(sp[cy][cx][i]==1){
					ans++;legit=true;break;
				}
			}
			if(!legit){
				ans=-1;break;
			}
		}
		if(ans!=-1)
		printf("Case #%d: %d\n",tcno,ans);
		else printf("Case #%d: IMPOSSIBLE\n",tcno);
	}
}
