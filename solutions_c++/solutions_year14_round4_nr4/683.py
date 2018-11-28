#include<cstdio>
#include<string>
#include<map>
#include<iostream>
using namespace std;
int m,n;
string x[8];
int now[8];
int maxx=0;
int maxcnt=0;
void pro(){
	//printf("%d %d %d %d\n",now[0],now[1],now[2],now[3]);
	map<string,int> a[4];
	int cnt=0;
	int same=now[0];
	int flag=(n!=1);
	for(int i=0;i<m;i++){
		if( flag && same!=now[i]) flag=false;
		for(int j=0;j<=x[i].length();j++){
			string sub=x[i].substr(0,j);
			//cout<<sub<<endl;
			if(a[now[i]][sub]!=1){
				a[now[i]][sub]=1;
				cnt++;
			}
		}
	}
	if(flag) return;
	if(maxx<cnt){
		maxcnt=0;
		maxx=cnt;
	//	printf("%d %d %d %d %d\n",maxx,now[0],now[1],now[2],now[3],now[4]);
	}
	if(maxx==cnt){
		maxcnt++;
	//	printf("%d %d %d %d %d\n",maxx,now[0],now[1],now[2],now[3],now[4]);
	}
}
void bktk(int a){
	if(a==m) pro();
	else{
		for(int i=0;i<n;i++){
			now[a]=i;
			bktk(a+1);
		}
	}
	return;
}
int main(){
	int t;
	freopen("D-small-attempt1.in","rt",stdin);
	freopen("D.out","wt",stdout);
	scanf("%d",&t);
	for(int _=1;_<=t;_++){
		maxx=0;
		maxcnt=0;
		fprintf(stderr,"%d\n",_);
		printf("Case #%d: ",_);
		cin>>m>>n;
		for(int i=0;i<m;i++) cin>>x[i];
		bktk(0);
		printf("%d %d\n",maxx,maxcnt);
	}
	return 0;
}