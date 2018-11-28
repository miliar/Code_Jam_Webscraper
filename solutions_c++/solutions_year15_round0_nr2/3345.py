#include<iostream>
#include<string.h>
using namespace std;
int a[1005],n,mk[1005][1005];
int go(int x,int j){
	int cnt;
	if(mk[x][j]!=-1) return mk[x][j];
	if(x>=j) mk[x][j]=0;
	else mk[x][j]=min(go(x,j-x)+1,go(x,j/2)+go(x,(j+1)/2)+1);
	return mk[x][j];
}
int chk(int x){
	int i,cnt,f,fn=n;
	for(i=cnt=0;i<n;i++)
		cnt+=go(x,a[i]);
	return cnt+x;
}
int main(){
	int m,ans,i,nn,r=1;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>nn;
	memset(mk,-1,sizeof(mk));
	while(nn--){
		cin>>n;
		for(i=m=0;i<n;i++){
			cin>>a[i];
			m=max(m,a[i]);
		}
		ans=chk(1);
		for(i=2;i<=m;i++)
			ans=min(ans,chk(i));
		cout<<"Case #"<<r<<": "<<ans<<endl;
		r++;
	}
	return 0;
}